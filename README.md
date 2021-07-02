# GetYourStuff

# Setup the virtual env with below commands 
python -m venv env
source env/bin/activate

# Upgrade the pip with this command 
python -m pip install --upgrade pip

# Add a requiremnts.txt which contains all the needed packages or modules and then run the below command to install them in virtual env
pip install -r requirements.txt

# To install a specific package
pip install 'package name' 

# verify installed packages for the project 
pip freeze

# Setup env variables 

export FLASK_APP=appstart.py
export FLASK_DEBUG=1

# To debug with VSCode
Run->Add configuration --> Add below :

"env": {
                "FLASK_APP": "appstart.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--port",
                "2525"
            ]

# Run the flask app
flask run

# Run the flask app with host and port
flask run -h localhost -p 3000

app.run(debug=True).

# Choose the interpreter 
Set up virtual env and debug steps

# Heroku get started

Install the CLI -
brew tap heroku/brew && brew install heroku

Verify version -
heroku --version

Login command - 
heroku login
#heroku login -i 



# Azure webapp [https://medium.com/@nikovrdoljak/deploy-your-flask-app-on-azure-in-3-easy-steps-b2fe388a589e]
Create a web app
Now we can create web app or App Service. On portal left navigation bar click “App Services” and then “Add”. Select “Web App” and click “Create”:

Select appropriate pricing tier, but for demo purposes, Basic tier(B1) is the most suitable option.

Click “Deployment center”, and select "Git”: set the git repo

Go to “Application settings” and enter the following line in “Startup File” field:
gunicorn --bind=0.0.0.0 --timeout 600 appstart:app