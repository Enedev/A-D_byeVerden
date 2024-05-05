function quickSort(arr, propertyName) {
    if (arr.length <= 1) {
        return arr;
    }

    const pivot = arr[arr.length - 1][propertyName];
    const left = [];
    const right = [];

    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i][propertyName] < pivot) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }

    const sortedLeft = quickSort(left, propertyName);
    const sortedRight = quickSort(right, propertyName);

    return [...sortedLeft, arr[arr.length - 1], ...sortedRight];
}
