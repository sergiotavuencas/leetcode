import time
import tracemalloc
import threading

class TimeoutException(Exception):
    pass

class Performance:
    @staticmethod
    def measure(func, *args, timeout=None, **kwargs):
        result_container = {}

        def target():
            result_container['start'] = time.perf_counter()
            result_container['result'] = func(*args, **kwargs)
            result_container['end'] = time.perf_counter()

        tracemalloc.start()

        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        class_name = func.__self__.__class__.__name__ if hasattr(func, '__self__') and func.__self__ else 'N/A'

        if thread.is_alive():
            print(f"Class: {class_name}")
            print(f"Method: {func.__name__}")
            print(f"  ⚠️ Timeout after {timeout}s")
            print(f"  Peak memory usage before timeout: {peak / 1024:.4f} KB\n")
            return

        exec_time = (result_container['end'] - result_container['start']) * 1000

        print(f"Class: {class_name}")
        print(f"Method: {func.__name__}")
        print(f"  Result: {result_container['result']}")
        print(f"  Execution time: {exec_time:.4f} ms")
        print(f"  Peak memory usage: {peak / 1024:.4f} KB\n")
