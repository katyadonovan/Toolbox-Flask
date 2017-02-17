"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, url_for, render_template
app = Flask(__name__)

#app.run(debug=True)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html',name=name)
"""@app.route('/')
def index(): pass

@app.route('/login')
def profile(login): pass

@app.route('/user/<username')
def profile(username): pass

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile',username='John Doe')"""

if __name__ == '__main__':
    app.run()
