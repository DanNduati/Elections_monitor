import json
from datetime import datetime
from pathlib import Path

import pandas as pd
import tenacity
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)


def process_stats(stats: str):
    return int(stats.split("(")[0].replace(",", "")), float(
        stats.split("(")[1].strip(")").replace("%", "")
    )


@tenacity.retry(stop=tenacity.stop_after_attempt(20))
def get_data(url: str, driver: webdriver.Chrome):
    data = []
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find("table", class_="table table-striped")
        data_rows = table.find_all("tr")
        for i, candidate in enumerate(data_rows):
            candidate_dict = {}
            if i == 0 or i > 4:
                # Ignore the tr element in the th and the
                # last tr element (contains the updated at data).
                continue
            candidate_dict["CandidateName"] = str(
                candidate.find("th", class_=None).text.lower()
            ).title()
            candidate_dict["Votes"], candidate_dict["Percentage"] = process_stats(
                candidate.find("td", class_=None).text
            )
            candidate_dict["Party"] = str(
                candidate.find("td", class_="text-uppercase").text.lower()
            ).capitalize()
            candidate_dict["Source"] = url
            candidate_dict["UpdatedAt"] = str(datetime.now())
            data.append(candidate_dict)
    except:
        print("Could not fetch data")
    else:
        return json.dumps(data)
    finally:
        driver.quit()


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
    URL = "https://elections.citizen.digital/"
    DATA_DIR = Path(__file__).resolve().parent.parent.joinpath("data")
    data = get_data(url=URL, driver=driver)
    print(data)
    if data:
        store_data(data_dir=DATA_DIR, jsondata=data)


if __name__ == "__main__":
    main()
