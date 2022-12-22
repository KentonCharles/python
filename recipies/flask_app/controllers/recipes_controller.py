from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

# route to add new recipe form
@app.route('/recipes/new')
def new_recipe_form():
    return render_template('recipes_new.html')

# action route for processing new recipe w/ redirect to main dashboard
@app.route('/recipe/create', methods=['POST'])
def create_recipe():
    # check for user login
    if "user_id" not in session:
        return redirect('/')
    # check for validation
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    recipe_data = {
        **request.form,
        'user_id': session['user_id']
    }
    Recipe.create(recipe_data)
    return redirect('/dashboard')

# route for displaying details for single recipe
@app.route('/recipes/<int:id>/view')
def get_one_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id': id
    }
    one_recipe = Recipe.get_one(data)
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template('recipes_one.html', one_recipe=one_recipe, logged_user=logged_user)

# route for displaying edit form
@app.route('/recipes/<int:id>/edit')
def edit_recipe_form(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id': id
    }
    one_recipe = Recipe.get_one(data)
    return render_template('recipes_edit.html', one_recipe=one_recipe)

# action route for processing recipe edits
@app.route('/recipes/<int:id>/update', methods =['POST'])
def update_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect(f'/recipes/{id}/edit')
    update_data = {
        **request.form,
        'id':id
    }
    Recipe.update(update_data)
    return redirect('/dashboard')

# route to delete recipe(get request)
@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id': id
    }
    Recipe.delete(data)
    return redirect('/dashboard')