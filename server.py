from flask import Flask,render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    source = url_for('static', filename='img/tmnt.png')
    return render_template('ninja.html',image_source = source)

@app.route('/ninja/<color>')
def color_ninja(color):
    print color
    if(color == "blue"):
        source = url_for('static', filename='img/leonardo.jpg')
    elif(color == "orange"):
        source = url_for('static', filename='img/michelangelo.jpg')
    elif(color == "red"):
        source = url_for('static', filename='img/raphael.jpg')
    elif(color == "purple"):
        source = url_for('static', filename='img/donatello.jpg')
    else:
        source = url_for('static', filename='img/notapril.jpg')
    return render_template('ninja.html',image_source = source)

app.run(debug=True)