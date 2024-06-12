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

## Using example

In any place open your terminal and write a command:

```shell
hello-cli
12-Jun-24 16:53:47 - INFO - Hello World!
```

```shell
hello-cli User
12-Jun-24 16:55:35 - INFO - Hello User!
```
