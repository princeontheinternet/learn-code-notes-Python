# Virtual Environment

* A Python virtual environment is a tool that allows you to create an isolated environment for your Python projects.

* It can be useful to package your project and it's dependecies in separate environments for different projects, each with their own packages and dependencies.

* It can also be useful to manage multiple python versions that can be used in multiple projects.

---

## Managing multiple python versions using virtualenv

* Check default Python version and all availabe Python versions

```shell

# Default python version of the system
$ python3 --version

# Lists all python executales/versions installed on your system
$ ls /usr/bin/python*

```

* Change the default Python version

```shell

# To set a particular version as default version of python
$ sudo update-alternatives --install /usr/bin/python3.6 python /usr/bin/python3.11 1

```

> **update-alternatives** command is used to manage alternative programs on ubuntu.

> **--install** is used to install a new alternative that takes 3 arguments

> **/usr/bin/python3.6 python /usr/bin/python3.11** --> makes Python3.11 as alternative to 3.6

> **'1'** is the priority of the alternative. Higher priority means that the alternative will be preferred over others.
  

* Install virtualenv

```shell

$ pip install virtualenv
