import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            all_data.append(line)
            if not line:
                break


files = [f'./file {number}.txt' for number in range(1,5)]
# start_time = time.time()
#
# for file in files:
#     read_info(file)
#
# end_time = time.time()
# execution_time = end_time - start_time
# print(f'{execution_time} (линейный)')



if __name__ == '__main__':
    start_time = time.time()
    with Pool(4) as pool:
        result = pool.map(read_info, files)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f'{execution_time} (многопроцессорный)')