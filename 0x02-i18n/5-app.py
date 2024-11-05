from flask import Flask, g, request, render_template, redirect, url_for
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Return a user dictionary or None if the ID is not found."""
    user_id = request.args.get("login_as")
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None

@app.before_request
def before_request():
    """Set a user for the session."""
    g.user = get_user()

@app.route('/')
def index():
    """Render the index page."""
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(debug=True)
