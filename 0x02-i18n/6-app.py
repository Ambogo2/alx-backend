from flask import Flask, render_template, request, session
from flask_babel import Babel, _
from typing import Optional

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']
babel = Babel(app)

def get_user_locale() -> Optional[str]:
    return session.get('user_locale')

@babel.localeselector
def get_locale():
    
    locale = request.args.get('locale')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    
    user_locale = get_user_locale()
    if user_locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return user_locale

    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/')
def home():
    return render_template('6-index.html')

@app.route('/set_user_locale/<locale>')
def set_user_locale(locale):
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        session['user_locale'] = locale
    return f"User locale set to {locale}"

if __name__ == "__main__":
    app.run(debug=True)
