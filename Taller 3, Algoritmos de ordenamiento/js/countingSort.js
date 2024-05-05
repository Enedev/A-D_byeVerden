// no funciona para negativos ni flotantes

function countingSort(arr, propertyName) {
    const maxValue = Math.max(...arr.map(item => item[propertyName]));
    const counts = new Array(maxValue + 1).fill(0);

    arr.forEach(item => counts[item[propertyName]]++);

    let sortedIndex = 0;
    counts.forEach((count, value) => {
        for (let i = 0; i < count; i++) {
            // Crear un nuevo objeto con las otras propiedades intactas
            const newItem = { ...arr[sortedIndex], [propertyName]: value };
            arr[sortedIndex++] = newItem;
        }
    });

    return arr;
}
