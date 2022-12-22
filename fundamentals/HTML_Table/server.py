from flask import Flask, render_template 
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'

@app.route('/list')
def table_list():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("list.html", table_list = users)


if __name__=="__main__":   
    app.run(debug=True)    

