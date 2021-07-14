import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
<<<<<<< HEAD
app.listen(process.env.PORT || 3000)
=======
app.set("port",'8080')
>>>>>>> 90fa5df9c0044ab3f0e9400a631177717e4b3d61

migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


from flask_login import login_required
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'