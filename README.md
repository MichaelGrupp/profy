# profy

***quickly profile Python commands with cProfile and Snakeviz***

---

## Installation

```
pip install profy
```

## Overview

profy doesn't do much, but it saves some time if you want to quickly profile a Python script or an entry point executable and view the result in your browser with [snakeviz](https://github.com/jiffyclub/snakeviz/)

Instead of:

```
python -m cProfile -o out.prof my_script.py --some_option
snakeviz out.prof
```

just type `profy` in front of your command:

```
profy my_script.py --some_option
```

### Entry Points

profy is able to detect whether the command is a script-file or a globally installed entry point executable.

For example, we can profile a `pip` command:

```
profy pip search numpy --timeout 5
```

or even profy itself:

```
profy profy
```
