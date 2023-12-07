from flask import Flask, redirect, url_for
application = Flask(__name__)


# create route
@application.route('/')
def domain():
    return 'Welcome !'

@application.route('/home/')
def home():
    return "Hello World!"

@application.route('/shop')
def shop():
    return 'Shop page'

# @application.route('/about/')
def about_function():
    return '<h1> About page </h1>'
application.add_url_rule('/about','about',about_function)

# pass variable through route
# @application.route('/product/<id>')

# pass variable of specific data type
@application.route('/product/<int:id>')
def product(id):
    return f'Product Page: {id}'

# redirect to differenct routes
@application.route('/goto/<key>')
def goto(key):

    if key == 'home':
        # return redirect('/home')
        return redirect( url_for('home'))
    elif(key == 'shop'):
        return redirect( url_for('shop') )
    elif(key == 'about'):
        return redirect( url_for( 'about_funciton')  )
    else:
        return f" {key} keyword not supported "



if __name__ == '__main__':
    # application.run()
    # application.run(port=7000)
    application.run(debug=True)


