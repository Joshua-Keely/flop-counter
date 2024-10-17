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
    with open('value.txt', 'r') as f:
        counter = int(f.read())
    counter += 1
    with open('value.txt', 'w') as f:
        f.write(str(counter))
    return str(counter)


@app.route('/subtract', methods=['POST'])
def subtract():
    with open('value.txt', 'r') as f:
        counter = int(f.read())
    counter -= 1
    with open('value.txt', 'w') as f:
        f.write(str(counter))
    return str(counter)


@app.route('/get_counter', methods=['GET'])
def get_counter():
    with open('value.txt', 'r') as f:
        counter = f.read()
    return counter


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
