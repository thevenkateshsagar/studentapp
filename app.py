from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Config
app.config['MYSQL_HOST'] = 'mysql'   # service name
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Welcome@123'
app.config['MYSQL_DB'] = 'studentdb'


mysql = MySQL(app)

# Home - List Students


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', students=data)

# Add Student


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)", (name, email, course))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('add.html')

# Edit Student


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cur.fetchone()
    cur.close()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE students SET name=%s, email=%s, course=%s WHERE id=%s",
                    (name, email, course, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

    return render_template('edit.html', student=student)

# Delete Student


@app.route('/delete/<int:id>', methods=['GET'])
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
