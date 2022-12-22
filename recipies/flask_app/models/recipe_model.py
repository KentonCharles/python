from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
import re

class Recipe:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under30 = data['under30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # method for creating new recipe entry
    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO recipies (name,description,instructions,date,under30,user_id)
        VALUES (%(name)s,%(description)s,%(instructions)s,%(date)s,%(under30)s,%(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    # method for getting all recipes
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM recipies JOIN users ON recipies.user_id = users.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        if results:
            for row in results:
                this_recipe = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                this_user = user_model.User(user_data)
                this_recipe.cook = this_user
                all_recipes.append(this_recipe)
        return all_recipes

    # method for getting one recipe w/ newly created attribute of "cook" through a join
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM recipies JOIN users ON recipies.user_id = users.id
        WHERE recipies.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            row = results[0]
            this_recipe = cls(row)
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            this_user = user_model.User(user_data)
            this_recipe.cook = this_user
            return this_recipe
        return False

    # method for updating/editing recipe entry
    @classmethod
    def update(cls,data):
        query = """
        UPDATE recipies SET name = %(name)s, description = %(description)s,
        instructions = %(instructions)s, date = %(date)s, 
        under30 = %(under30)s
        WHERE recipies.id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    # method for deleting single recipe entry
    @classmethod
    def delete(cls,data):
        query = """
        DELETE FROM recipies WHERE id = %(id)s
        """
        return connectToMySQL(DATABASE).query_db(query,data)


    # validation method for new recipe entry
    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['name']) < 3:
            flash("name must be at least 3 characters")
            is_valid = False
        if len(form_data['description']) < 3:
            flash("description required")
            is_valid = False
        if len(form_data['instructions']) < 3:
            flash("instructions required")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("date required")
            is_valid = False
        if "under30" not in form_data:
            flash("under 30 required")
            is_valid = False
        return is_valid
        


