from src.models.tokenizer import Tokenizer

class Prediction:
    """
    Predicition class used to predict inpu name
    """
    def __init__(self, model) -> None:
        """
        Construct prediction class
        Args:
            model: model used in prediction
        """
        self.model = model
        self.max_len = 31
        self.tokenizer = Tokenizer()

    def predict(self, names):
        """
        Take the names convert it to padded sequences and use model to get prediction
        Args:
            names: names to verify using the model
        """
        sequences = self.tokenizer.texts_to_sequences(names)
        padded = self.tokenizer.pad_sequences(sequences, self.max_len)
        return self.model.predict(padded)
    
    def convert_prediction_0_1(self, y_pred):
        """
        Convert result to 1 or 0 using threshold 0.5
        Args:
            y_pred: prediction to convert
        """
        return [1 if x > 0.5 else 0 for x in y_pred]
    
    def convert_prediction_into_confidence(self, y_pred):
        """
        Convert prediction to confidence
        Args:
            y_pred: prediction to convert
        """
        results = []
        for x in y_pred:
            if x >= 0.9:
                results.append('Real name with high confidence')
            elif x > 0.5 and x < 0.9:
                results.append('Real name with low confidence')
            elif x < 0.5 and x > .0001:
                results.append('Wrong name with low confidence')
            else:
                results.append('Wrong name with high confidence')
        return results