import requests

class TestAPI:
    
    def test_single_names(self, url):
        single_real_names = ['حسام', 'دعاء', 'السيد', 'اسماعيل']
        single_wrong_names = ['هويدا', 'محدر', 'وحيد', 'خالض']

        for name in single_real_names:
            data = {"name": name}

            r = requests.post(
                url,
                json = data
            )

            assert float(r.json()['prediction']) > 0.9
        
        for name in single_wrong_names:
            data = {"name": name}

            r = requests.post(
                url,
                json = data
            )

            assert float(r.json()['prediction']) < 0.1

    def test_double_names(self, url):
        double_real_names = ['حسام أسعد', 'دعاء محمد', 'اسماعيل محمد', 'محمد  اسماعيل', 'ابتسام كريم']
        double_wrong_names = ['هويدا محمد', 'محدر محموي', 'وحيد خالد', 'محمد دعاء', 'كريم ابتسام']

        for name in double_real_names:
            data = {"name": name}

            r = requests.post(
                url,
                json = data
            )

            assert float(r.json()['prediction']) > 0.5
        
        for name in double_wrong_names:
            data = {"name": name}

            r = requests.post(
                url,
                json = data
            )

            assert float(r.json()['prediction']) < 0.1

    def test_triple_names(self, url):
        triple_real_names = ['حسام أسعد رجب', 'دعاء محمد مصطفي', 'اسماعيل محمد هاني', 'ابتسام محمد اسعد','محمد اسماعيل خليل']
        triple_wrong_names = ['هويدا محمد خليل', 'محش سشيدر محموي', 'وحيد خالد محمود', 'خالص هاتن شاكر', 'محمد هاني حنان']

        for name in triple_real_names:
            data = {"name": name}

            r = requests.post(
                url,
                json = data
            )

            assert float(r.json()['prediction']) > 0.5
        
        for name in triple_wrong_names:
            data = {"name": name}

            r = requests.post(
                url,
                json = data
            )

            assert float(r.json()['prediction']) < 0.1