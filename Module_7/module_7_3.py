class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for names in self.file_names:
            with open(names, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for punct in ",.=!?;:-":
                    text = text.replace(punct, '')
                words = text.split()
                all_words[names] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        positions = {}
        for name, words in all_words.items():
            if word in words:
                positions[name] = words.index(word) + 1
        return positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        count_words = {}
        for name, words in all_words.items():
            count_words[name] = words.count(word)
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
