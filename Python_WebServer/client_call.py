import requests


def main():
    client_r = requests.get("http://127.0.0.1:8080")
    print(client_r.text)
    print(client_r.headers)


if __name__ == '__main__':
    main()

