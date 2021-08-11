import requests
import json

def get_api_key(filename="key"):
    with open(filename) as key:
        return key.read()


def get_url(filename="url"):
    with open(filename) as urlList:
        return [url.strip() for url in urlList.readlines()]


class simpull:
    def __init__(self):
        self.api_key = get_api_key()

    def capabilities(self):
        return requests.get(
            url=(f"https://api.similarweb.com/capabilities?" f"api_key={self.api_key}")
        )

    def lead_gen(self, url, start_date="2020-08", end_date="2021-07", country="world"):
        return requests.get(
            url=(
                f"https://api.similarweb.com/v1/website/"
                f"{url}/lead-enrichment/all?api_key="
                f"{self.api_key}&start_date={start_date}&"
                f"end_date={end_date}&country={country}&"
                f"main_domain_only=false&format=json&"
                f"show_verified=false"
            )
        )


print(get_url())

# #### WORKING DOWNLOADER #####
for each in get_url():
    with open(f'{each}.json', 'w') as outfile:
        json.dump(simpull().lead_gen(each).json(), outfile, indent=4)
# #############################
