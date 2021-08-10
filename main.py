import requests


def get_api_key(filename='key'):
    with open(filename) as key:
        return key.read()


class nameOfClass():

    def __init__(self):
        self.api_key = get_api_key()

    def capabilities(self):
        return requests.get(url=(f"https://api.similarweb.com/capabilities?"
                                 f"api_key={self.api_key}"))

    def lead_gen(self):
        return requests.get(url=(f"https://api.similarweb.com/v1/website/"
                                 f"bbc.co.uk/lead-enrichment/all?api_key="
                                 f"{self.api_key}&start_date=2019-01&"
                                 f"end_date=2019-09&country=us&"
                                 f"main_domain_only=false&format=json&"
                                 f"show_verified=false"))


print(nameOfClass().capabilities())
