# Development


## Required Packages

**Virtualenv**

**For Debian and Derivatives**
```bash
sudo su
apt install python3-venv
```

**For Fedora**

Virtual environment installed by default on Fedora

## Steps for running the project

**Get source code**
```bash
git clone https://github.com/kaganndemirr/kozmoz-project-backend.git (Use HTTPS)
git clone git@github.com:kaganndemirr/kozmoz-project-backend.git (Use SSH)
```

**Change directory**
```bash
cd kozmoz-project-backend
```

**Create virtualenv with python3**
```bash
python3 -m venv env
```

**Make active virtualenv**
```bash
source env/bin/activate
```

**Create required files**
```bash
touch kozmoz/settings/staging_production_secrets.py
```

Note: Please ask secret credentials from admin.

**Install requirements**
```bash
pip3 install -r requirements/staging.txt
```

**Create database**
```bash
./manage.py migrate
```

**Run project**
```bash
./manage.py runserver 0.0.0.0:8000 (http://127.0.0.1:8000)
```
