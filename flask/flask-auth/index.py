from flask import Flask, render_template, request, redirect, url_for, flash,session
from mysql import connector

connect = connector.connect(host='localhost',user='root',password='',database='flask-auth' )
is_authenticated = False
app = Flask(__name__)
app.secret_key = 'flask-auth'


@app.route('/dashboard')
def dashboard():    
    if 'user_id' in session:
        is_authenticated = True
        return render_template('dashboard.html',is_authenticated=is_authenticated)
    else:
        flash('Please login first','danger')
        return redirect(url_for('login'))

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        # return request.form

        errors = False

        if not fname:
            flash('First name is required','danger') 
            errors = True

        if not email:
            flash('Email is required','danger') 
            errors = True

        if not password:
            flash('Password is required','danger') 
            errors = True

        if password != confirm_password:
            flash('Passwords should match.','danger')
            errors = True
        
        if errors:
            return redirect( url_for('signup'))

        db = connect.cursor()
        db.execute('INSERT INTO users (fname,lname,email,password) VALUES(%s,%s,%s,%s)',(fname,lname,email,password))
        connect.commit()
        db.close()

        flash('User registered successfully!','success')
        return redirect( url_for('signup'))
    else:
        return render_template('signup.html',is_authenticated=is_authenticated)
    
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html',is_authenticated=is_authenticated)
    else:
        email = request.form['email']
        password = request.form['password']
        
        errors = False
        
        if not email:
            flash('Please enter your Email address','danger')
            errors = True

        if not password:
            flash('Please enter valid password','danger')
            errors = True

        if errors:
            return redirect(url_for('login'))

        db = connect.cursor()
        db.execute('SELECT * FROM users WHERE email= %s AND password = %s',(email,password))
        # user = db.fetchone()
        user = db.fetchall()
        if len(user) == 0:
            flash('Please signup first','danger')
            return redirect(url_for('signup'))
        else:
            session['user_id'] = user[0][0]
            session['user_name'] = user[0][1]
            session['user_email'] = user[0][3]

            flash('login successfully!','success')
            return redirect(url_for('dashboard'))


        return request.form

@app.route('/quiz-app')
def quiz_app():
    if 'user_id' in session:
        is_authenticated = True
        return render_template('quiz_app.html',is_authenticated=is_authenticated)
    else:
        flash('Please login first','danger')
        return redirect(url_for('login'))

@app.route('/todo-app')
def todo_app():
    if 'user_id' in session:
        is_authenticated = True
        return render_template('todo_app.html',is_authenticated=is_authenticated)
    else:
        flash('Please login first','danger')
        return redirect(url_for('login'))

@app.route('/weather-app')
def weather_app():
    if 'user_id' in session :
        is_authenticated = True
        return render_template('weather_app.html',is_authenticated=is_authenticated)
    else:
        flash('Please login first','danger')
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session.pop('user_id',None)
    session.pop('user_name',None)
    session.pop('user_email',None)

    flash('logout successfully!','success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)