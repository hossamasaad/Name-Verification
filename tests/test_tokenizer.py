import pytest

class TestTokenizer:

    def test_texts_to_sequences(self, tokenizer):
        sentences = ['حسام أسعد رجب', 'محمد خالد هاني']
        sequences = [[6, 12, 1, 24, 32, 1, 12, 18, 8, 32, 10, 5, 2],
                     [24, 6, 24, 8, 32, 7, 1, 23, 8, 32, 26, 1, 25, 28]]

        assert tokenizer.texts_to_sequences(sentences) == sequences
    
    def test_pad_sequences(self, tokenizer):
        sequences = [[6, 12, 1, 24, 32, 1, 12, 18, 8, 32, 10, 5, 2],
                     [24, 6, 24, 8, 32, 7, 1, 23, 8, 32, 26, 1, 25, 28]]

        padded   = [[6, 12, 1, 24, 32, 1, 12, 18, 8, 32, 10, 5, 2, 0, 0, 0, 0, 0, 0, 0],
                    [24, 6, 24, 8, 32, 7, 1, 23, 8, 32, 26, 1, 25, 28, 0, 0, 0, 0, 0, 0]]
        
        assert tokenizer.pad_sequences(sequences, 20) == padded

    def test_sequences_to_text(self, tokenizer):
        padded   = [[6, 12, 1, 24, 32, 1, 12, 18, 8, 32, 10, 5, 2, 0, 0, 0, 0, 0, 0, 0],
                    [24, 6, 24, 8, 32, 7, 1, 23, 8, 32, 26, 1, 25, 28, 0, 0, 0, 0, 0, 0]]
        
        sentences = ['حسام اسعد رجب', 'محمد خالد هانى']

        assert tokenizer.sequences_to_text(padded) == sentences