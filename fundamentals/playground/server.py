from flask import Flask, render_template  
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")  

@app.route('/play')
def playground1():
    return render_template("playground_play.html")

@app.route('/play/<int:boxes>')
def playgrounder(boxes):
    return render_template("playground_play_x.html", boxes = boxes)

@app.route('/play/<int:boxes>/<color>')
def playgroundest(boxes,color):
    return render_template("playground_play_x_color.html", boxes = boxes, color = color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
