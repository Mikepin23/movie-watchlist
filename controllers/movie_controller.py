from flask import jsonify, render_template, request, flash, redirect, url_for
from flask_login import current_user
from forms.movie_forms import AddMovieForm
from models.movie import Movie
from extensions import db
import datetime

def require_login(message):
    if not current_user.is_authenticated:
        flash(message, 'warning')
        return redirect(url_for('auth.login'))
    return None

def handle_list_movies():
    login_redirect = require_login('Please log in to view your watchlist.')
    if login_redirect:
        return login_redirect

    watched_movies = Movie.query.filter_by(user_id=current_user.id, watched=True).all()
    unwatched_movies = Movie.query.filter_by(user_id=current_user.id, watched=False).all()
    form = AddMovieForm()
    return render_template('watchlist.html', watched_movies=watched_movies, unwatched_movies=unwatched_movies, form=form)


def handle_add_movie():
    login_redirect = require_login('Please log in to add movies to your watchlist.')
    if login_redirect:
        return login_redirect

    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        new_movie = Movie(title=title, user_id=current_user.id, date_added=datetime.datetime.now())
        db.session.add(new_movie)
        db.session.commit()
        flash(f'Movie "{title}" added to your watchlist!', 'success')
    else:
        flash('Movie title cannot be empty.', 'danger')

    return redirect(url_for('movie.watchlist'))


def handle_delete_movie(movie_id):
    login_redirect = require_login('Please log in to modify your watchlist.')
    if login_redirect:
        return login_redirect

    form_movie_id = request.form.get('movie_id')
    movie = Movie.query.filter_by(id=form_movie_id or movie_id, user_id=current_user.id).first()
    if movie:
        db.session.delete(movie)
        db.session.commit()
        flash(f'Movie "{movie.title}" removed from your watchlist!', 'success')
    else:
        flash('Movie not found or you do not have permission to delete it.', 'danger')

    return redirect(url_for('movie.watchlist'))


def handle_toggle_watched(movie_id):
    login_redirect = require_login('Please log in to modify your watchlist.')
    if login_redirect:
        return login_redirect

    movie = Movie.query.filter_by(id=movie_id, user_id=current_user.id).first()
    if movie:
        movie.watched = not movie.watched
        if movie.watched:
            import datetime
            movie.date_watched = datetime.datetime.now()
        else:
            movie.date_watched = None
        db.session.commit()
        status = 'watched' if movie.watched else 'unwatched'
        flash(f'Movie "{movie.title}" marked as {status}.', 'success')
    else:
        flash('Movie not found.', 'danger')
    return redirect(url_for('movie.watchlist'))