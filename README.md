# Hello_CLI

## Description
This is a tutorial pet-project to learn how to create your own 
 Python console utilities

## Clone project

```shell
git clone <project_URL>
```

## Onen project directory

```shell
cd hello-cli
```

## Install packages

### Linux

```shell
python3 -m pip install -U -r requirements.txt
```

### Windows

```shell
python -m pip install -U -r requirements.txt
```

## Build program

### Linux

```shell
python3 -m PyInstaller hello-cli.py
```

### Windows

```shell
pyinstaller hello-cli.py
```

## Install program

### Linux

```shell
cd dist/hello-cli
cp hello-cli ~/.local/bin/; cp -R _internal/ ~/.local/bin/_internal/
```

### Windows

Copy directory `\hello-cli` from `\dist` to `C:\Users\<username>` or another path in your OS.

Add path `C:\Users\<username>\hello-cli` (or another path in your case) to PATH in Windows environment variables.

### Help

```shell
usage: hello-cli [options] [NAME]

This program prints "Hello [NAME]".

positional arguments:
  name           name of whom to greet
  unrecognized   unrecognized args will be ignored

options:
  -h, --help     show this help message and exit
  -v, --verbose  enable verbose output
  -d, --debug    enable debug output
```

## Using example

In any place open your terminal and write a command:

```shell
hello-cli
Hello World!
```

```shell
hello-cli User
02-Jul-24 21:29:17 - DEBUG - Namespace(name='User', verbose=True, debug=True, unrecognized=[])
02-Jul-24 21:29:17 - INFO - Hello User!
```
