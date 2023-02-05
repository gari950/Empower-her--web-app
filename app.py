from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/breathe')
def breathe():
    return render_template('breathe.html')

@app.route('/clean')
def clean():
    return render_template('clean.html')

@app.route('/what')
def what():
    return render_template('what.html')

@app.route('/book')
def book():
    return render_template('book.html')
    
@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/task')
def task():
    return render_template('task.html')

@app.route('/ocd')
def ocd():
    return render_template('ocd.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/breath')  
def breath():
    return render_template('breath.html')

if __name__ == "__main__":
    app.run(debug=True)