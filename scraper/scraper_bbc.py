import re
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup
from webdriver_manager.core.driver_cache import json


def make_request(url: str) -> str:
    with requests.Session() as s:
        page = s.get(url=url)
    return page.text


def process_votes(raw_vote: str) -> int:
    return int(raw_vote.replace(",", ""))


def get_data(page: str):
    data = []
    try:
        soup = BeautifulSoup(page, "html.parser")
        updated_element = (
            soup.find("p", class_="live-results-label__timestamp-line")
            .text.replace("Last updated:", "")
            .strip()
        )
        candidates_table = soup.find("table", class_="candidates-table")
        candidates_images = candidates_table.find_all(
            "img", class_=re.compile(r"profile-picture--")
        )  # more than 4
        candidates_names = candidates_table.find_all(
            "span", class_="hidden-name__text"
        )  # more than 4
        candidates_coalitions = candidates_table.find_all(
            "td", class_="candidates-table__cell candidates-table__coalition"
        )
        candidates_votes = candidates_table.find_all(
            "div", class_=re.compile(r"votes--")
        )
        candidates_percentages = candidates_table.find_all(
            "div", class_="candidates-table__votes-percentage-value"
        )
        candidates_25ptally = candidates_table.find_all(
            "td", class_=re.compile(r"tally--")
        )
        for i in range(4):
            candidates_dict = {}
            candidates_dict["CandidateName"] = candidates_names[i].text.strip()
            candidates_dict["Coalition"] = candidates_coalitions[i].text.strip()
            candidates_dict["Votes"] = process_votes(candidates_votes[i].text.strip())
            candidates_dict["Percentage"] = candidates_percentages[i].text.strip()
            candidates_dict["Atleast25PercentOfCounty"] = candidates_25ptally[
                i
            ].text.strip()
            candidates_dict["CandidateImage"] = candidates_images[i]["src"].strip()
            candidates_dict["UpdatedAt"] = updated_element
            candidates_dict["Source"] = "https://www.bbc.com/news/world-africa-62444316"
            data.append(candidates_dict)

    except Exception as e:
        raise e
    else:
        return json.dumps(data)


def store_data(data_dir: Path, jsondata) -> None:
    try:
        data_dir.mkdir(exist_ok=True)
    except OSError as e:
        raise e
    csv_path = data_dir.joinpath(
        f"{datetime.now().strftime('%Y_%m_%d-%I:%M:%S_%p')}.csv"
    )
    with open(csv_path, "w") as f:
        df = pd.read_json(jsondata, orient="records")
        df.to_csv(str(csv_path), index=False)


def main():
    URL = "https://www.bbc.com/news/world-africa-62444316"
    DATA_DIR = Path(__file__).resolve().parent.parent.joinpath("data")
    page = make_request(url=URL)
    data = get_data(page)
    print(data)
    if data:
        store_data(data_dir=DATA_DIR, jsondata=data)


if __name__ == "__main__":
    main()
