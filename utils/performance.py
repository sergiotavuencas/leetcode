import time
import tracemalloc

class Performance(object):
    @staticmethod
    def measure(func, *args, **kwargs):
        tracemalloc.start()
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        class_name = func.__self__.__class__.__name__ if hasattr(func, '__self__') and func.__self__ else 'N/A'
        func_name = func.__name__

        print(f"Class: {class_name}")
        print(f"Method: {func_name}")
        print(f"  Result: {result}")
        print(f"  Execution time: {(end - start) * 1000:.4f} ms")
        print(f"  Peak memory usage: {peak / 1024:.4f} KB\n")

