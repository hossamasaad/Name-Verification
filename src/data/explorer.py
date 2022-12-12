import pandas as pd

class Explorer:
    """
    Create Explorer to explore and get familiar with data
    """
    def __init__(self, data) -> None:
        """
        Construct the explorer

        Args:
            data: data to be explored
        """
        self.data = data
    

    def get_duplicated_rows(self):
        """
        Get duplicated rows in the data
        """
        return self.data[self.data.duplicated() == True]


    def get_duplicate_names(self):
        """
        Get duplicated names in the date
        """
        return self.data[self.data['Name'].duplicated(keep=False) == True]
    

    def get_gender_counts(self):
        """
        Get each gender count
        """
        return self.data['Gender'].value_counts()
    
    def get_double_names(self):
        """
        Get the names that are considered male or female names
        """
        names = []
        gender = []

        for i in range(len(self.data)):
            if len(self.data['Name'][i].split()) > 1:
                names.append(self.data['Name'][i])
                gender.append(self.data['Gender'][i])

        return pd.DataFrame({'Name':names,
                            'Gender':gender})
    