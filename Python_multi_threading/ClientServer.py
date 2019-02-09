import requests


def main():
    client_request = requests.get("http://172.0.0.1:8080")
    print(client_request.headers)


if __name__ == '__main__':
    main()

