from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buttons')
def buttons():
    return render_template('buttons.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/forgot-password')
def password():
    return render_template('forgot-password.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/tables')
def tablas():
    return render_template('tables.html')

@app.route('/utilities-color')
def colores():
    return render_template('utilities-color.html')

@app.route('/utilities-border')
def bordes():
    return render_template('utilities-border.html')

if __name__ == '__main__':
    app.run(port=63343, debug=True)
