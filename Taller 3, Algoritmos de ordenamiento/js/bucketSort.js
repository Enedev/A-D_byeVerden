// no funciona para negativos ni flotantes

function bucketSort(arr, propertyName) {
    const n = arr.length;
    if (n === 0) return arr;

    const min = Math.min(...arr.map(item => item[propertyName]));
    const max = Math.max(...arr.map(item => item[propertyName]));
    const bucketSize = 5;

    const bucketCount = Math.floor((max - min) / bucketSize) + 1;
    const buckets = Array.from({ length: bucketCount }, () => []);

    arr.forEach(item => {
        const bucketIndex = Math.floor((item[propertyName] - min) / bucketSize);
        buckets[bucketIndex].push(item);
    });

    arr.length = 0;
    buckets.forEach(bucket => insertionSort(bucket, propertyName).forEach(item => arr.push(item)));

    return arr;
}
