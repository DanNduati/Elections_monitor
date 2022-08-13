<h1 align="center"> Presidential Elections Watch </h1>

Lets have fun with some election data.

## <b>Description</b>
Scrape presidential tally election data off either:
1. [Citizen Tv's election portal](https://elections.citizen.digital/). 
2. [BBC News](https://www.bbc.com/news/world-africa-62444316)

And provides a simple API interface to the data.

## <b>Prerequisites</b>
1. [Python](https://www.python.org/downloads/)
2. [Docker and Docker Compose](https://docs.docker.com/get-docker/)

## <b>Setup</b>
<details>
<summary>Click to expand!</summary>

### Clone the repository
```bash
$ git clone https://github.com/DanNduati/Elections_watch.git
$ cd Elections_watch/
```
### 1. Local Installation
#### Install dependencies
Create a python virtual environment activate it and install dependencies
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
#### Schedule the scraper
> :warning: The cron service is only available for **Unix-based systems** checkout the Windows OS equivalent to a cron job called a [scheduled task](https://active-directory-wp.com/docs/Usage/How_to_add_a_cron_job_on_Windows/Scheduled_tasks_and_cron_jobs_on_Windows/)

Schedule the scraper to run every `n`th duration with cron. In my case i ran the scraper every 15 minutes by adding the following to your crontab file:
```bash
*/15 * * * * <path to your virtual environment python executable> <path to the scraper script>
```
#### Run the API server
```bash
$ uvicorn api.main:app --reload
```

### 2. Docker
#### Schedule the scraper
Schedule the scraper to run at your preferred duration as described in the local installation section.

#### Build and run the API with Docker Compose
```bash
$ docker compose up -d --build
```
</details>

### 3.Check the API
#### 1. <b>Presidential Results endpoint</b>
```http
GET /elections/
```
__Sample request__
```bash
curl -X 'GET' \
  'http://0.0.0.0:8000/election/' \
  -H 'accept: application/json'
```
__Sample response__
```json

{
  "data": [
    {
      "CandidateName": "William Ruto",
      "Coalition": "Kenya Kwanza Alliance",
      "Votes": 6395857,
      "Percentage": "51.1%",
      "Atleast25PercentOfCounty": "21/47",
      "CandidateImage": "https://news.files.bbci.co.uk/include/vjafeast/642-kenya-presidential-elections-results/assets/app-project-assets/img/candidates/kka.png",
      "UpdatedAt": "08/13/2022, 18:09:04 local time (GMT+3)",
      "Source": "https://www.bbc.com/news/world-africa-62444316"
    },
    {
      "CandidateName": "Raila Odinga",
      "Coalition": "Azimio la Umoja coalition",
      "Votes": 6026207,
      "Percentage": "48.2%",
      "Atleast25PercentOfCounty": "19/47",
      "CandidateImage": "https://news.files.bbci.co.uk/include/vjafeast/642-kenya-presidential-elections-results/assets/app-project-assets/img/candidates/alu.png",
      "UpdatedAt": "08/13/2022, 18:09:04 local time (GMT+3)",
      "Source": "https://www.bbc.com/news/world-africa-62444316"
    },
    {
      "CandidateName": "George Wajackoyah",
      "Coalition": "Roots Party",
      "Votes": 56700,
      "Percentage": "0.5%",
      "Atleast25PercentOfCounty": "0/47",
      "CandidateImage": "https://news.files.bbci.co.uk/include/vjafeast/642-kenya-presidential-elections-results/assets/app-project-assets/img/candidates/roots.png",
      "UpdatedAt": "08/13/2022, 18:09:04 local time (GMT+3)",
      "Source": "https://www.bbc.com/news/world-africa-62444316"
    },
    {
      "CandidateName": "David Mwaure",
      "Coalition": "Agano Party",
      "Votes": 27802,
      "Percentage": "0.2%",
      "Atleast25PercentOfCounty": "0/47",
      "CandidateImage": "https://news.files.bbci.co.uk/include/vjafeast/642-kenya-presidential-elections-results/assets/app-project-assets/img/candidates/agano.png",
      "UpdatedAt": "08/13/2022, 18:09:04 local time (GMT+3)",
      "Source": "https://www.bbc.com/news/world-africa-62444316"
    }
  ]
}
```
Alternatively open your browser at: http://0.0.0.0:8000/
You should see the automatic interactive API documentation provided by Swagger UI:
<p align="center">
    <img src="images/swagger_docs.png">
</p>

## <b>License and Copyright</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)

Copyright 2022 Daniel Chege Nduati
