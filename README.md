# Flask-Babel
Can't get it to work...

Getting Started
===============
1. Install
`bash install.sh`

2. Run application using Blueprint and a function to create the Flask App (Doesn't work).
`bash run_nok.sh`

3. Run application that doesn't use Blueprint nor a function to create the Flask App (Works).
`bash run_ok.sh`

Translations
============
Translations are already set and compiled.
In case you want to redo it yourself or add more text to translate:

1. In Jinja2
`{{ _('Hello') }}`

2. In Python
 Use Babel's gettext: 

 `from flask.ext.babel import gettext`
 `gettext('Hello')`

3. Update translation files: `bash babel-update.sh`

4. Set translations in french .po file: `translations/fr/LC_MESSAGES/messages.po`

5. Compile translations: `bash babel-compile.sh`

6. Should see 'Bonjour' instead of 'Hello'. Doesn't work when Flask App is created using a function (and with Blueprint).

Note
====
Getting the locale to translate to has been hardcoded to french  (i.e. "fr").
The get_locales function fires as expected but translation doesn't actually occur.
See \_\_init\_\_.py:

`@babel.localeselector`
`def get_locale():`
  `return 'fr'`

We should be seeing "Bonjour" instead of "Hello".



