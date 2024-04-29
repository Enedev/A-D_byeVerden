function bubbleSort(arr, propertyName) {
    let swapped;
    do {
      swapped = false;
      for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i][propertyName]> arr[i + 1][propertyName]) {
          // Swap elements
          let temp = arr[i];
          arr[i] = arr[i + 1];
          arr[i + 1] = temp;
          swapped = true;
        }
      }
    } while (swapped);
    console.log(arr)
}