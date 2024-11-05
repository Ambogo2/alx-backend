from flask import Flask, render_template, request, session
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']
babel = Babel(app)

def get_user_timezone() -> str:

    return session.get('user_timezone')

@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    user_locale = session.get('user_locale')
    if user_locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return user_locale
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@babel.timezoneselector
def get_timezone():
 
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
  
    user_timezone = get_user_timezone()
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except UnknownTimeZoneError:
            pass

    return 'UTC'

@app.route('/')
def home():
    return render_template('7-index.html')

@app.route('/set_user_timezone/<timezone>')
def set_user_timezone(timezone):
    try:
        pytz.timezone(timezone)
        session['user_timezone'] = timezone
        return f"User timezone set to {timezone}"
    except UnknownTimeZoneError:
        return "Invalid timezone", 400

if __name__ == "__main__":
    app.run(debug=True)
