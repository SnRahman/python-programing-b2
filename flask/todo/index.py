from flask import Flask, render_template , request , redirect , url_for , flash, session
from mysql import connector

app = Flask(__name__)

app.secret_key = 'todo'

connect = connector.connect(host='localhost',user='root',password='',database='flask-todo')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register',methods=['POST'])
def register():
    fname = request.form['fname'] 
    lname = request.form['lname'] 
    email = request.form['email'] 
    password = request.form['password'] 
    confirm_password = request.form['confirm_password'] 

    if fname and lname and email and password and confirm_password and password == confirm_password:

        db = connect.cursor()
        db.execute('INSERT INTO users (fname,lname,email,password) VALUES (%s,%s,%s,%s)',(fname,lname,email,password))
        connect.commit()
        db.close()
        flash('User Registered Successfully!','success')
        return redirect( url_for('login') )
    else:
        flash('All fields are required!','danger')
        return redirect(url_for('signup'))
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']

        if email and password:
            db = connect.cursor()
            db.execute('SELECT * FROM users WHERE email = %s AND password = %s ',(email,password))
            user = db.fetchone()

            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                session['email'] = user[3]

                flash('Login successfully!','success')
                return redirect(url_for('todo'))
            else:
                flash('No record found, signup first','danger')
                return redirect(url_for('signup'))

        else:
            flash('Enter Valid information','danger')
            return redirect(url_for('login'))
        return request.form


@app.route('/todo')
def todo():
    if 'username' in session:
        user_id = session.get('user_id',-1)

        db = connect.cursor()
        db.execute('SELECT * FROM todos WHERE user_id = %s',(user_id,))
        tasks = db.fetchall()
        db.close()

        return render_template('todo_app.html',tasks=tasks)
    else:
        flash('kindly login first','danger')
        return redirect(url_for('login'))


@app.route('/create-todo',methods=['POST'])
def create_todo():
    task = request.form['todo']

    if task:
        user_id = session.get('user_id',-1)
        db = connect.cursor()
        db.execute('INSERT INTO todos (task,user_id) VALUES (%s,%s)',(task,user_id))
        # db.execute(f'INSERT INTO todos (task) VALUES ({task})')
        connect.commit()
        db.close()

        flash('task addedd successfull!','success')
        return redirect(url_for('todo'))
    else:
        flash('Please enter any task','danger')
        return redirect(url_for('todo'))


@app.route('/delete-task/<id>')
def delete_task(id):
    db = connect.cursor()
    db.execute('DELETE FROM todos WHERE id = %s',(id,) )
    connect.commit()
    db.close()

    flash('Task deleted successfully!','success')
    return redirect(url_for('todo'))


@app.route('/logout')
def logout():
    session.pop('username',None)
    session.pop('email',None)
    session.pop('user_id',None)
    
    flash('Logout Successfully!','success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)