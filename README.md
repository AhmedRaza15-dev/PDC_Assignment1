Here’s your **Performance Analysis Report** perfectly formatted for a **GitHub README.md** — clean, structured, and Markdown-optimized (with headings, tables, and code-like formatting for clarity).

You can copy and paste this directly into your `README.md` file 👇

---

# 🧠 Performance Analysis Report: Multithreaded Searching and Sorting Algorithms

## 📌 1. Objective

To implement and analyze task parallelism using **multithreading in Python** for fundamental algorithms: **Linear Search** and **Merge Sort**.
The aim is to evaluate performance improvements through parallel execution and understand the practical limitations of Python's threading model for **CPU-bound tasks**.

---

## ⚙️ 2. Problem Description

This study investigates whether multithreading can provide performance benefits for computational tasks involving array searching and sorting.
The challenge lies in Python's **Global Interpreter Lock (GIL)**, which restricts true parallel execution of CPU-bound tasks.

**Key Focus Areas:**

* Measuring execution time differences between single-threaded and multithreaded implementations
* Analyzing how array size affects performance gains
* Evaluating the overhead of thread management versus computational benefits

---

## 💻 3. Implementation Details

### **Algorithms Implemented**

* **Linear Search:** Sequential search algorithm with *O(n)* complexity
* **Merge Sort:** Divide-and-conquer sorting algorithm with *O(n log n)* complexity

### **Approaches**

* **Single-threaded:** Sequential execution within one thread
* **Multithreaded:** Parallel execution using `threading` and `ThreadPoolExecutor`

### **Technical Specifications**

* **Language:** Python
* **Libraries:** `threading`, `concurrent.futures`, `time`, `random`
* **Thread Configuration:**

  * Up to 4 threads for Linear Search
  * Recursive threading for Merge Sort

---

## 🧩 4. Experimental Setup

### **Hardware Environment**

* **Processor:** Intel Core i7, 6th Generation
* **RAM:** 16 GB
* **Operating System:** Windows 11 (64-bit)

### **Test Parameters**

* **Array Sizes:** 1,000 · 10,000 · 100,000 elements
* **Data Generation:** Random integers between 1 and *(size × 10)*
* **Target Selection:** Middle element of each array
* **Performance Metric:** Execution time (seconds)

---

## 📊 5. Results and Analysis

### **Performance Comparison Table**

| Size    | Algorithm            | Time (s) | Speedup |
| ------- | -------------------- | -------- | ------- |
| 1,000   | Linear Search Single | 0.000000 | 1.00x   |
| 1,000   | Linear Search Multi  | 0.001333 | 0.00x   |
| 1,000   | Merge Sort Single    | 0.004875 | 1.00x   |
| 1,000   | Merge Sort Multi     | 0.022669 | 0.22x   |
| 10,000  | Linear Search Single | 0.000000 | 1.00x   |
| 10,000  | Linear Search Multi  | 0.010421 | 0.00x   |
| 10,000  | Merge Sort Single    | 0.050269 | 1.00x   |
| 10,000  | Merge Sort Multi     | 0.047591 | 1.06x   |
| 100,000 | Linear Search Single | 0.005257 | 1.00x   |
| 100,000 | Linear Search Multi  | 0.008247 | 0.64x   |
| 100,000 | Merge Sort Single    | 0.770902 | 1.00x   |
| 100,000 | Merge Sort Multi     | 0.681747 | 1.13x   |

---

### 🔍 Key Observations

#### **Linear Search Performance**

* **Small arrays (1,000):** Multithreading introduced overhead (0.001333s vs 0.000000s)
* **Medium arrays (10,000):** Single-threaded remained superior (0.000000s vs 0.010421s)
* **Large arrays (100,000):** Single-threaded maintained advantage (0.005257s vs 0.008247s)

#### **Merge Sort Performance**

* **Small arrays (1,000):** Multithreading was 4.5× slower due to thread management overhead
* **Medium arrays (10,000):** Slight performance gain (1.06× speedup)
* **Large arrays (100,000):** Noticeable performance benefit (1.13× speedup)

---

## 🧠 6. Discussion

### **Thread Overhead vs Computational Gain**

For small datasets, thread management overhead outweighs the benefits.
As dataset size grows, computational work becomes substantial enough to justify threading costs.

### **Python GIL Limitations**

Multithreaded Linear Search shows minimal benefit due to the **GIL**, which restricts true parallel CPU execution.
Threads compete for interpreter control, negating potential performance gains.

### **Algorithm-Specific Behavior**

**Merge Sort** benefits more from multithreading due to its divide-and-conquer design —
independent subarrays allow partial parallelism with minimal contention.

---

## 🏁 7. Conclusion

The effectiveness of **multithreading in Python** for CPU-bound tasks depends on several factors:

1. **Algorithm Characteristics** – Divide-and-conquer algorithms (e.g., Merge Sort) benefit most.
2. **Data Size** – Gains appear for larger datasets (≥10,000 elements).
3. **Python’s GIL Impact** – Limits benefits for CPU-bound, non-I/O tasks.
4. **Optimal Use Cases:**

   * Large-scale sorting (100,000+ elements)
   * Algorithms with natural parallelism
   * Mixed workloads with I/O operations

> ⚠️ For smaller datasets or simple sequential algorithms, **single-threaded implementations remain more efficient** due to reduced overhead and GIL constraints.




