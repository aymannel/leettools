import time

def timeit(func):
    def wrapper(*args, **kwargs):
        runtime = list()
        iterations = 0
        loop_start = time.time()
        loop_end = loop_start

        while (loop_end - loop_start) < 0.001:
            start = time.time()
            result = func(*args, **kwargs)
            stop = time.time()
            runtime.append(stop - start)
            
            iterations += 1
            loop_end = time.time()

        print(result)
        min_time = '{:.8e}'.format(float(min(runtime)))
        mean_time = '{:.4e}'.format(float(sum(runtime) / iterations))
        print(f'{func.__name__} ran {iterations} times | mean time = {mean_time} s | min time = {min_time} s')
    return wrapper
