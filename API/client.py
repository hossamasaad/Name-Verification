import requests


def main():

    name = input('Enter an arabic name or enter to skip: ')

    while name:
        data = {"name": name}

        r = requests.post(
            'http://0.0.0.0:8000/is_real_name/',
             json = data
        )

        print(r.text)
        name = input('Enter an arabic name or enter to skip: ')

if __name__ == '__main__':
    main()