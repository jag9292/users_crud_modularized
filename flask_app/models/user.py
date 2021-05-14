from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @classmethod
    def add(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(email)s);"
        
        return connectToMySQL('users').query_db(query, data)


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users').query_db(query,data)
        return cls(results[0])


    @classmethod
    def edit(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL('users').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        
        return connectToMySQL('users').query_db(query, data)


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL('users').query_db(query,data)