from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    with open('value.txt', 'r') as f:
        counter = f.read()
    return render_template('index.html', counter=counter)

@app.route('/add', methods=['POST'])
def add():
    session['counter'] += 1
    with open('value.txt', 'w') as f:
        f.write(str(session['counter']))
    return redirect(url_for('index'))

@app.route('/subtract', methods=['POST'])
def subtract():
    session['counter'] -= 1
    with open('value.txt', 'w') as f:
        f.write(str(session['counter']))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)