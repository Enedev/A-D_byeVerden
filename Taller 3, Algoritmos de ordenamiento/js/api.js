let data; // Variable global para almacenar los datos

function generateRandomId() {
    // Generar un número entero aleatorio entre -10000 y 10000 para el ID
    return Math.floor(Math.random() * 100) - 50;
}

function fetchAndShowData() {
    let url = 'https://jsonplaceholder.typicode.com/users/';
    fetch(url)
        .then(response => response.json())
        .then(result => {
            // Modificar los IDs para que sean aleatorios
            result.forEach(user => {
                user.id = generateRandomId();
            });
            
            data = result;
            mostrarData(data);
        })
        .catch(error => console.log(error));
}


function mostrarData(data) {
    let body = "";
    for (let i = 0; i < data.length; i++) {
        body += `<tr><td>${data[i].id}</td><td>${data[i].name}</td><td>${data[i].email}</td></tr>`;
    }
    document.getElementById('data').innerHTML = body;
    console.log("Datos mostrados en la tabla");
}


function updatePropertyName(newPropertyName) {
    propertyName = newPropertyName;
}

function sortData(method) {
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

fetchAndShowData(); // Cargar y mostrar los datos al cargar la página
