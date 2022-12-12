import pandas as pd

class Preprocess:
    """
    A class contains some methods to facilitate some preprocessing steps
    """
    def __init__(self) -> None:
        pass

    def load_txt_data(self, data_path: str, gender: str):
        """
        Load data from txt file and create the dataframe

        Args:
            data_paths: path of txt file
            gender: gender of the names in file
        Returns
            data: dataframe created from txt file
        """
        names = []
        with open(data_path) as f:
            names = f.read().splitlines()
        
        genders = [str(gender)] * len(names)
        data = pd.DataFrame({
            'Name':names,
            'Gender':genders
        })

        return data
    
    def combine_data(self, data: list):
        """
        Combine dataframes together

        Args:
            data: list of dataframes to combine
        
        Returns:
            combined data frame
        """
        return pd.concat(data).reset_index(drop=True)
    

    def delete_duplicated_raws(self, data):
        """
        Delete duplicated row from the data

        Args:
            data: dataframe to delete duplicate rows from it
        
        Returns:
            unique rows dataframe
        """
        return data.drop(data[data.duplicated()].index, axis=0).reset_index(drop=True)
    
    def handle_double_names(self, data):
        """
        Handle double names to deal as one name

        Args:
            data: data to handel its values

        Returns:
            data: data after handling double names
        """
        data = data[ data['Name'] != 'سعيدة بضم السين' ].reset_index(drop=True)
        data['Name'] = data['Name'].map(lambda x: x.replace(" ", "-") if len(x.split()) > 1 else x)
        return data