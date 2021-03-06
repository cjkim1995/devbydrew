import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('posts', __name__, url_prefix='/posts')




# Registering portion
@bp.route('/<username>', methods=('GET', 'POST'))

def index(username):
  db = get_db()
  posts = db.execute(
    'SELECT p.id, title, body, created, author_id, username'
    ' FROM post p JOIN user u ON p.author_id = u.id'
    ' ORDER BY created DESC'
  ).fetchall()
  return render_template('blog/userposts.html', posts=posts)


def get_post(id, check_author=True):
  post = get_db().execute(
    'SELECT p.id, title, body, created, author_id, username'
    ' FROM post p JOIN user u ON p.author_id = u.id'
    ' WHERE p.id = ?',
    (id,)
  ).fetchone()

  if post is None:
    abort(404, "Post id {0} doesn't exist.".format(id))

  if check_author and post['author_id'] != g.user['id']:
    abort(403)

  return post