# Virtual Environment

* A Python virtual environment is a tool that allows you to create an isolated environment for your Python projects.

* It can be useful to package your project and it's dependecies in separate environments for different projects, each with their own packages and dependencies.

* It can also be useful to manage multiple python versions that can be used in multiple projects.

---

<br>

## Commands in Linux/Mac

* ### Check default Python version and all availabe Python versions

```python

# Default python version of the system
$ python3 --version

"""LINUX"""
# Lists all python executales/versions installed on your system
$ ls /usr/bin/python*

"""WINDOWS"""
C:\> where python
```

---

* ### Using venv (built-in module)

  * venv is included with the Python standard library, so it doesn't require an additional package to be installed.

```python
# Runs on all platforms (Windows, Linux or Mac)
python3.8 -m venv py_env_3.8
```

> the -m option is to run module venv as a script to create virtual env.

---

<br>

* ### Using virtualenv (third-party package)

```python

$ pip install virtualenv

"""LINUX"""
# Create Virtual env for version 3.8
$ virtualenv -p /usr/bin/python3.8 py_env_3.8

"""WINDOWS"""
C:\> virtualenv -p C:\Pytho38\python.exe py_env_3.8

```

> The above command will create a virtual environment that will have python3.8 version.

> the -p option is used to specify which version on python to be used to create the virtual environment.

---

<br>

* ### The below command will create a virtual environment with the default python version on the system
  
```python
#uisng venv
python3 -m venv py_env

#using virtualenv
virtualenv py_env
```

---

<br>

* ### To activate the virtual environment

```python
"""LINUX"""
$ source py_env_3.8/bin/activate

"""WINDOWS"""
py_env_3.8\Scripts\activate.bat
```

---

<br>


```python
# To see all the packages installed in the current environment with their version numbers.
$ pip list

# pip freeze is similar to pip list but it generates o/p that is suitable for requirements file.
$ pip freeze > requirements.txt

#--local tells to only include packages in the current environment, rather than globally
$ pip freeze --local > requirements.txt
```

> It is advisable to use pip freeze over pip freeze --local to have complete list of packages.

---

* ### Install all the packages in a virtual env
  
```python
pip install -r requirements.txt
# -r stands for read
```

---

* ### To deactivate the virtual env

```python
deactivate
```
