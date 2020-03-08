import pytest

from stopwords import StopWordList


@pytest.fixture(scope = "class")
def array():
    return ["un", "deux"]

@pytest.fixture(scope = "class")
def _stopwords():
    return StopWordList("",["un", "deux"])

class Test_StopWordList():
    
    def test_extend_size(self, _stopwords):
        print(type(_stopwords))
        assert len(_stopwords.stop_words) == 2


    def test_extend_un(self, _stopwords):
        assert "un" in _stopwords.stop_words

        
    def test_extend_deux(self, array, _stopwords):
        for i in range(len(_stopwords.stop_words)):
            assert (array[i] in _stopwords.stop_words) == True
            
    @pytest.mark.parametrize("test_input,expected", [("un", True), ("deux", True), ("trois", False)])
    def test_extend_trois(self, test_input, expected, _stopwords):
        assert (test_input in _stopwords.stop_words) == expected
    
    def test_add_language(self):
        _stopwords_en = StopWordList("english")
        _stopwords2 = StopWordList("")
        assert "a" in _stopwords_en.stop_words
        assert "found" in _stopwords_en.stop_words
        assert len(_stopwords2.stop_words) == 0