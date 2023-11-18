This readme will be having all the commands mentioned in the **Setting up a Virtual Environment and GitHub Repo : A Step-by-Step Guide** Medium blog.

### To install virtualenv Python library
```python
pip install virtualenv
```

### To install any other packaga
```python
pip install package_name
```

### To list all the install packages
```python
pip list
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

### To initialize a git repository
```python
git init
```

### To add a new remote repository reference to your local Git repository.
```python
git remote add origin <remote_repository_url>
```

### To list the branches available in the remote repository.
```python
git ls-remote --heads origin
```

### To fetch the latest changes from the remote repository
```python
git fetch origin
```

### To create a new local branch named "main" that tracks the remote "main" branch and switch to it.
```python
git checkout main
```

### To create a new local branch named "main" that tracks the remote "main" branch.
```python
git checkout -b main origin/main
```

### To push the commited changes from local Git repository to the remote Git repository.
```python
git push
```

### To push the commits from your local "master" branch to the remote repository called "origin."
```python
git push -u origin master
```
