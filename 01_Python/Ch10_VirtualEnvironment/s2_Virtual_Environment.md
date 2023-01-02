# Virtual Environment

* A Python virtual environment is a tool that allows you to create an isolated environment for your Python projects.

* It can be useful to package your project and it's dependecies in separate environments for different projects, each with their own packages and dependencies.

* It can also be useful to manage multiple python versions that can be used in multiple projects.

---

<br>

## Commands in Ubuntu

* Check default Python version and all availabe Python versions

```python

# Default python version of the system
$ python3 --version

# Lists all python executales/versions installed on your system
$ ls /usr/bin/python*

```

<br>

* Change the default Python version

```python

# To set a particular version as default version of python
$ sudo update-alternatives --install /usr/bin/python3.6 python /usr/bin/python3.11 1

```

> **update-alternatives** command is used to manage alternative programs on ubuntu.

> **--install** is used to install a new alternative that takes 3 arguments

> **/usr/bin/python3.6 python /usr/bin/python3.11** --> makes Python3.11 as alternative to 3.6

> **'1'** is the priority of the alternative. Higher priority means that the alternative will be preferred over others.
  
<br>

* Install virtualenv

```python

$ pip install virtualenv

# Create Virtual env for version 3.8
$ virtualenv -p /usr/bin/python3.8 py_env_3.8
```

> The above command will create a virtual environment that will have python3.8 version.

> the -p option is used to specify which version on python to be used to create the virtual environment.

<br>

* The below command will create a virtual environment with the default python version on the system.
  
```python
$ virtualenv py_env
```

<br>

* To activate the virtual environment

```python
$ source py_env_3.8/bin/activate
```

<br>

```python
# To see all the packages installed in the current environment with their version numbers.
$ pip list

# pip freeze is similar to pip list but it generates o/p that is suitable for requirements file.
$ pip freeze

#---local tells to only include packages in the current environment, rather than globally
$ pip freeze --local > requirements.txt
```

<br>


* To deactivate the virtual env

```python
$ deactivate
```

<br>