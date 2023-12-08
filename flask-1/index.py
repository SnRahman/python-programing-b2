from flask import Flask , redirect ,url_for, render_template

app = Flask(__name__) 


# return an html page
@app.route('/html')
def html():
    return render_template('html.html')
    # return 'this is html page.'

@app.route('/home/')
def home():
    return render_template('home.html')
    return 'this is home page.'


@app.route('/')
def index():
    return '<a href="/home">Home</a> <a href="/html">Html</a> <a href="/">Index page</a> <h1> this is index page. </h1>'
    # return 'this is index page.'

# pass variable through route
@app.route('/product/<id>')
def product(id):
    # return 'this is product page.'
    return f'this is product page. product id is: {id}'

# pass variable of specific data type
@app.route('/details/<int:id>')
def details(id):
    return f'this is Details page. product id is: {id}'

@app.route('/google')
def google():
    return redirect('https://www.google.com')

@app.route('/redirect')
def app_redirect():
    return redirect( url_for('product',id= 28) )
    # return redirect('prodcut/10')
    # return url_for('html')
    # return url_for('product',id=10)




if __name__ == '__main__':
    # app.run()
    # app.run(port=8080)
    app.run(debug=True)