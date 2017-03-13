from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    error = None
    if request.method == 'POST':
        if(request.form['name'] != '' and request.form['age'] != '' and request.form['fav ninja'] != ''):
            name = request.form['name']
            age = request.form['age']
        else:
            error = 'Please fill out everything!'
    return render_template("result.html",name = name, age = age,error=error)

if __name__ == '__main__':
    app.run()
