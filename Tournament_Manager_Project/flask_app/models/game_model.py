from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model, tournament_model, team_model
import re

class Game:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.venue = data['venue']
        self.game_date = data['game_date']
        self.game_time = data['game_time']
        self.winning_score = data['winning_score']
        self.losing_score = data['losing_score']
        self.team_home = data['team_home']
        self.team_away = data['team_away']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tournament_id = data['tournament_id']
        self.tournament_user_id = data['tournament_user_id']

    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO games (venue,game_date, game_time, winning_score, losing_score, team_home, team_away, tournament_id, tournament_user_id)
        VALUES (%(venue)s, %(game_date)s, %(game_time)s, %(winning_score)s, %(losing_score)s, %(team_home)s, %(team_away)s, %(tournament_id)s, %(tournament_user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    # need to create many to many 
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
