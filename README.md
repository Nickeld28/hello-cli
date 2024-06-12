# Hello_CLI

## Description
This is a tutorial pet-project to learn how to create your own 
 Python console utilities

## Clone project

```shell
git clone <project_URL>
```

## Install packages

```shell
pip install -U -r requirements.txt
```

## Build program

```shell
pyinstaller hello-cli.py
```

## Install program

### Windows

Replace directory `\hello-cli` from `\dist` to `C:\Users\<username>` or another path in your OS.

Add path `C:\Users\<username>\hello-cli` (or another path in your case) to PATH in Windows environment variables.

## Using example

In any place open your terminal and write a command:

```shell
C:\>hello-cli
12-Jun-24 16:53:47 - INFO - Hello World!
```

```shell
C:\>hello-cli User
12-Jun-24 16:55:35 - INFO - Hello User!
```
