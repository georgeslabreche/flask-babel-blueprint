# Flask-Babel Sample App
A simple sample app to showcase how to setup the Flask-Babel plugin.

Getting Started
===============
1. Install
`bash install.sh`

2. Run application
`bash run.sh`


Translations
============
Translations are already set and compiled, this was initialized like so: `bash babel-init.sh`

In case you want to redo it yourself or add more text to translate:

1. In Jinja2 template files:
`{{ _('Hello') }}`

2. In Python files use Babel's gettext function: 

 `from flask.ext.babel import gettext`
 `gettext('Hello')`

3. Update translation files: `bash babel-update.sh`

4. Set Albanian translations in .po file: `translations/sq/LC_MESSAGES/messages.po`

4. Set Serbian translations in .po file: `translations/sr/LC_MESSAGES/messages.po`

5. Compile translations: `bash babel-compile.sh`

6. Set locale to use in `app/__init__.py` (hardcoded in this example project).

7. Run the app.

8. You will either see 'Përshëndetje' or 'Здраво' depending on which locale you set in `app/__init__.py` (sq for Albanian or sr for Serbian).




