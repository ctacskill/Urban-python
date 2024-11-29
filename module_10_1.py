from time import sleep
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for num in range(1, word_count + 1):
            f.write(f'Какое-то слово № {num}\n')
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")

start_time = datetime.now()
for num, i in [(10, 1), (30, 2), (200, 3), (100, 4)]:
    write_words(num, f'example{i}.txt')
end_time = datetime.now()
delta_time = end_time - start_time
print(f'Работа потоков {delta_time}')

thread1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = Thread(target=write_words, args=(100, 'example8.txt'))

start_time = datetime.now()
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
end_time = datetime.now()
delta_time = end_time - start_time

print(f'Работа потоков {delta_time}')

