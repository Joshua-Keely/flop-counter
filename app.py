from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    session['counter'] += 1
    return redirect(url_for('index'))

@app.route('/subtract', methods=['POST'])
def subtract():
    session['counter'] -= 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)