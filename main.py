from calendar import different_locale
import requests
import json
import pandas as pd
import xlsxwriter as xl


def get_things(filename):
    with open(filename, "r") as get_file:
        return (
            get_file.read()
            if filename == "key"
            else [url.strip() for url in get_file.readlines()]
        )


def capabilities():
    return requests.get(
        url=(f"https://api.similarweb.com/capabilities?" f"api_key={get_things('key')}")
    )


def lead_gen(url, start_date="2020-08", end_date="2021-07", country="world"):
    return requests.get(
        url=(
            f"https://api.similarweb.com/v1/website/"
            f"{url}/lead-enrichment/all?api_key="
            f"{get_things('key')}&start_date={start_date}&"
            f"end_date={end_date}&country={country}&"
            f"main_domain_only=false&format=json&"
            f"show_verified=false"
        )
    )


# #### WORKING DOWNLOADER #####
def download_things():
    for each in get_things("url"):
        with open(f"{each}.json", "w") as outfile:
            json.dump(lead_gen(each).json(), outfile, indent=4)
# #############################


# #### JSON READER #####
def do_things(filename, metric):
    with open(f"{filename}.json", "r") as get_file:
        df = json.load(get_file)
        df = pd.json_normalize(df, metric).assign(**df["meta"]["request"])
        return df
# #############################


def metricPls():
    my_list = ['visits', 'pages_per_visit', 'average_visit_duration', 'bounce_rate']
    y = ['main_domain_only', 'show_verified', 'state', 'page', 'format', 'start_date', 'end_date']

    for url in get_things("url"):
        writer = pd.ExcelWriter(f'{url}.xlsx', engine='xlsxwriter')
        for each in my_list:
            x = do_things(url, each).drop(columns=y)
            print(x)
            x.to_excel(writer, sheet_name=each)
        writer.save()


metricPls()
