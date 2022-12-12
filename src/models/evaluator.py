import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from tqdm import tqdm
from tensorflow.math import confusion_matrix
from sklearn.metrics import classification_report

from src.models.tokenizer import Tokenizer

class Evaluator:
    """
    Create an Evaluator to get metrics, plots and missclassified data
    """

    def __init__(self, model, history, padded, labels):
        """
        Construct the evaluator

        Args:
            model  : model to make prediction
            history: model history
            padded : padded sequences to use it in evaluation
            labelse: sequences labels
        """

        self.model = model
        self.history = history
        self.padded = padded
        self.labels = list(labels)
        
        # prediction
        self.y_pred = self.model.predict(padded)
        self.y_pred = [1 if x > 0.5 else 0 for x in  self.y_pred]


    def metrics_report(self):
        """
        Get some metrics accuracy, recall, percision and f1-score 
        """
        return classification_report(self.labels, self.y_pred)


    def get_missclassified_examples(self):
        """
        Get the missclassified examples and convert it back to names
        
        Returns:
            names: list of missclassified names
        """
        indices = [i for i in tqdm(range(len(self.y_pred))) if self.y_pred[i] != self.labels[i]]
        subset_of_wrongly_predicted = [self.padded[i] for i in indices]
        names = Tokenizer().sequences_to_text(subset_of_wrongly_predicted)
        return names
    

    def accuracy(self, save_fig = None):
        """
        Plot accuracy graph
        Args:
            save_fig: path to save fig 
        """

        plt.plot(self.history.history['accuracy'])
        plt.plot(self.history.history['val_accuracy'])
        plt.xlabel("Epochs")
        plt.ylabel('Accuracy')
        plt.legend(['accuracy', 'val_accuracy'])
        if save_fig:
            plt.savefig('../reports/figures/{}.png'.format(save_fig))
        
        plt.show()
    

    def loss(self, save_fig = None):
        """
        Plot loss graph
        Args:
            save_fig: path to save fig 
        """
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.xlabel("Epochs")
        plt.ylabel('Loss')
        plt.legend(['loss', 'val_loss'])
        if save_fig:
            plt.savefig('../reports/figures/{}.png'.format(save_fig))
        
        plt.show()
   

    def confusion_matrix(self, save_fig=None):
        """
        Show the confusion matrix
        
        Args:
            save_fig: path to save fig 
        """

        cm = confusion_matrix(self.labels, self.y_pred)                     # confusion matrix
        l = ['Real', 'Not real']

        # plot confusion matrix
        plt.figure(figsize=(8,8))
        sns.heatmap(cm, annot = True, fmt='g')
        loc = np.array(range(2)) +.5
        plt.xticks(loc, l)
        plt.yticks(loc, l)

        if save_fig:
            plt.savefig('../reports/figures/{}.png'.format(save_fig))
        
        plt.show()