from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World! Home"

@app.route('/shop')
def shop():
    return "<h1>Shop page </h1>"


if __name__ == "__main__":
    
    # app.run(debug=True)
    app.run(port=7000)