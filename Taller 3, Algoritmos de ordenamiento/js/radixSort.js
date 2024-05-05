// no funciona para negativos ni flotantes

function radixSort(arr, propertyName) {
    const max = Math.max(...arr.map(item => item[propertyName]));
    for (let exp = 1; Math.floor(max / exp) > 0; exp *= 10) {
        countingSortByDigit(arr, propertyName, exp);
    }
    return arr;
}

function countingSortByDigit(arr, propertyName, exp) {
    const counts = new Array(10).fill(0);
    const output = new Array(arr.length);

    arr.forEach(item => {
        const digit = Math.floor(item[propertyName] / exp) % 10;
        counts[digit]++;
    });

    for (let i = 1; i < 10; i++) {
        counts[i] += counts[i - 1];
    }

    for (let i = arr.length - 1; i >= 0; i--) {
        const digit = Math.floor(arr[i][propertyName] / exp) % 10;
        output[counts[digit] - 1] = arr[i];
        counts[digit]--;
    }

    for (let i = 0; i < arr.length; i++) {
        arr[i] = output[i];
    }
}
