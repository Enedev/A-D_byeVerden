let data; // Variable global para almacenar los datos

function generateRandomDates() {
    // Generar un número entero aleatorio entre -10000 y 10000 para el ID
    return Math.floor(Math.random() * 1990) - 0;
}

// Cambiar el randomGenerate

function fetchAndShowData() {
    let url = 'https://www.datos.gov.co/resource/t2ca-uae5.json';
    fetch(url)
        .then(response => response.json())
        .then(result => {
            // Modificar los IDs para que sean aleatorios
            result.forEach(user => {
                user.anio = generateRandomDates();
                user.area_total = parseFloat(user.area_total); // Convertir a número
                user.area_produccion = parseFloat(user.area_produccion); // Convertir a número
                user.volumen_produccion = parseFloat(user.volumen_produccion); // Convertir a número
            });
            
            data = result;
            mostrarData(data);
        })
        .catch(error => console.log(error));
}


function mostrarData(data) {
    let body = "";
    for (let i = 0; i < data.length; i++) {
        body += `<tr><td>${data[i].tipo}</td><td>
        ${data[i].rubro}</td><td>${data[i].subregion}</td><td>${data[i].anio}</td><td>${data[i].municipio}</td>
        <td>${data[i].area_total}</td>
        <td>${data[i].area_produccion}</td>
        <td>${data[i].volumen_produccion}</td></tr>`;
    }
    document.getElementById('data').innerHTML = body;
    console.log("Datos mostrados en la tabla");
}

function sortData(method,propertyName) {
    if (method === 'bubble') {
        bubbleSort(data, propertyName);
    } else if (method === 'quick') {
        quickSort(data, propertyName);
    } else if (method === 'merge') {
        mergeSort(data, propertyName);
    }else if (method === 'counting') {
        countingSort(data, propertyName);
    }else if (method === 'selection') {
        selectionSort(data, propertyName);
    }else if (method === 'insertion') {
        insertionSort(data, propertyName);
    }else if (method === 'bucket') {
        bucketSort(data, propertyName);
    }else if (method === 'radix') {
        radixSort(data, propertyName);
    }else if (method === 'radix') {
        heapSort(data, propertyName);
    }
    
    mostrarData(data); // Actualizar la tabla después de ordenar
}

// Función para vaciar los elementos select
function vaciarSelects() {
    $('#columnaSelect').val('');
    $('#metodoSelect').val('');
}

// Función para abrir el modal de ordenar
function openOrdenarModal() {
    vaciarSelects(); // Vaciar los selects antes de abrir el modal
    $('#ordenarModal').modal('show');
}

// Función para ordenar los datos
function ordenarDatos() {
    let columna = $('#columnaSelect').val();
    let metodo = $('#metodoSelect').val();
    sortData(metodo, columna);
    $('#ordenarModal').modal('hide'); // Cierra el modal al ordenar
    vaciarSelects(); // Vaciar los selects después de ordenar
}

fetchAndShowData(); // Cargar y mostrar los datos al cargar la página
