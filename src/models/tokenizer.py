class Tokenizer:
    """
    Create Tokenizer to convert text names to sequence of numbers
    """
    def __init__(self) -> None:
        self.max_len = 0
        self.map = {'أ' : 1, 'ا' : 1, 'إ' : 1,  'آ' : 1,
                    'ب' : 2,
                    'ت' : 3,
                    'ث' : 4, 
                    'ج' : 5, 
                    'ح' : 6, 
                    'خ' : 7, 
                    'د' : 8, 
                    'ذ' : 9, 
                    'ر' : 10, 
                    'ز' : 11,
                    'س' : 12,
                    'ش' : 13,
                    'ص' : 14,
                    'ض' : 15,
                    'ط' : 16,
                    'ظ' : 17, 
                    'ع' : 18,
                    'غ' : 19, 
                    'ك' : 20, 
                    'ف' : 21, 
                    'ق' : 22, 
                    'ل' : 23,
                    'م' : 24,
                    'ن' : 25, 
                    'ه' : 26, 
                    'و' : 27, 
                    'ي' : 28, 'ى' : 28,
                    'ة' : 29, 
                    'ء' : 30, 'ئ' : 30, 'ؤ' : 30,
                    '-' : 31,
                    ' ' : 32}


    def texts_to_sequences(self, names):
        """
        Convert every char in names to number

        Args:
            names: names to be converted to sequence of numbers
        
        Return:
            Sequences: Sequence of numbers represent names
        """
        sequences = []
        for sen in names:
            seq = []
            for char in sen:
                seq.append(self.map[char])

            sequences.append(seq)
            self.max_len = max(self.max_len, len(seq))
        return sequences
    
    def sequences_to_text(self, sequences):
        """
        Convert every number in sequences to char

        Args:
            Sequences: Sequences to be converted back to names
        
        Return:
            names: names that the sequences represent
        """

        # reverse map
        seq_map = {}
        for key, val in self.map.items():
            seq_map[val] = key

        seq_map[0], seq_map[1], seq_map[30] = '', 'ا', 'ء'

        names = []
        for seq in sequences:
            name = []
            for num in seq:
                name.append(seq_map[num])

            names.append("".join(name))

        return names

    def get_max_len(self):
        """
        Get the longest name length

        Return:
            max_len: longest name length
        """
        return self.max_len


    def pad_sequences(self, sequences, max_len):
        """
        Pad sequences to the longest length

        Args:
            sequences: sequences to pad
            max_len: longest length to pad names to it

        Returns:
            sequences: padded sequences
        """
        for i in range(len(sequences)):
            while len(sequences[i]) < max_len:
                sequences[i].append(0)
            
            while len(sequences[i]) > max_len:
                del sequences[i][-1]
    
        return sequences