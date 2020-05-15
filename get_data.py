import requests
import json


def get_covid_data():
    source_url = "https://api.covid19india.org/raw_data4.json"
    res = requests.get(source_url)
    try:
        if res.status_code == 200:
            json_res = json.loads(res.content)
            return json_res
        else:
            print("Error")
    except requests.exceptions.RequestException as e:
        print(e)


def get_sources():
    data = get_covid_data()
    all_sources = []
    if data:
        raw_data = data["raw_data"]
        for data in raw_data:
            sources = {}
            if data["source1"]:
                sources.update({"source1": data["source1"]})
            elif data["source2"]:
                sources.update({"source2": data["source2"]})
            elif data["source3"]:
                sources.update({"source3": data["source3"]})
            all_sources.append(sources)
    return all_sources
