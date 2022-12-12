import pytest
import pandas as pd

class TestExplorer:

    def test_get_duplicated_rows(self, explorer):
        assert len(explorer.get_duplicated_rows()) == 1
        assert explorer.get_duplicated_rows()['Name'].iloc[0] == 'ابتسام'

    def test_get_duplicate_names(self, explorer):
        assert len(explorer.get_duplicate_names()) == 4
        assert explorer.get_duplicate_names()['Name'  ].iloc[0] == 'ابتسام'
        assert explorer.get_duplicate_names()['Gender'].iloc[0] == 'F'
        assert explorer.get_duplicate_names()['Name'  ].iloc[2] == 'ضياء'
        assert explorer.get_duplicate_names()['Gender'].iloc[2] == 'F'
        assert explorer.get_duplicate_names()['Gender'].iloc[3] == 'M'

    def test_get_gender_counts(self, explorer):
        assert explorer.get_gender_counts()['M'] == 3
        assert explorer.get_gender_counts()['F'] == 5

    def test_get_double_names(self, explorer):
        assert len(explorer.get_double_names()) == 1
        assert explorer.get_double_names()['Name'].iloc[0] == 'أم كلثوم'


class TestGenerateData:

    def test_generate_real_data(self, generator):
        assert len(generator.generate_real_data(0)) == 0
        assert len(generator.generate_real_data(20)) == 20
        assert len(generator.generate_real_data(50)) == 50
        assert len(generator.generate_real_data(2)['name'].iloc[0].split()) == 3
        assert generator.generate_real_data(2)['correct'].iloc[0] == 1
        
    def test_generate_wrong_names_data(self, generator):
        assert len(generator.generate_wrong_names_data(0)) == 0
        assert len(generator.generate_wrong_names_data(20)) == 20
        assert len(generator.generate_wrong_names_data(50)) == 50
        assert len(generator.generate_wrong_names_data(2)['name'].iloc[0].split()) == 3
        assert generator.generate_wrong_names_data(2)['correct'].iloc[0] == 0


class TestPreprocess:

    def test_combine_data(self, preprocessor):
        d1 = pd.DataFrame({
            'name':['حسام'],
            'gender':['M']
        })

        d2 = pd.DataFrame({
            'name':['داليا'],
            'gender':['F']
        })

        data = pd.DataFrame({
            'name':['حسام', 'داليا'],
            'gender':['M', 'F']
        })

        assert len(preprocessor.combine_data([d1, d2])) == len(data)
        assert all(preprocessor.combine_data([d1, d2])['name'] == data['name'])
        assert all(preprocessor.combine_data([d1, d2])['gender'] == data['gender'])

    def test_delete_duplicated_raws(self, preprocessor):
        d1 = pd.DataFrame({
            'name':['حسام', 'حسام', 'داليا', 'داليا'],
            'gender':['M','M','F','F']
        })

        d2 = pd.DataFrame({
            'name':['حسام', 'داليا'],
            'gender':['M','F']
        })

        assert len(preprocessor.delete_duplicated_raws(d1)) == 2
        assert any(preprocessor.delete_duplicated_raws(d1) == d2)

    def test_handle_double_names(self, preprocessor):
        d1 = pd.DataFrame({
            'Name':['أم كلثوم', 'نجم الدين'],
            'gender':['F','M']
        })

        d2 = pd.DataFrame({
            'Name':['أم-كلثوم', 'نجم-الدين'],
            'gender':['F','M']
        })

        assert any(preprocessor.handle_double_names(d1) == d2)
        assert any(preprocessor.handle_double_names(d1) == d2)
        assert preprocessor.handle_double_names(d1)['Name'].iloc[0] == 'أم-كلثوم'
        assert preprocessor.handle_double_names(d1)['Name'].iloc[1] == 'نجم-الدين'


        