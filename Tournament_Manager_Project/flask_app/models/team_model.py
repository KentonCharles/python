from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model, tournament_model, game_model
import re

class Team:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.team_name = data['team_name']
        self.team_mascot = data['team_mascot']
        self.team_city = data['team_city']
        self.team_state = data['team_state']
        self.team_wins = data['team_wins']
        self.team_losses = data['team_losses']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO games (team_name, team_mascot, team_city, team_state, team_wins, team_losses)
        VALUES (%(team_name)s, %(team_mascot)s, %(team_city)s, %(team_state)s, %(team_wins)s, %(team_losses)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)