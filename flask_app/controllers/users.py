from flask import render_template, request, redirect
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User



@app.route("/users")
def users():
    mysql = connectToMySQL('users')
    users = mysql.query_db('SELECT * FROM users;')
    return render_template("index.html", all_users = users)


@app.route('/users/new')
def show():
    return render_template('index_new.html')

@app.route('/users', methods=['POST'])
def add_user():
    User.add(request.form)
    return redirect("/users")


@app.route('/users/show/<id>')
def show_user_page(id):
    data = {
        'id' : int(id)
    }
    return render_template('index_show.html', user = User.get_by_id(data))



@app.route('/users/edit/<id>')
def edit(id):
    data = {
        "id" : int(id)
    }
    return render_template('index_edit.html', user = User.get_by_id(data))

@app.route("/edit/<id>", methods=["POST"])
def update(id):
    data = {
        "first_name" : request.form['fname'],
        "last_name" : request.form['lname'],
        "email" : request.form['email'],
        "id" : int(id)
    }
    User.update(data)
    return redirect(f'/users/show/{id}')



@app.route('/delete/<id>')
def delete_user(id):
    data = {
        "id" : int(id)
    }
    User.delete(data)
    return redirect("/users")