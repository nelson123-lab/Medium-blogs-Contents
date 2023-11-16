This readme will be having all the commands mentioned in the **Setting up a Virtual Environment and GitHub Repo : A Step-by-Step Guide** Medium blog.

### To install virtualenv Python library
```python
pip install virtualenv
```

### To install any other packaga
```python
pip install package_name
```

### To create a virtual environment named "ML"
```python
virtualenv venv
```

### To view all the installed libraries in the location.
```python
pip list
```

### To activate the virtual environment.
```python
# These command should be used when the current directory is the virtual environment folder.
Scripts\activate
```

### To deactivate the virtual environment.
```python
# These command should be used when the virtual environment is active.
deactivate
```

### To clone a github repository.
```python
git clone github_url
```

### To create requirements.txt
```python
# This should be used when the repository is active.
pip freeze > requirements.txt
```

### To install all the packages from requirements.txt.
```python
# This command should be used when the current directory have the requirements.txt as file.
pip install -r requirements.txt
```
