from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def login():
    return render_template('login.html')

@app.route('/principal')

def principal():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(port=63343, debug=True)
