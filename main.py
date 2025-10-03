import threading
import time
import random
import concurrent.futures

class MultithreadedAlgorithms:
    def __init__(self, data):
        self.data = data.copy()
        self.original_data = data.copy()
    
    def linear_search_single(self, target):
        for i, value in enumerate(self.data):
            if value == target:
                return i
        return -1
    
    def linear_search_multi(self, target, num_threads=4):
        chunk_size = len(self.data) // num_threads
        results = [-1] * num_threads
        threads = []
        
        def search_chunk(chunk_idx, start, end):
            for i in range(start, end):
                if self.data[i] == target:
                    results[chunk_idx] = i
                    return
        
        for i in range(num_threads):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i != num_threads - 1 else len(self.data)
            thread = threading.Thread(target=search_chunk, args=(i, start, end))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        for result in results:
            if result != -1:
                return result
        return -1
    
    def merge_sort_single(self, arr=None):
        if arr is None:
            arr = self.data
        
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort_single(arr[:mid])
        right = self.merge_sort_single(arr[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
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
    
    def merge_sort_multi(self, arr=None, max_threads=4):
        if arr is None:
            arr = self.data
        
        if len(arr) <= 1:
            return arr
        
        if max_threads <= 1 or len(arr) < 1000:
            return self.merge_sort_single(arr)
        
        mid = len(arr) // 2
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_left = executor.submit(self.merge_sort_multi, arr[:mid], max_threads//2)
            future_right = executor.submit(self.merge_sort_multi, arr[mid:], max_threads//2)
            
            left = future_left.result()
            right = future_right.result()
        
        return self.merge(left, right)
    
    def reset_data(self):
        self.data = self.original_data.copy()

def generate_data(size):
    return [random.randint(1, size * 10) for _ in range(size)]

def performance_test():
    sizes = [1000, 10000, 100000]
    algorithms = MultithreadedAlgorithms([])
    
    print("Performance Comparison:")
    print("=" * 80)
    print(f"{'Size':<10} {'Algorithm':<25} {'Time (s)':<15} {'Speedup':<10}")
    print("-" * 80)
    
    for size in sizes:
        data = generate_data(size)
        algorithms.data = data.copy()
        algorithms.original_data = data.copy()
        
        target = data[size // 2]  # Search for middle element
        
        # Linear Search Comparison
        start_time = time.time()
        algorithms.linear_search_single(target)
        single_search_time = time.time() - start_time
        
        start_time = time.time()
        algorithms.linear_search_multi(target)
        multi_search_time = time.time() - start_time
        
        if multi_search_time == 0:
            search_speedup = float('inf')
        else:
            search_speedup = single_search_time / multi_search_time
        
        # Merge Sort Comparison
        start_time = time.time()
        algorithms.merge_sort_single()
        single_sort_time = time.time() - start_time
        algorithms.reset_data()
        
        start_time = time.time()
        algorithms.merge_sort_multi()
        multi_sort_time = time.time() - start_time
        algorithms.reset_data()
        
        if multi_sort_time == 0:
            sort_speedup = float('inf')
        else:
            sort_speedup = single_sort_time / multi_sort_time
        
        print(f"{size:<10} {'Linear Search Single':<25} {single_search_time:<15.6f} {'1.00x':<10}")
        if search_speedup == float('inf'):
            print(f"{size:<10} {'Linear Search Multi':<25} {multi_search_time:<15.6f} {'∞x':<10}")
        else:
            print(f"{size:<10} {'Linear Search Multi':<25} {multi_search_time:<15.6f} {search_speedup:.2f}x")
        
        print(f"{size:<10} {'Merge Sort Single':<25} {single_sort_time:<15.6f} {'1.00x':<10}")
        if sort_speedup == float('inf'):
            print(f"{size:<10} {'Merge Sort Multi':<25} {multi_sort_time:<15.6f} {'∞x':<10}")
        else:
            print(f"{size:<10} {'Merge Sort Multi':<25} {multi_sort_time:<15.6f} {sort_speedup:.2f}x")
        print("-" * 80)

if __name__ == "__main__":
    performance_test()