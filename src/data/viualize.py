import seaborn as sns
import matplotlib.pyplot as plt

class Visualizer:
    """
    A class contains some methods to make some visualization
    """

    def __init__(self, data) -> None:
        """
        Construct the visualizer
        Args:
            data: data to visualize it
        """
        self.data = data
    

    def show_gender_counts(self, save_fig = None):
        """
        Show bar plot to show langauge counts
        Args:
            save_fig: path to save fig 
        """
        plt.figure(figsize=(8, 8))
        sns.countplot(x = 'Gender', data= self.data, order= self.data['Gender'].value_counts().index, palette= 'pastel')
        plt.title('Gender Counts', fontsize=24)
        plt.xlabel("Gender",fontsize=20)
        plt.ylabel("Count", fontsize=20)
        plt.xticks(size= 18)

        if save_fig:
            plt.savefig('../reports/figures/{}.png'.format(save_fig))
        
        plt.show()

    def show_percentage(self, save_fig = None):
        """
        Show pie plot to show gender percentages
        Args:
            save_fig: path to save fig 
        """
        plt.figure(figsize=(8, 8))
        language= self.data['Gender'].value_counts().reset_index()
        
        plt.pie(language['Gender'],
                labels = language['index'],
                autopct='%.1f%%',
                textprops={'fontsize': 14},
                colors=sns.color_palette('pastel'))
            
        if save_fig:
            plt.savefig('../reports/figures/{}.png'.format(save_fig))
            
        plt.show()