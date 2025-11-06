from flask import Flask,render_template,request

''''create Flask app instance'''
app = Flask(__name__)


@app.route('/')
def home():
    return " Hare Krishna Hare Krishna Krishna Krishna Hare Hare, Hare Rama Hare Rama Rama Rama Hare Hare"



@app.route('/about')
def about():
    return render_template("about.html")  # Render the about.html template


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')  # match HTML field name
        email = request.form.get('email')
        password = request.form.get('password')
        return f"Thank you for signing up, {username}! <br> Your email is {email}."
    return render_template("signup.html")




if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode for development purposes 