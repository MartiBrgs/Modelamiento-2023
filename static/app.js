function sendFormLehmer() {
    console.log("Enviando formulario...");

    // Limpiar mensajes de error anteriores
    document.getElementById('errorContainer').style.display = 'none';
    document.getElementById('results').style.display = 'none';

    // Obtener los valores de los campos de entrada
    const x0 = document.getElementById('x0').value;
    const k = document.getElementById('k').value;
    const g = document.getElementById('g').value;
    const c = document.getElementById('c').value;

    // Construir el cuerpo de la solicitud
    const formData = new FormData();
    formData.append('x0', x0);
    formData.append('k', k);
    formData.append('g', g);
    formData.append('c', c);

    // Hacer la solicitud POST a la ruta de tu función en FastAPI
    fetch('/lehmer', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Hubo un problema con el formato de los datos\nDeben ser enteros mayores a 0.');
        }
        return response.json();
    })
    .then(data => {
        // Verificar si la respuesta contiene la clave "error"
        if (data.error) {
            // Manejar el mensaje de error y mostrarlo
            console.error('Error:', data.error);
            document.getElementById('errorContainer').innerText = data.error;
            document.getElementById('errorContainer').style.display = 'block';
        } else {
            // Verificar si la respuesta contiene las claves esperadas
            if (data.x_list && data.r_list) {
                // Manejar la respuesta del servidor
                console.log(data);

                const resultsBody = document.getElementById('resultsBody');
                resultsBody.innerHTML = ""; // Limpiar resultados anteriores

                data.x_list.forEach((x, index) => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <th scope="row">${index + 1}</th>
                        <td>${x}</td>
                        <td>${data.r_list[index]}</td>
                    `;
                    resultsBody.appendChild(row);
                });

                // Mostrar la sección de resultados
                document.getElementById('results').style.display = 'block';
            } else {
                // La respuesta no tiene la estructura esperada
                throw new Error('La respuesta del servidor no tiene la estructura esperada.');
            }
        }
    })
    .catch(error => {
        // Manejar errores de la solicitud y mostrar el mensaje de error
        console.error('Error:', error.message);
        document.getElementById('errorContainer').innerText = error.message;
        document.getElementById('errorContainer').style.display = 'block';
    });
}

function sendFormMult() {
    console.log("Enviando formulario...");

    // Limpiar mensajes de error anteriores
    document.getElementById('errorContainer').style.display = 'none';
    document.getElementById('results').style.display = 'none';

    // Obtener los valores de los campos de entrada
    const x0 = document.getElementById('x0').value;
    const k = document.getElementById('k').value;
    const g = document.getElementById('g').value;

    // Construir el cuerpo de la solicitud
    const formData = new FormData();
    formData.append('x0', x0);
    formData.append('k', k);
    formData.append('g', g);

    // Hacer la solicitud POST a la ruta de tu función en FastAPI
    fetch('/mult', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Hubo un problema con el formato de los datos\nDeben ser enteros mayores a 0.');
        }
        return response.json();
    })
    .then(data => {
        // Verificar si la respuesta contiene la clave "error"
        if (data.error) {
            // Manejar el mensaje de error y mostrarlo
            console.error('Error:', data.error);
            document.getElementById('errorContainer').innerText = data.error;
            document.getElementById('errorContainer').style.display = 'block';
        } else {
            // Verificar si la respuesta contiene las claves esperadas
            if (data.x_list && data.r_list) {
                // Manejar la respuesta del servidor
                console.log(data);

                const resultsBody = document.getElementById('resultsBody');
                resultsBody.innerHTML = ""; // Limpiar resultados anteriores

                data.x_list.forEach((x, index) => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <th scope="row">${index + 1}</th>
                        <td>${x}</td>
                        <td>${data.r_list[index]}</td>
                    `;
                    resultsBody.appendChild(row);
                });

                // Mostrar la sección de resultados
                document.getElementById('results').style.display = 'block';
            } else {
                // La respuesta no tiene la estructura esperada
                throw new Error('La respuesta del servidor no tiene la estructura esperada.');
            }
        }
    })
    .catch(error => {
        // Manejar errores de la solicitud y mostrar el mensaje de error
        console.error('Error:', error.message);
        document.getElementById('errorContainer').innerText = error.message;
        document.getElementById('errorContainer').style.display = 'block';
    });
}