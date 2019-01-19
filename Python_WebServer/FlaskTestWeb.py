from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<h1>Home page, Web server!<h1>'


@app.route('/about')
def about():
    return "<h1>This is an about page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
