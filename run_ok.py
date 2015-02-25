from flask import Flask
from flask.ext.babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale():
    lang_code = 'fr'
    print "Get locale '%s'" % lang_code
    return lang_code

@app.route('/')
def hello():
	message = gettext(u'Hello')
	return message

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)