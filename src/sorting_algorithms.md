# Sorting Algorithms

When I was a Teacher Assistant (TA) in Intro To Computer Science lab, fellow TA
[Ian](https://www.linkedin.com/in/ianhowell0/) and I were showing off our programming prowess. I thought I had it in the bag: I had solved a competitive programming problem in compile-time (C++ templates are Turing-complete!) and a Space Invaders clone for a class.

But Ian was more clever than I, and showed me something that fundamentally changed how I saw a core-component of programming: a [terminal-based (ncurses) sorting algorithm visualizers](https://github.com/ian-howell/sort-visualizer).
It was the first time I had ever seen these algorithms graphed like this — ever! And, yes, I blame my Algorithm instructor. I finally could see all the hypothetical sorting in a real-life application.

With the power of LLMs in hand, and a website as my canvas, I wanted to see if I could recreate this. Kudos to you, Ian.

Sorting algorithms form the backbone of computer science, serving as fundamental building blocks for countless applications from database management to search engines. This comprehensive guide examines the 25 most important sorting algorithms, organized by type, with detailed analysis of their performance, implementation, and practical applications.

<div class="ghost-toc"></div>

## 1. Basic Comparison-Based Algorithms {#basic-comparison}

These fundamental algorithms serve as the foundation for understanding sorting concepts, though they generally have O(n²) time complexity.

### 1.1 Bubble Sort

**Complexity Analysis:**
- Best Case: **O(n)** / Ω(n) - when array is already sorted
- Average Case: **O(n²)** / Θ(n²)
- Worst Case: **O(n²)**
- Space: **O(1)**

**Properties:** Stable, In-place, Adaptive

```python
def bubble_sort(arr):
    """
    Bubble Sort with optimization
    Time: O(n²) average/worst, O(n) best
    Space: O(1)
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred, array is sorted
        if not swapped:
            break

    return arr
```

**When to Use:**
- Small datasets (< 50 elements)
- Educational purposes - excellent for teaching
- Nearly sorted data
- Memory-constrained environments

**Step-by-Step Example:**
Array: [64, 34, 25, 12, 22, 11, 90]

Pass 1: [34, 25, 12, 22, 11, 64, 90] - Largest element "bubbles" to end
Pass 2: [25, 12, 22, 11, 34, 64, 90]
... continues until sorted

**History:** First described by Edward Harry Friend in 1956. The name "bubble sort" was coined by Kenneth E. Iverson due to how smaller elements "bubble" to the top.

**Notable Trivia:** Donald Knuth famously stated "bubble sort seems to have nothing to recommend it, except a catchy name." Despite criticism, it remains the most taught sorting algorithm due to its simplicity.

---

### 1.2 Selection Sort

**Complexity Analysis:**
- Best/Average/Worst Case: **O(n²)** - always makes same comparisons
- Space: **O(1)**

**Properties:** Unstable, In-place, Not adaptive

```python
def selection_sort(arr):
    """
    Selection Sort implementation
    Time: O(n²) for all cases
    Space: O(1)
    """
    n = len(arr)

    for i in range(n):
        # Find minimum element in remaining unsorted array
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
```

**When to Use:**
- When memory write operations are expensive (e.g., flash memory)
- Small datasets where simplicity matters
- When the number of swaps needs to be minimized

**Key Advantage:** Performs only O(n) swaps compared to O(n²) for bubble sort.

**History:** Has ancient origins in manual sorting processes. Formalized in the 1950s as one of the fundamental sorting methods.

---

### 1.3 Insertion Sort

**Complexity Analysis:**
- Best Case: **O(n)** - already sorted
- Average/Worst Case: **O(n²)**
- Space: **O(1)**

**Properties:** Stable, In-place, Adaptive, Online

```python
def insertion_sort(arr):
    """
    Insertion Sort implementation
    Time: O(n²) average/worst, O(n) best
    Space: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
```

**When to Use:**
- Small datasets (typically < 50 elements)
- Nearly sorted data - performs in O(n) time
- Online algorithms - when data arrives sequentially
- As a subroutine in quicksort and mergesort for small subarrays

**Notable Use:** Used in Timsort (Python's built-in sort) for small runs. Often faster than O(n log n) algorithms for arrays with fewer than 10-20 elements.

---

### 1.4 Shell Sort

**Complexity Analysis:**
- Best Case: **O(n log n)**
- Average Case: **O(n^1.25)** to **O(n^1.5)** depending on gap sequence
- Worst Case: **O(n²)** for Shell's original sequence
- Space: **O(1)**

**Properties:** Unstable, In-place, Adaptive

```python
def shell_sort(arr):
    """
    Shell Sort using Shell's original sequence
    Time: O(n²) worst case, O(n log n) average
    Space: O(1)
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:
        # Perform gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr
```

**When to Use:**
- Medium-sized datasets (100-5000 elements)
- When recursion should be avoided
- Embedded systems - simple and efficient

**History:** Invented by Donald L. Shell in 1959, it was one of the first algorithms to break the O(n²) barrier.

---

### 1.5 Cocktail Shaker Sort (Bidirectional Bubble Sort)

**Complexity Analysis:**
- Best Case: **O(n)**
- Average/Worst Case: **O(n²)**
- Space: **O(1)**

**Properties:** Stable, In-place, Adaptive, Bidirectional

```python
def cocktail_shaker_sort(arr):
    """
    Cocktail Shaker Sort (Bidirectional Bubble Sort)
    Time: O(n²) average/worst, O(n) best
    Space: O(1)
    """
    n = len(arr)
    start = 0
    end = n - 1

    while start < end:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        end -= 1
        swapped = False

        # Backward pass
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        if not swapped:
            break

        start += 1

    return arr
```

**Advantage:** Better than bubble sort at moving small elements (turtles) to the beginning.

---

## 2. Efficient Comparison-Based Algorithms {#efficient-comparison}

These algorithms achieve O(n log n) average performance and form the backbone of many practical sorting implementations.

### 2.1 Quick Sort

**Complexity Analysis:**
- Best/Average Case: **O(n log n)**
- Worst Case: **O(n²)** - when pivot is always minimum/maximum
- Space: **O(log n)** - recursion stack

**Properties:** Unstable, In-place, Not adaptive

```python
def quicksort(arr, low=0, high=None):
    """
    Quicksort with Hoare partition scheme
    Time: O(n log n) average, O(n²) worst
    Space: O(log n)
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_idx)
        quicksort(arr, pivot_idx + 1, high)

    return arr

def partition(arr, low, high):
    """Hoare partition scheme"""
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]
```

**Why It's Preferred Despite O(n²) Worst Case:**
1. Excellent average-case performance with good constant factors
2. Cache-friendly sequential access patterns
3. In-place sorting
4. Modern implementations use introsort to guarantee O(n log n)

**History:** Invented by Tony Hoare in 1959 while working on machine translation at Moscow State University.

---

### 2.2 Merge Sort

**Complexity Analysis:**
- All Cases: **O(n log n)** - guaranteed performance
- Space: **O(n)** - requires additional space for merging

**Properties:** Stable, Not in-place, Not adaptive

```python
def merge_sort(arr):
    """
    Merge Sort implementation
    Time: O(n log n) guaranteed
    Space: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
```

**When to Use:**
- When stability is required
- External sorting (large datasets that don't fit in memory)
- Linked lists (efficient with O(1) extra space)
- Parallel processing

**History:** Invented by John von Neumann in 1945, with detailed analysis published in 1948.

---

### 2.3 Heap Sort

**Complexity Analysis:**
- All Cases: **O(n log n)** - guaranteed performance
- Space: **O(1)** - true in-place sorting

**Properties:** Unstable, In-place, Not adaptive

```python
def heap_sort(arr):
    """
    Heap Sort implementation
    Time: O(n log n) guaranteed
    Space: O(1)
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    """Maintain heap property"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

**When to Use:**
- Memory-constrained environments
- Real-time systems (guaranteed performance)
- Systems concerned with malicious input

**History:** Invented by J. W. J. Williams in 1964, with in-place version by Robert Floyd.

---

### 2.4 Binary Tree Sort

**Complexity Analysis:**
- Best/Average Case: **O(n log n)** - with balanced tree
- Worst Case: **O(n²)** - with unbalanced tree
- Space: **O(n)** - for tree structure

**Properties:** Can be stable, Not in-place

**When to Use:**
- Educational purposes
- When tree structure is needed for other operations
- Online sorting

**Note:** Self-balancing trees (AVL, Red-Black) guarantee O(n log n) performance.

---

### 2.5 Smooth Sort

**Complexity Analysis:**
- Best Case: **O(n)** - for sorted data
- Average/Worst Case: **O(n log n)**
- Space: **O(1)**

**Properties:** Unstable, In-place, Adaptive

**History:** Invented by Edsger W. Dijkstra in 1981 as an improvement over heapsort for partially sorted data.

**Notable Use:** Used in musl C library's qsort() implementation.

---

## 3. Non-Comparison Based Algorithms {#non-comparison}

These algorithms achieve linear O(n) time complexity by exploiting specific properties of the data rather than comparing elements.

### 3.1 Counting Sort

**Complexity Analysis:**
- All Cases: **O(n + k)** where k is the range of values
- Space: **O(n + k)**

**Properties:** Stable, Not in-place

```python
def counting_sort(arr):
    """
    Counting Sort for non-negative integers
    Time: O(n + k)
    Space: O(n + k)
    """
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Count occurrences
    for num in arr:
        count[num] += 1

    # Calculate cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build output array
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output
```

**When to Use:**
- Sorting integers in a small range
- As a subroutine in radix sort
- When k is O(n) or smaller

**History:** Invented by Harold H. Seward in 1954 at MIT.

---

### 3.2 Radix Sort

**Complexity Analysis:**
- All Cases: **O(d × (n + k))** where d is number of digits
- Space: **O(n + k)**

**Properties:**
- LSD (Least Significant Digit): Stable
- MSD (Most Significant Digit): Can be stable

```python
def radix_sort_lsd(arr):
    """
    LSD Radix Sort implementation
    Time: O(d × (n + k))
    Space: O(n + k)
    """
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
```

**When to Use:**
- Sorting integers with many digits
- String sorting (MSD variant)
- When d is small compared to log n

**History:** Dates back to 1887 with Herman Hollerith's tabulating machines.

---

### 3.3 Bucket Sort

**Complexity Analysis:**
- Best/Average Case: **O(n + k)** for uniform distribution
- Worst Case: **O(n²)** when all elements fall into one bucket
- Space: **O(n + k)**

**Properties:** Stable (if sub-sorting is stable), Not in-place

```python
def bucket_sort(arr):
    """
    Bucket Sort for floating-point numbers
    Time: O(n + k) average
    Space: O(n + k)
    """
    if not arr:
        return arr

    min_val, max_val = min(arr), max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Distribute elements into buckets
    for num in arr:
        if max_val == min_val:
            index = 0
        else:
            index = int((num - min_val) / (max_val - min_val) * (bucket_count - 1))
        buckets[index].append(num)

    # Sort individual buckets
    result = []
    for bucket in buckets:
        if bucket:
            bucket.sort()  # Can use insertion sort
            result.extend(bucket)

    return result
```

**When to Use:**
- Uniformly distributed floating-point numbers
- Large datasets with known range
- When memory is not a constraint

---

### 3.4 Pigeonhole Sort

**Complexity Analysis:**
- All Cases: **O(n + range)** where range = max - min + 1
- Space: **O(range)**

**Properties:** Stable, Not in-place

**When to Use:**
- Small range of integer values
- When range is comparable to n
- Simple counting applications

**History:** Based on the pigeonhole principle, formally described by A.J. Lotka (1926).

---

### 3.5 Flash Sort

**Complexity Analysis:**
- Best/Average Case: **O(n)** for uniform distribution
- Worst Case: **O(n²)**
- Space: **O(m)** where m is number of classes

**Properties:** Unstable, In-place (major advantage)

**When to Use:**
- Large uniformly distributed datasets
- When memory is limited
- When O(n) average performance is critical

**History:** Invented by Karl-Dietrich Neubert in 1998 as an efficient in-place implementation of bucket sort.

---

## 4. Modern Hybrid Algorithms {#hybrid-algorithms}

These algorithms represent the state-of-the-art in practical sorting, combining multiple techniques for superior performance.

### 4.1 Timsort

**Complexity Analysis:**
- Best Case: **O(n)** - already sorted
- Average/Worst Case: **O(n log n)**
- Space: **O(n)**

**Properties:** Stable, Not in-place

**Key Innovations:**
1. **Run Detection:** Identifies naturally occurring sorted subsequences
2. **Minimum Run Size:** Calculates optimal minrun (32-64 elements)
3. **Galloping Mode:** Switches to exponential search when one run consistently "wins"

**Where It's Used:**
- Python's default sort since version 2.3
- Java for sorting objects (Java 7+)
- Android, V8, Swift, Rust

**History:** Created in 2002 by Tim Peters for Python. A critical bug was discovered and fixed in 2015 through formal verification.

---

### 4.2 Introsort (Introspective Sort)

**Complexity Analysis:**
- All Cases: **O(n log n)** - guaranteed by heapsort fallback
- Space: **O(log n)**

**Properties:** Unstable, In-place

**Techniques Combined:**
- Quicksort for main sorting
- Heapsort when recursion depth exceeds 2×log₂(n)
- Insertion sort for small subarrays (< 16 elements)

**Where It's Used:**
- C++ STL's std::sort() in GCC and LLVM
- Microsoft .NET Framework 4.5+

**History:** Created by David Musser in 1997 to provide guaranteed O(n log n) performance while maintaining quicksort's average-case speed.

---

### 4.3 Block Sort (WikiSort)

**Complexity Analysis:**
- Best Case: **O(n)**
- Average/Worst Case: **O(n log n)**
- Space: **O(1)** - constant space!

**Properties:** Stable, In-place

**Key Innovation:** Achieves stable merge sort performance with O(1) space by using internal buffering.

**When to Use:** When O(1) space complexity and stability are both required.

---

### 4.4 Pattern-defeating Quicksort (pdqsort)

**Complexity Analysis:**
- Best Case: **O(n)** for specific patterns
- Average/Worst Case: **O(n log n)**
- Space: **O(log n)**

**Properties:** Unstable, In-place

**Key Innovations:**
1. Pattern detection and optimization
2. Branchless partitioning
3. Adaptive strategy based on input characteristics

**Where It's Used:**
- Rust's default unstable sort
- C++ Boost libraries

**History:** Created by Orson Peters in 2016 to improve upon introsort with better pattern handling.

---

### 4.5 Dual-Pivot Quicksort

**Complexity Analysis:**
- Best Case: **O(n)** when all elements equal
- Average Case: **O(n log n)** - 5% fewer comparisons than single-pivot
- Worst Case: **O(n²)** - still possible but less likely
- Space: **O(log n)**

**Properties:** Unstable, In-place

**Key Innovation:** Uses two pivots to partition array into three parts, reducing comparisons.

**Where It's Used:** Java's default algorithm for primitive arrays since Java 7.

**History:** Created by Vladimir Yaroslavskiy in 2009, adopted by Java in 2011.

---

## 5. Specialized and Educational Algorithms {#specialized-algorithms}

These algorithms serve specific purposes or demonstrate important concepts in computer science education.

### 5.1 Comb Sort

**Complexity Analysis:**
- Best Case: **O(n log n)**
- Average Case: **O(n²/2^p)** where p is number of increments
- Worst Case: **O(n²)**
- Space: **O(1)**

**Properties:** Unstable, In-place

**Key Feature:** Improves upon bubble sort using variable gap with shrink factor of 1.3.

**History:** Developed by Włodzimierz Dobosiewicz in 1980 to address bubble sort's inefficiency.

---

### 5.2 Gnome Sort (Stupid Sort)

**Complexity Analysis:**
- Best Case: **O(n)**
- Average/Worst Case: **O(n²)**
- Space: **O(1)**

**Properties:** Stable, In-place, Adaptive

**Unique Feature:** Uses only a single while loop - inspired by garden gnomes sorting flower pots.

---

### 5.3 Cycle Sort

**Complexity Analysis:**
- All Cases: **O(n²)**
- Space: **O(1)**

**Properties:** Unstable, In-place

**Key Feature:** Minimizes memory writes - each element is written at most once to its correct position.

**When to Use:** When memory write operations are expensive (EEPROM, Flash memory).

---

### 5.4 Pancake Sort

**Complexity Analysis:**
- Best Case: **O(n)**
- Average/Worst Case: **O(n²)**
- Space: **O(1)**

**Properties:** Unstable, In-place

**Unique Constraint:** Only allowed operation is "flip" (reverse prefix).

**Historical Note:** Bill Gates' only published academic paper was on this problem (1979), providing a (5n+5)/3 upper bound algorithm.

---

### 5.5 Bogo Sort

**Complexity Analysis:**
- Best Case: **O(n)** - already sorted
- Average Case: **O(n·n!)** - expected permutations
- Worst Case: **O(∞)** - theoretically unbounded
- Space: **O(1)**

**Properties:** Unstable, In-place

**Educational Value:**
- Demonstrates worst-case analysis
- Teaches randomized algorithms
- Shows importance of algorithm selection

```python
import random

def bogo_sort(arr):
    """The worst sorting algorithm ever conceived"""
    def is_sorted(arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

    while not is_sorted(arr):
        random.shuffle(arr)

    return arr
```

**Trivia:** "Quantum Bogo Sort" hypothetically destroys universes where array isn't sorted, leaving only sorted universes.

---

## Summary and Recommendations

### Performance Comparison Table

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | In-Place |
|-----------|-----------|--------------|------------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Yes | No |
| Radix Sort | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Yes | No |
| Timsort | O(n) | O(n log n) | O(n log n) | O(n) | Yes | No |

### When to Use Which Algorithm

**For Small Datasets (< 50 elements):**
- Insertion Sort - simple and efficient
- Selection Sort - when minimizing swaps matters

**For General Purpose:**
- Timsort (Python) or Introsort (C++) - best overall performance
- Quick Sort with good pivot selection - excellent average case

**For Guaranteed Performance:**
- Merge Sort - stable and predictable
- Heap Sort - when O(1) space is required

**For Special Data Types:**
- Counting Sort - small integer ranges
- Radix Sort - large integers or strings
- Bucket Sort - uniformly distributed floats

**For Educational Purposes:**
- Start with Bubble Sort for simplicity
- Progress to Quick Sort and Merge Sort
- Use Bogo Sort to demonstrate algorithm analysis

### Key Takeaways

1. **No single best algorithm** - choice depends on data characteristics, constraints, and requirements

2. **Modern algorithms are hybrids** - combining techniques yields superior performance

3. **Stability matters** for sorting complex objects where maintaining relative order is important

4. **Space-time tradeoffs** are crucial - some algorithms trade memory for speed

5. **Real-world performance** often differs from theoretical complexity due to cache effects, data patterns, and implementation details

Understanding these 25 algorithms provides a comprehensive foundation for tackling sorting problems in any context, from embedded systems to large-scale data processing.
