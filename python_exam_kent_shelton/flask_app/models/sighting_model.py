from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
import re

class Sighting:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.date = data['date']
        self.num_squatches = data['num_squatches']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # method for creating new sighting entry
    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO sightings (location,description,date,num_squatches,user_id)
        VALUES (%(location)s,%(description)s,%(date)s,%(num_squatches)s,%(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    # method for getting all sightings
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM sightings JOIN users ON sightings.user_id = users.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_sightings = []
        if results:
            for row in results:
                this_sighting = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                this_user = user_model.User(user_data)
                this_sighting.squatcher = this_user
                all_sightings.append(this_sighting)
        return all_sightings

    # method for getting one sighting w/ newly created attribute of "squatcher" through a join
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM sightings JOIN users ON sightings.user_id = users.id
        WHERE sightings.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            row = results[0]
            this_sighting = cls(row)
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            this_user = user_model.User(user_data)
            this_sighting.squatcher = this_user
            return this_sighting
        return False

    # method for updating/editing sighting entry
    @classmethod
    def update(cls,data):
        query = """
        UPDATE sightings SET location = %(location)s, description = %(description)s,
        date = %(date)s, 
        num_squatches = %(num_squatches)s
        WHERE sightings.id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    # method for deleting single sighting entry
    @classmethod
    def delete(cls,data):
        query = """
        DELETE FROM sightings WHERE id = %(id)s
        """
        return connectToMySQL(DATABASE).query_db(query,data)


    # validation method for new sighting entry
    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['location']) < 1:
            flash("location required")
            is_valid = False
        if len(form_data['description']) < 1:
            flash("what happened required")
            is_valid = False
        if len(form_data['date']) < 1:
            flash("date required")
            is_valid = False
        if len(form_data['num_squatches']) < 1:
            flash("at least 1 Sasquatch required")
            is_valid = False
        return is_valid
        


