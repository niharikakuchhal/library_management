from app import create_app
from flask_migrate import Migrate
from app.routes import main

app = create_app()
# migrate = Migrate(app, db)
# app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
