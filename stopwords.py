
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

class StopWordList:
    """
        list of stopwords and operations
    """
    
    def __init__(self, language = "", word_list = [], file = None):
        self.stop_words = []
        self.add_language(language)
        self.extend(word_list)
        self.import_file(file)
    
    def extend(self, word_list):
        if type(word_list) in (frozenset, list, set):
            self.stop_words.extend(word_list)
        else:
            print(f"WARNING: word_list: {word_list} is not a list")
            print(f"type: {type(word_list)}")
        self.rationalize()
        
    def add_language(self, language = "english"):
        if language == "english":
            self.extend(ENGLISH_STOP_WORDS)
        else:
            print(f"WARNING: language '{language}' not yet implemented")

    def import_file(self, file_path ):
        if file_path is None or file_path == "":
            print("WARNING: no file path given")
        else:
            try:
                with open(file_path, "r") as file_stop_words:
                    words = file_stop_words.readlines()
                    words = [ word.rstrip() for word in words]
                    self.extend(words)
            except Exception as err:
                print(err)
                    
    def rationalize(self):
        self.stop_words = list(set(self.stop_words))
        self.drop_word('')
        return self.stop_words

    def drop_word(self, word):
        if word in self.stop_words:
            self.stop_words.remove(word)

    def drop_word_list(self, word_list):
        for word in word_list:
            self.drop_word(word)


    def print(self):
        print(self.stop_words)