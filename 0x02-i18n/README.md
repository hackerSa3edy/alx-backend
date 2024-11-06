# Project: 0x02. i18n

## Description

This directory contains projects focused on internationalization (i18n) in Flask applications using Flask-Babel. The projects cover locale management, template parametrization, timezone handling and other i18n concepts.

## Resources

### Read or watch

* [Flask-Babel](https://flask-babel.tkte.ch/)
* [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
* [pytz](https://pythonhosted.org/pytz/)

## Tasks

| Task                                | File                                                                          | Description                                                    |
|------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------|
| 0. Basic Flask app                 | [0-app.py](./0-app.py)                                                       | Sets up a basic Flask app with a single route and template     |
| 1. Basic Babel setup               | [1-app.py](./1-app.py)                                                       | Adds Flask-Babel configuration to the app                      |
| 2. Get locale from request         | [2-app.py](./2-app.py)                                                       | Implements locale detection from request headers               |
| 3. Parametrize templates           | [3-app.py](./3-app.py)                                                       | Adds support for parametrized translations in templates        |
| 4. Force locale with URL parameter | [4-app.py](./4-app.py)                                                       | Allows forcing locale via URL parameters                       |
| 5. Mock logging in                 | [5-app.py](./5-app.py)                                                       | Implements mock user login system with i18n support           |
| 6. Use user locale                 | [6-app.py](./6-app.py)                                                       | Uses user's preferred locale for translations                  |
| 7. Infer appropriate time zone     | [7-app.py](./7-app.py)                                                       | Adds timezone detection and handling                          |
| 8. Display the current time        | [app.py](./app.py)                                                           | Shows current time based on user's timezone and locale        |
