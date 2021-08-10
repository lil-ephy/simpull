import requests


def get_api_key(filename='key'):
    with open(filename) as key:
        return key.read()


def get_url(filename='url'):
    with open(filename) as url:
        return list(x.strip() for x in url.readlines())


def get_url2(filename='url'):
    with open(filename) as url:
        x = list(x.strip() for x in url.readlines())
        for each in x:
            yield each


def get_url3(filename='url'):
    with open(filename) as urlList:
        urlList = [each for each in [x.strip() for x in urlList.readlines()]]
        yield urlList


class simpull():

    def __init__(self):
        self.api_key = get_api_key()

    def capabilities(self):
        return requests.get(url=(f"https://api.similarweb.com/capabilities?"
                                 f"api_key={self.api_key}"))

    def lead_gen(self, start_date='2020-08', end_date='2021-07',
                 country='world', url=get_url):
        return requests.get(url=(f"https://api.similarweb.com/v1/website/"
                                 f"bbc.co.uk/lead-enrichment/all?api_key="
                                 f"{self.api_key}&start_date={start_date}&"
                                 f"end_date={end_date}&country={country}&"
                                 f"main_domain_only=false&format=json&"
                                 f"show_verified=false"))


print(get_url3())

for i in get_url3():
    print(i)

# for k, v in enumerate(get_url()):
#     print(simpull.lead_gen())

# print(get_url())
# print(nameOfClass().capabilities().text)
