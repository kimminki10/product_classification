from search_engine import laptop_search


def get_laptop_gpu_benchmark():
    benchmark_list = laptop_search.notebook_benchmark()

    for benchmark in benchmark_list:
        print(benchmark)


if __name__=="__main__":
    get_laptop_gpu_benchmark()
    laptop_search.quit_driver()
