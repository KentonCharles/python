from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.sighting_model import Sighting

# route to add new sighting form
@app.route('/sightings/new')
def new_sighting_form():
    logged_user=User.get_by_id({'id':session['user_id']})
    return render_template('sightings_new.html', logged_user=logged_user)

# action route for processing new sighting w/ redirect to main dashboard
@app.route('/sighting/create', methods=['POST'])
def create_sighting():
    # check for user login
    if "user_id" not in session:
        return redirect('/')
    # check for validation
    if not Sighting.validator(request.form):
        return redirect('/sightings/new')
    sighting_data = {
        **request.form,
        'user_id': session['user_id']
    }
    Sighting.create(sighting_data)
    return redirect('/dashboard')

# route for displaying details for single sighting
@app.route('/sightings/<int:id>/view')
def get_one_sighting(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id': id
    }
    one_sighting = Sighting.get_one(data)
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template('sightings_one.html', one_sighting=one_sighting, logged_user=logged_user)

# route for displaying edit form
@app.route('/sightings/<int:id>/edit')
def edit_sighting_form(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id': id
    }
    one_sighting = Sighting.get_one(data)
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template('sightings_edit.html', one_sighting=one_sighting, logged_user=logged_user)

# action route for processing sighting edits
@app.route('/sightings/<int:id>/update', methods =['POST'])
def update_sighting(id):
    if "user_id" not in session:
        return redirect('/')
    if not Sighting.validator(request.form):
        return redirect(f'/sightings/{id}/edit')
    update_data = {
        **request.form,
        'id':id
    }
    Sighting.update(update_data)
    return redirect('/dashboard')

# route to delete sighting(get request)
@app.route('/sightings/<int:id>/delete')
def delete_sighting(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id': id
    }
    Sighting.delete(data)
    return redirect('/dashboard')