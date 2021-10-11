import os
from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import User, Role


#THis is the factory function used for lazy initialization of the application
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


from flask_login import login_required
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


#Executed during deployment- DB migrations get applied
@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

    # create or update user roles
    Role.insert_roles()
    
