from flask import Flask, render_template
app = Flask(__name__)                     

@app.route('/')                           
def index():
    return render_template('checkerboard.html', row = 8, col = 8)

@app.route('/<y>')                           
def rows(y):
    return render_template('checkerboard.html', row = 8, col = int(y))

@app.route('/<x>/<y>')                           
def rowsCol(x, y):
    return render_template('checkerboard.html', row = int(x), col = int(y))

if __name__=="__main__":
    app.run(debug=True)  