function heapSort(arr, propertyName) {
    buildMaxHeap(arr, propertyName);
    let n = arr.length;
    for (let i = arr.length - 1; i > 0; i--) {
        [arr[0], arr[i]] = [arr[i], arr[0]];
        maxHeapify(arr, 0, --n, propertyName);
    }
    return arr;
}

function buildMaxHeap(arr, propertyName) {
    for (let i = Math.floor(arr.length / 2); i >= 0; i--) {
        maxHeapify(arr, i, arr.length, propertyName);
    }
}

function maxHeapify(arr, i, n, propertyName) {
    let left = 2 * i + 1;
    let right = 2 * i + 2;
    let largest = i;

    if (left < n && arr[left][propertyName] > arr[largest][propertyName]) {
        largest = left;
    }

    if (right < n && arr[right][propertyName] > arr[largest][propertyName]) {
        largest = right;
    }

    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]];
        maxHeapify(arr, largest, n, propertyName);
    }
}
