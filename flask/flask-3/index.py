from flask import Flask , render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = 'index'

@app.route('/home/')
def home():
    return 'home page'


# @app.route('/signup-form')
@app.route('/signup')
def signup():
    # return 'sign up page'
    # return render_template('signup.html')
    return render_template('forms/signup.html')

# submit form using POST
@app.route('/register',methods=['POST'])
# @app.route('/register',methods=['GET','POST'])
def register():    
   
    form_data = request.form
    return render_template('register.html',form_data=form_data)
    
    # return form_data
    # first_name = request.form['first_name']
    # last_name = request.form['last_name']
    # email = request.form['email']
    # password = request.form['password']
    # confirm_password = request.form['confirm_password']
    # return render_template('register.html',f_name=first_name, last_name=last_name,email=email,password=password,confirm_password=confirm_password )
    # return f"first Name: {first_name} <br> Last Name: {last_name} <br> Email : {email} <br> Password: {password} <br> Conform Password: {confirm_password}  "
    # return last_name
    return 'form is submitted'

# submit form using GET
@app.route('/register-get')
def register_get():
    form_data = request.args
    # form_data = request.args['first_name']
    # form_data = request.args.get('first_name')
    # return form_data
    return render_template('register.html',form_data=form_data)



@app.route('/signup-new')
def signup_new():
    return render_template('forms/signup-new.html')

@app.route('/register-new',methods=['POST'] )
def register_new():
    data = request.form

    

    first_name = request.form['first_name']
    email = request.form['email']
    password  = request.form['password']
    confirm_password = request.form['confirm_password']

    if request.files['image']:
        file = request.files['image']
        file_name = file.filename
        file.save('uploads/' + file_name)
    else:
        flash('Kindly upload you file ','error')


    if first_name and email and password and password == confirm_password:
        flash('Form is submitted successfully!','success')
    else:
        flash('Enter Valid informations','error')
        return redirect( url_for('signup_new') )

    # if first_name:
    #     return first_name
    # else:
    #     return 'Enter your first name'
    

    # if email:
    #     return email
    # else:
    #     return 'enter a valid email'

    return render_template('register_new.html', data=data )




if __name__ == "__main__":
    app.run(debug=True)