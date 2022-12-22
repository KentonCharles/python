from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model
import re

class Tournament:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.tournament_name = data['tournament_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # method for creating new recipe entry
    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO tournaments (tournament_name,user_id)
        VALUES (%(tournament_name)s, %(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    # method for getting all recipes
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM tournaments JOIN users ON tournaments.user_id = users.id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_tournaments = []
        if results:
            for row in results:
                this_tournament = cls(row)
                user_data = {
                    **row,
                    'id': row['users.id'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                this_user = user_model.User(user_data)
                this_tournament.organizer = this_user
                all_tournaments.append(this_tournament)
        return all_tournaments

    # method for getting one recipe w/ newly created attribute of "cook" through a join
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM tournaments JOIN users ON tournaments.user_id = users.id
        WHERE tournaments.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            row = results[0]
            this_tournament = cls(row)
            user_data = {
                **row,
                'id': row['users.id'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            this_user = user_model.User(user_data)
            this_tournament.organizer = this_user
            return this_tournament
        return False

    # method for updating/editing recipe entry
    @classmethod
    def update(cls,data):
        query = """
        UPDATE tournaments SET tournament_name = %(tournament_name)s
        WHERE tournaments.id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    # method for deleting single recipe entry
    @classmethod
    def delete(cls,data):
        query = """
        DELETE FROM tournaments WHERE id = %(id)s
        """
        return connectToMySQL(DATABASE).query_db(query,data)