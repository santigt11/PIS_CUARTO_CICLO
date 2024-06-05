function calculateEuler() {
    // Obtener valores iniciales desde el HTML
    let N0 = parseFloat(document.getElementById("initialEnrolled").value);  // Número inicial de estudiantes matriculados
    let M0 = parseFloat(document.getElementById("initialUnenrolled").value);  // Número inicial de estudiantes no matriculados
    let startYear = parseInt(document.getElementById("startYear").value);
    let endYear = parseInt(document.getElementById("endYear").value);
    let T = endYear - startYear;  // Período de predicción (años)
    let h = 0.1;   // Paso de tiempo (aproximadamente 1 mes)

    // Función que define la tasa de cambio
    function f(N, M) {
        return -0.01 * N + 0.03 * M;   // Función ajustada
    }

    // Método de Euler
    let N = N0;
    let M = M0;
    let t = 0;
    let time_steps = Math.ceil(T / h);  // Número de pasos de tiempo

    // Almacenar los resultados
    let N_values = [N];
    let M_values = [M];
    let time_values = [t];

    for (let i = 0; i < time_steps; i++) {
        let dN_dt = f(N, M);
        N = N + h * dN_dt;
        M = N0 + M0 - N;  // Asegurando que N + M = N0 + M0
        t = t + h;
        N_values.push(N);
        M_values.push(M);
        time_values.push(t);
    }

    // Obtener el número final de estudiantes desertados
    let estudiantes_desertados = M_values[M_values.length - 1];

    // Crear el mensaje de resultados
    let output = "Hola,\n\n";
    output += `Para el período de ${startYear} a ${endYear}:\n`;
    output += `Estudiantes matriculados inicialmente: ${N0}\n`;
    output += `Estudiantes no matriculados inicialmente: ${M0}\n`;
    output += "---------------------------------------------\n";
    output += "Tiempo (años)\tEstudiantes matriculados\tEstudiantes que desertaron\n";
    for (let i = 0; i < time_values.length; i++) {
        output += `${time_values[i].toFixed(2)}\t\t${N_values[i].toFixed(2)}\t\t\t${M_values[i].toFixed(2)}\n`;
    }
    output += `\nNúmero final de estudiantes desertados: ${estudiantes_desertados.toFixed(2)}`;

    // Mostrar los resultados en el HTML
    document.getElementById("resultBox").value = output;
}
