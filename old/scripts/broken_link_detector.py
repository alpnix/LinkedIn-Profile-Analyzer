import requests

# Author: Sky Luo
# March 15, 2024


def check_link(url):
    try:
        response = requests.head(url=url, allow_redirects=True)
        if response.status_code == 200:
            print(response.status_code)
            return True
        else:
            print(response.status_code)
            return False
    except requests.RequestException as e:
        print(e)
        return False


if __name__ == "__main__":
    print(check_link("https://www.apple.com"))
