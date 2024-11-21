def custom_write(file_name, strings):
    string_positions = {}
    num_str = 1
    for string in strings:
        file = open(file_name, 'a',encoding='utf-8')
        byte_str = (file.tell())
        file.write(string)
        file.write('\n')
        file.close()
        string_positions[(num_str, byte_str)] = string
        num_str += 1
    result = string_positions
    return result

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)