from flask import Flask

''''create Flask app instance'''
app = Flask(__name__)


@app.route('/')
def home():
    return " Hare Krishna Hare Krishna Krishna Krishna Hare Hare, Hare Rama Hare Rama Rama Rama Hare Hare"

@app.route('/about')
def about():
    return "This is a simple Flask web application."    



if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode for development purposes 