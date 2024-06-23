# CmdLlama

Simple cli script to ask ollama to generate and explain script and optionally execute the generated script.

# Installation

[Install ollama](https://ollama.com/download) and pull model of your choice. This was tested with [phi3](https://ollama.com/library/phi3).

Clone this and install the utility with setuptools
```commandline
python3 -m venv .venv
. .venv/bin/activate
pip install --editable .
```

You might want to add .venv/bin/activate/Script to the path.

# Usage

Use at your own risk. It doesn't do anything to your system without confirmation. It should warn about dangerous commands but what is and isn't dangerous is determined by the model.

`/etc/os-release` is inserted into the prompt so that it knows which package manager to use.

```commandline
$ ask "install firefox"
The command "sudo dnf install firefox" uses the 'dnf' package manager, which is specific to Fedora and other Red Hat-based Linux distributions. The 'install' option tells it that you want to install a new software package (in this case, Firefox). The 'firefox' keyword specifies the name of the package you wish to install.
Do you want to execute "sudo dnf install firefox"? [y/N]:  
```