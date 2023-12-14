from flask import Flask, render_template, request, redirect, url_for, flash
from mysql import connector

app = Flask(__name__)

app.secret_key = 'db connection'
connection = connector.connect(host='localhost',user='root',password='',database='flask-3')


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
        return "All fields are not complete"

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