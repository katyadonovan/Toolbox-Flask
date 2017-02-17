from flask import Flask, render_template, request, redirect
app = Flask(__name__)
"""
@app.route('/')
def hello_world():
    author ="Me"
    name = "You"
    return 'Hello World!"""

@app.rout('/signup', methods = ['POST'])
def signup():
    name=request.form['name']
    age = request.form['age']
    print("Hello'"+ name +"'")
    return redirect('/')

if __name__ == '__main__':
    app.run()
