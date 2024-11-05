from flask import Flask, render_template, request
from flask_babel import Babel

app =Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    # This function can be enhanced to infer locale from request
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('1-index.html', title="Welcome to Holberton")

if __name__ == '__main__':
    app.run(debug=True)