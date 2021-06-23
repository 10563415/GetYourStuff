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

export FLASK_APP=flaskprojectstartpythonfile.py
export FLASK_DEBUG=1

# To debug with VSCode
Run->Add configuration --> Add below :

"env": {
                "FLASK_APP": "start.py",
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
