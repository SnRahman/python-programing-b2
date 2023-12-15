from flask import Flask, render_template, request, redirect, url_for, flash
from mysql import connector

app = Flask(__name__)

app.secret_key = 'db connection'
connection = connector.connect(host='localhost',user='root',password='',database='flask-3')


@app.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('forms/login.html')
    else:
        # return request.form
        email = request.form['email']
        password = request.form['password']

        db = connection.cursor()
        db.execute('SELECT * FROM users WHERE email = %s and password = %s',(email, password))
        user = db.fetchall()
        db.close()
        if len(user) > 0:
            flash('user login successfull!','success')
            return redirect(url_for('users'))
        else:
            flash('Invalid credentials','error')
            return redirect(url_for('login'))


@app.route('/users')
def users():
    db = connection.cursor()
    db.execute('SELECT * FROM users')
    users = db.fetchall()
    db.close()
    return render_template('users.html',users=users )

@app.route('/signup')
def signup():
    return render_template('forms/signup-new.html')


@app.route('/register',methods = ['POST'] )
def register():
    # form_data = request.form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if first_name and last_name and email and password and confirm_password and password== confirm_password:
        # insert into data base 
        db = connection.cursor()
        db.execute('INSERT INTO users (first_name,last_name,email,password) VALUES (%s,%s,%s,%s)',(first_name,last_name,email,password))
        
        connection.commit()

        db.close()
        flash('User is added Successfully!','success')
        return redirect( url_for('users') )
    else:
        flash('Something went wrong with your information','error')
        return redirect(url_for('signup'))
        # return "All fields are not complete"


@app.route('/edit-user/<id>')
def edit_user(id):
    db = connection.cursor()
    db.execute(f'SELECT id, first_name, last_name, email FROM users WHERE id = {id}')
    user = db.fetchall()
    # return user[0][2]
    return render_template('forms/update-form.html',user= user)
    # return f'updating user: {id}'

@app.route('/update-user/<id>', methods=['POST'])
def update_user(id):
    data = request.form
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']

    if first_name and last_name and email:
        db = connection.cursor()
        db.execute('UPDATE users SET first_name = %s , last_name = %s, email = %s WHERE id = %s',(first_name,last_name,email,id))        
        connection.commit()
        db.close()

        flash('User Record updated Successfully!','success')
        return redirect(url_for("users"))
        # return 'user data updated'
    else:
        flash('Something went wrong with your information','error')
        return redirect(url_for('edit_user',id=id))



@app.route('/delete-user/<id>')
def delete_user(id):
    
    # return f'delete user {id}'   
    db = connection.cursor()
    db.execute('DELETE FROM users WHERE id = (%s)',(id,))
    connection.commit()
    db.close()
    flash('user deleted Successfully!','success')
    return redirect( url_for('users') )

    # return form_data


if __name__ == '__main__':
    app.run(debug=True)