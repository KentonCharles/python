from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secrets secrets are no fun"
# our index route will handle rendering our form
@app.route('/')
def welcome():
    return "Howdy!"

@app.route('/form')
def display_form():
    if "count_track" in session:
        session["count_track"] += 1
    else:
        session["count_track"] = 1
    return render_template("index.html", count = session["count_track"])

# @app.route('/process', methods= ['POST']) #ACTION
# def add_count():
#     print(request.form)
#     session['count_track'] = request.form['count_track'] + 1
#     return redirect('/count')

# @app.route('/count')#DISPLAY
# def display_click():
#     return render_template("counter.html", count = session["count_track"])

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/form')


if __name__ == "__main__":
    app.run(debug=True)

