from itertools import count


class WordsFinder:
    def __init__(self, *args):
        self.file_name = args

    def __repr__(self):
        return self.file_name

    def get_all_words(self):
        all_words = {}
        for file in self.file_name:
            with open(file, 'r', encoding='utf-8') as f:
                lines = []
                for line in f:
                    lines.append(line)
            changed_lines = []
            for line in lines:
                import string
                line = line.lower()
                line = line.translate(str.maketrans('', '', string.punctuation))
                line = line.split()
                changed_lines.append(line)
            all_words_list = []
            for element in changed_lines:
                for word in element:
                    all_words_list.append(word)
            all_words[file] = all_words_list

        return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            counter = 0
            for word_ in words:
                counter += 1
                if word.lower() == word_:
                    find_dict[name] = counter
                    break
        return find_dict

    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            counter = 0
            for word_ in words:
                if word.lower() == word_:
                    counter += 1
            count_dict[name] = counter
        return count_dict


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))