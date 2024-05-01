class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, provided_list):
        anagram_list = list()
        word_list = sorted([letter for letter in self.word])
        for anagram_word in provided_list:
            if sorted([letter for letter in anagram_word]) == word_list:
                anagram_list.append(anagram_word)
        return anagram_list 