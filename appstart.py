import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.set("port",'8080')

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


from flask_login import login_required
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'