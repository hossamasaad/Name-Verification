import joblib
import random
import pandas as pd

class DataGenerator:
    """
    Class to Generate correct and wrong data 
    """
    def __init__(self, data) -> None:
        """
        Construct the data generator
        Args:
            data: data I will generate the data from
        """
        self.data = data
        self.male_names   = list(data[data['Gender'] == 'M']['Name'])
        self.female_names = list(data[data['Gender'] == 'F']['Name'])
        self.names = self.male_names + self.female_names
        self.mf_names = joblib.load("/home/hossamasaad/Desktop/Workspace/Digified-Task/data/processed/fm_names.pkl")

    def generate_real_data(self, n):
        """
        Genertate n real data

        Args:
            n: length of the data
        
        Returns
            real_data: generated data ['name', 'correct']
        """
        names = []

        for i in range(n):
            a = random.randint(0, len(self.names     ) - 1)
            b = random.randint(0, len(self.male_names) - 1)
            c = random.randint(0, len(self.male_names) - 1)

            a, b, c = self.names[a], self.male_names[b], self.male_names[c]
            name = a + ' ' + b + ' ' + c
            names.append(name)
        
        real_data = pd.DataFrame({
            'name': names,
            'correct': [1] * len(names)
        })

        return real_data

    def generate_wrong_names_data(self, n):
        """
        Genertate n not correct names

        Args:
            n: length of the data
        
        Returns
            fake_data: generated data ['name', 'correct']
        """
        names = []
        alpha = 'ةأابتثجحخدذرزسشصضطظعغفقكلمنهويى'

        # Generate Wrong names
        for i in range(int(n * 0.5)):

            # Generate random real names
            a = random.randint(0, len(self.names     ) - 1)
            b = random.randint(0, len(self.male_names) - 1)
            c = random.randint(0, len(self.male_names) - 1)

            a, b, c = self.names[a], self.male_names[b], self.male_names[c]
            
            # update some random char from the real name with some random chars
            a1 = random.randint(0, len(alpha) - 1)
            b1 = random.randint(0, len(alpha) - 1)
            c1 = random.randint(0, len(alpha) - 1)

            a2 = random.randint(0, len(a) - 1)
            b2 = random.randint(0, len(b) - 1)
            c2 = random.randint(0, len(c) - 1)

            a = a[:a2] + alpha[a1] + a[a2+1:]
            b = b[:b2] + alpha[b1] + b[b2+1:]
            c = c[:c2] + alpha[c1] + c[c2+1:]
            
            name = a + ' ' + b + ' ' + c
            names.append(name)
        
        # wrong names: name + female + female 
        for i in range(int(n * 0.1)):
            a = random.randint(0, len(self.names     ) - 1)
            b = random.randint(0, len(self.female_names) - 1)
            c = random.randint(0, len(self.female_names) - 1)

            # handle the case the name can be male or female
            while self.female_names[b] in self.mf_names:
                b = random.randint(0, len(self.female_names) - 1)

            # handle the case the name can be male or female
            while self.female_names[c] in self.mf_names:
                c = random.randint(0, len(self.female_names) - 1)

            a, b, c = self.names[a], self.female_names[b], self.female_names[c]
            name = a + ' ' + b + ' ' + c
            names.append(name)

        # wrong names: name + female + male 
        for i in range(int(n * 0.2)):
            a = random.randint(0, len(self.names     ) - 1)
            b = random.randint(0, len(self.female_names) - 1)
            c = random.randint(0, len(self.male_names) - 1)

            # handle the case the name can be male or female
            while self.female_names[b] in self.mf_names:
                b = random.randint(0, len(self.female_names) - 1)

            a, b, c = self.names[a], self.female_names[b], self.male_names[c]
            name = a + ' ' + b + ' ' + c
            names.append(name)
        
        # wrong names: name + male + female
        for i in range(int(n * 0.2)):
            a = random.randint(0, len(self.names     ) - 1)
            b = random.randint(0, len(self.male_names) - 1)
            c = random.randint(0, len(self.female_names) - 1)

            # handle the case the name can be male or female
            while self.female_names[c] in self.mf_names:
                c = random.randint(0, len(self.female_names) - 1)

            a, b, c = self.names[a], self.male_names[b], self.female_names[c]
            name = a + ' ' + b + ' ' + c
            names.append(name)

        # Create the data frame
        wrong_data = pd.DataFrame({
            'name': names,
            'correct': [0] * len(names)
        })

        return wrong_data