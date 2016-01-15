from flask import Flask
from flask.ext.babel import Babel

babel = Babel()

def create_app():
    ''' Create the Flask app.
    '''
    # Create the Flask app.
    app = Flask(__name__)

    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        # 'sr' for Serbian and 'sq' for Albanian.
        lang_code = 'sq'
        return lang_code

     # Import a module / component using its blueprint handler variable 
    from app.mod_test.views import mod_test

    # Register blueprint(s)
    app.register_blueprint(mod_test)

    return app