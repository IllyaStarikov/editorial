# Sorting Algorithms Compared

Ever wondered how sorting algorithms looked in Swift? I did too — so I implemented some. Below you can find the following:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quicksort

As a preface: some of the algorithms use a self-implemented swap function — it is as follows:

```swift
extension Array {
    mutating func swap(i: Int, _ j: Int) {
        (self[i], self[j]) = (self[j], self[i])
    }
}
```

## Bubble Sort
```swift
func bubbleSort(var unsorted: Array<Int>) -> Array<Int> {
    for i in 0..<unsorted.count - 1 {
        for j in 0..<unsorted.count - i - 1 {
            if unsorted[j] > unsorted[j + 1] {
                unsorted.swap(j, j + 1)
            }
        }
    }
    
    return unsorted
}
```

## Selection Sort
```swift
func selectionSort(var unsorted: Array<Int>) -> Array<Int> {
    for i in 0..<unsorted.count - 1 {
        var minimumIndex = i
        for j in i + 1 ..< unsorted.count {
            if unsorted[j] < unsorted[minimumIndex] {
                minimumIndex = j
            }
            unsorted.swap(minimumIndex, i)
        }
    }
    
    return unsorted
}
```

## Insertion Sort
```swift
func insertionSort(var unsorted: Array<Int>) -> Array<Int> {
    for j in 1...unsorted.count - 1 {
        let key = unsorted[j];
        var i = j - 1
        
        while i >= 0 && unsorted[i] > key {
            unsorted[i + 1] = unsorted[i]
            i--
        }
        
        unsorted[i + 1] = key
    }
    
    return unsorted
}
```


## Merge Sort
```swift
func merge(leftArray left: Array<Int>, rightArray right: Array<Int>) -> Array<Int> {
    var result = [Int]()
    var leftIndex = 0, rightIndex = 0
    
    // Calculated variable to determine if the indexes have reached end of their respective arrays
    var indexesHaveReachedEndOfArrays: Bool { return leftIndex < left.count && rightIndex < right.count }
    
    while indexesHaveReachedEndOfArrays {
        if left[leftIndex] < right[rightIndex] {
            result.append(left[leftIndex])
            leftIndex++
        }
        else if left[leftIndex] > right[rightIndex] {
            result.append(right[rightIndex])
            rightIndex++
        }
        else {
            result.append(left[leftIndex])
            result.append(right[rightIndex])
            
            leftIndex++
            rightIndex++
        }
    }
    
    result += Array(left[leftIndex..<left.count])
    result += Array(right[rightIndex..<right.count])
    
    return result
}

func mergesort(unsorted: Array<Int>) -> Array<Int> {
    let size = unsorted.count
    if size < 2 { return unsorted }
    
    let split = Int(size / 2)
    
    let left = Array(unsorted[0 ..< split])
    let right = Array(unsorted[split ..< size])
    
    let sorted = merge(leftArray: mergesort(left), rightArray: mergesort(right))
    return sorted
}
```


## Quick Sort
```swift
func quicksort(var unsorted: Array<Int>) -> Array<Int> {
    quicksort(&unsorted, firstIndex: 0, lastIndex: unsorted.count - 1)
    return unsorted
}

private func quicksort(inout unsorted: Array<Int>, firstIndex: Int, lastIndex: Int) -> Array<Int> {
    if firstIndex < lastIndex {
        let split = partition(&unsorted, firstIndex: firstIndex, lastIndex: lastIndex)
        
        quicksort(&unsorted, firstIndex: firstIndex, lastIndex: split - 1)
        quicksort(&unsorted, firstIndex: split + 1, lastIndex: lastIndex)
    }
    
    return unsorted
}

private func partition(inout unsorted: Array<Int>, firstIndex: Int, lastIndex: Int) -> Int {
    let pivot = unsorted[lastIndex]
    var wall = firstIndex
    
    for i in firstIndex ... lastIndex - 1 {
        if unsorted[i] <= pivot {
            unsorted.swap(wall, i)
            wall++
        }
    }
    
    unsorted.swap(wall, lastIndex)
    return wall
}
```