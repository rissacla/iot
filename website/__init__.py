from flask import Flask
import os

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="enter secret key here",
    )
    upload_folder = os.path.join('website', 'static', 'uploads')
    app.config['UPLOAD_FOLDER'] = upload_folder

    # import blueprints
    from .dashboard import dashboard_bp
    from .preferences import preferences_bp
    from .settings import settings_bp

    app.register_blueprint(dashboard_bp,  url_prefix="/")
    app.register_blueprint(preferences_bp)
    app.register_blueprint(settings_bp)

    with app.app_context():
        pass

    return app
