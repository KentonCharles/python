from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key= "secrets secrets are no fun"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST']) #ACTION ROUTE (no render template here!)
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    session['office_fav'] = request.form['office_fav']
    return redirect('/results')

@app.route('/results')
def display_results():

    return render_template("result.html")

# @app.route('/form')
# def display_form():
#     return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)





