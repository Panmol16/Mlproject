from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home')
def after():
    return render_template('after.html')

if __name__ == "__main__":
    app.run(debug=True)