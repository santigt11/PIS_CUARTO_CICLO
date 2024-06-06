from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_euler(N0, M0, start_year, end_year):
    # Función que define la tasa de cambio
    def f(N, M):
        return -0.01 * N + 0.03 * M   # Función ajustada

    # Método de Euler
    N = N0
    M = M0
    t = 0
    T = end_year - start_year
    h = 0.1   # Paso de tiempo (aproximadamente 1 mes)

    N_values = [N]
    M_values = [M]
    time_values = [t]

    for i in range(int(T / h)):
        dN_dt = f(N, M)
        N += h * dN_dt
        M = N0 + M0 - N
        t += h
        N_values.append(N)
        M_values.append(M)
        time_values.append(t)

    estudiantes_desertados = M_values[-1]

    return {
        'N_values': N_values,
        'M_values': M_values,
        'time_values': time_values,
        'estudiantes_desertados': estudiantes_desertados
    }

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/inicio')
def principal():
    return render_template('index.html')

@app.route('/metodo')
def metodo():
    return render_template('metodo.html')

@app.route('/resultado', methods=['POST'])
def mostrar_resultado():
    # Obtener los datos del formulario
    N0 = int(request.form['N0'])
    M0 = int(request.form['M0'])
    start_year = int(request.form['start_year'])
    end_year = int(request.form['end_year'])

    # Calcular el método de Euler con los datos recibidos
    resultados_euler = calculate_euler(N0, M0, start_year, end_year)

    # Renderizar la plantilla de resultados con los resultados calculados
    return render_template('resultado.html', **resultados_euler)

if __name__ == '__main__':
    app.run(debug=True)
