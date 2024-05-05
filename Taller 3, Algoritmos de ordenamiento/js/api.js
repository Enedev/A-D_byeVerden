let data; // Variable global para almacenar los datos
let pageSize = 20; // Número de elementos por página
let totalPages; // Total de páginas
let currentPage = 1; // Página actual

function generateRandomDates() {
    // Generar un número entero aleatorio entre -10000 y 10000 para el ID
    return Math.floor(Math.random() * 1990) - 1000;
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
            totalPages = Math.ceil(data.length / pageSize); // Calcular el total de páginas
            mostrarData(data, currentPage);
            renderPagination();
        })
        .catch(error => console.log(error));
}


function renderPagination() {
    let paginationHtml = '';
    const maxPagesToShow = 10; // Máximo de páginas a mostrar alrededor de la actual

    // Botón para la primera página
    paginationHtml += `<button class="btn btn-outline-primary mx-2" onclick="changePage(1)" id="firstPageButton">First</button>`;

    // Mostrar páginas alrededor de la actual
    let startPage = Math.max(1, currentPage - Math.floor(maxPagesToShow / 2));
    let endPage = Math.min(totalPages, startPage + maxPagesToShow - 1);

    // Ajustar el inicio y fin si no se muestra el máximo de páginas
    if (endPage - startPage + 1 < maxPagesToShow) {
        startPage = Math.max(1, endPage - maxPagesToShow + 1);
    }

    for (let i = startPage; i <= endPage; i++) {
        if (i === currentPage) {
            paginationHtml += `<span class="mx-2">${i}</span>`;
        } else {
            paginationHtml += `<button class="btn btn-outline-primary mx-2" onclick="changePage(${i})">${i}</button>`;
        }
    }

    // Botón para la última página
    paginationHtml += `<button class="btn btn-outline-primary mx-2" onclick="changePage(${totalPages})">Last</button>`;

    document.getElementById('pagination-container').innerHTML = paginationHtml;
}


function changePage(pageNumber) {
    currentPage = pageNumber;
    mostrarData(data, currentPage);
    renderPagination();
}

function mostrarData(data, page) {
    
    let startIndex = (page - 1) * pageSize;
    let endIndex = startIndex + pageSize;
    let pageData = data.slice(startIndex, endIndex);

    let body = "";
    for (let i = 0; i < pageData.length; i++) {
        body += `<tr><td>${pageData[i].tipo}</td><td>
        ${pageData[i].rubro}</td><td>${pageData[i].subregion}</td><td>${pageData[i].anio}</td><td>${pageData[i].municipio}</td>
        <td>${pageData[i].area_total}</td>
        <td>${pageData[i].area_produccion}</td>
        <td>${pageData[i].volumen_produccion}</td></tr>`;
    }
    document.getElementById('data').innerHTML = body;
    console.log("Datos mostrados en la tabla");
    
}
// Resto de tu código...

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
    currentPage = 1; 
    mostrarData(data, currentPage); // Actualizar la tabla después de ordenar
}

// Función para vaciar los elementos select
function vaciarSelects() {
    $('#columnaSelect').val('');
    $('#metodoSelect').val('');
}

function checkForNegativeValues(columnName) {
    return data.some(item => item[columnName] < 0);
}
// Función para abrir el modal de ordenar
function openOrdenarModal() {
    vaciarSelects(); // Vaciar los selects before opening the modal

    // Add an event listener to the column select element
    $('#columnaSelect').on('change', function() {
        let columnName = $(this).val();

        // Check if the selected column contains negative values
        if (checkForNegativeValues(columnName)) {
            // Disable the counting, radix, and bucket sort options
            $('#metodoSelect option[value="counting"]').prop('disabled', true);
            $('#metodoSelect option[value="radix"]').prop('disabled', true);
            $('#metodoSelect option[value="bucket"]').prop('disabled', true);

            // Display a clear explanation
            $('#exclusionMessage').text('Counting, Radix, and Bucket sorts are disabled because they do not work with negative numbers.');
        } else {
            // Enable all options
            $('#metodoSelect option').prop('disabled', false);
            $('#exclusionMessage').text('');
        }
    });

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
