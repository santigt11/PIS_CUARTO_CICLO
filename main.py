from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def login():
    return render_template('login.html')

@app.route('/inicio')

def principal():
    return render_template('index.html')

@app.route('/metodo')
def metodo():
    metodoMatematico = ('EULER')
    return render_template('metodo.html',metodo=metodoMatematico)



if __name__ == '__main__':
    app.run(port=63343, debug=True)
