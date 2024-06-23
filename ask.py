#!/home/svobop/PycharmProjects/ollama_sandbox/.venv/bin/python
import ollama
import subprocess
import click
import json

@click.command()
@click.option('--model', default='phi3', help='ollama model')
@click.argument('question')
def ask(question, model):
    """Aks ollama to about linux commands"""
    response = ollama.chat(model=model, messages=[
        {
            'role': 'system',
            'content': 'You are a friendly and helpful linux expert. You have the context for the operating system and you will consider it in you response. The response must be in valid json. First key will be "cmd" with valid linux command if the task is clear and can be accomplished with a linux command or null value if not, second key will be "explain" where you break down what the command does step by step or explain why it is not possible. Third key will be "dangerous" boolean to set to true if the command could cause irreversible damage.',
        },
        {
            'role': 'system',
            'content': subprocess.run(['cat', '/etc/os-release'], capture_output=True, text=True).stdout
        },
        {
            'role': 'user',
            'content': question
        }
    ])
    response = response['message']['content'].strip().strip('`')
    if response.startswith('json'):
        response = response[4:]
    try:
        response = json.loads(response)
    except Exception as e:
        raise ValueError(f'Invalid response from the model \n {response} \n {repr(e)}')

    cmd = response.get("cmd")
    explain = response.get("explain")
    if explain.startswith('This command'):
        explain = f'The command "{cmd}"{explain[12:]}'
    dangerous = response.get("dangerous")
    if cmd and not dangerous:
        click.echo(explain)
        click.confirm(f'Do you want to execute "{cmd}"?', abort=True)
        subprocess.run(cmd.split(' '))
    elif explain:
        click.echo(explain)
    elif explain and dangerous:
        click.secho(explain, fg='green')
    else:
        raise ValueError(f'Invalid response from the model \n {response}')


if __name__ == '__main__':
    ask()
