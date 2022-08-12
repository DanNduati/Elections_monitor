import glob
import json
import os
from pathlib import Path

import pandas as pd
from fastapi import APIRouter

router = APIRouter(prefix="/election", tags=["Election"])


def get_latest_data():
    DATA_DIR = Path(__file__).resolve().parent.parent.parent.joinpath("data")
    files = glob.glob(str(DATA_DIR) + r"/*csv")
    if not files:
        return None
    # Get the latest scraper output csv file
    latest_file = max(files, key=os.path.getctime)
    try:
        with open(latest_file, "r") as f:
            df = pd.read_csv(f)
            json_data = json.loads(df.to_json(orient="records"))
    except Exception as e:
        raise e
    else:
        return json_data


@router.get("/")
async def get_election_data():
    data = get_latest_data()
    return {"data": data}
