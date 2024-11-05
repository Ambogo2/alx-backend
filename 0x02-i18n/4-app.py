from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']  # Supported locales
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Check if 'locale' is in the URL parameters and is a supported locale
    locale = request.args.get('locale')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    # Fallback to the best match if 'locale' is not in parameters or not supported
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/')
def home():
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run(debug=True)
