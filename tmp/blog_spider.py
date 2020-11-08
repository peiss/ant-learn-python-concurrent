import requests

urls = [
    f"http://www.crazyant.net/page/{idx}"
    for idx in range(1, 10 + 1)
]


def craw(url):
    r = requests.get(url)
    print(url, len(r.text))


if __name__ == "__main__":
    print(urls)
    craw(urls[0])
