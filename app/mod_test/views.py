# Import flask dependencies
from flask import Blueprint
from flask.ext.babel import Babel, gettext
from app import babel

# Define the blueprint:
mod_test = Blueprint('test', __name__)

@mod_test.route('/', methods=['GET'])
def hello():
	message = gettext(u'Hello')
	return message

@mod_test.route('/bye', methods=['GET'])
def bye():
	message = gettext(u'Goodbye')
	return message
