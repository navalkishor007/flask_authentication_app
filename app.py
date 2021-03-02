from flask import Flask, render_template,request,session,redirect
import os
import psycopg2

app = Flask(__name__)
app.secret_key= os.urandom(24)

conn = psycopg2.connect(database = "users", user = "postgres", password = "naval", host = "127.0.0.1", port = "5432")
cursor = conn.cursor()

# cursor.execute("CREATE TABLE Student_Infom (ID SERIAL PRIMARY KEY, name text);")
# conn.commit()
# cursor.close()
# conn.close()

print("Table created successfully")
        
@app.route('/')
def index():
   name = "naval"
   return render_template("base.html", name=name)

@app.route('/login')
def login_view():
   return render_template('login.html')

@app.route('/register')
def register_view():
    return render_template('register.html')

@app.route('/login_validation', methods=['post'])
def login_validation():
   email = request.form.get('email')
   password = request.form.get('password')
   cursor.execute("SELECT * FROM student WHERE email LIKE '{}' AND password LIKE '{}';".format(email,password))
   data = cursor.fetchall()
   print(data)
   if data:
      session['std_id'] = data[0][0]
      return render_template('base.html',name = email)
   else:
      return render_template('login_fail.html')

@app.route('/register_validation', methods=['post'])
def register_validation():   
   cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s);",
      (  request.form.get('std_id'),
         request.form.get('name'),
         request.form.get('email'),
         request.form.get('password')),
      )
   conn.commit()
   return redirect('/')

@app.route('/register_users')
def register_users():
   if 'std_id' in session:
      cursor.execute("SELECT * From student")
      result = cursor.fetchall()
      print(result)
      return render_template("users.html",data = result)
   else:
      return redirect('/login')

@app.route('/logout')
def logout_view():
   session.pop('std_id')
   return redirect('/')

@app.route('/delete/<int:std_id>', methods=['get','post'])
def delete_view(std_id):
   print(std_id)
   cursor.execute("DELETE FROM student WHERE stu_id=%s;",(std_id,))
   conn.commit()
   print('record deleted')
   return redirect('/')

if __name__ == '__main__':
   app.run(debug = True)