from flask import Blueprint
from controllers.movie_controller import handle_list_movies, handle_add_movie, handle_delete_movie, handle_toggle_watched

movie_bp = Blueprint('movie', __name__)

@movie_bp.route('/watchlist')
def watchlist():
	return handle_list_movies()

@movie_bp.route('/watchlist/add', methods=['POST'])
def add_movie():
	return handle_add_movie()

@movie_bp.route('/watchlist/delete/<movie_id>', methods=['POST'])
def delete_movie(movie_id):
	return handle_delete_movie(movie_id)

@movie_bp.route('/watchlist/toggle/<movie_id>', methods=['POST'])
def toggle_watched(movie_id):
	return handle_toggle_watched(movie_id)