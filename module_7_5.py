import os
import time



for root, dirs, files in os.walk('.'):
  for file in files:
    print(file)
    filepath = os.path.join
    filetime = os.path.getmtime
    # formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize
    parent_dir = os.path.dirname
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: , Родительская директория: {parent_dir}')