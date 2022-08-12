<h1 align="center"> Presidential Elections Watch </h1>

Lets have fun with some election data.

## <b>Description</b>
Scrape presidential election data off [Citizen Tv's election portal](https://elections.citizen.digital/). And provides a simple API interface to the data.

## <b>Prerequisites</b>
1. [Python](https://www.python.org/downloads/)
2. [Docker and Docker Compose](https://docs.docker.com/get-docker/)

## <b>Setup</b>
### Clone the repository
```bash
$ git clone https://github.com/DanNduati/Elections_watch.git
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

### 3.Check it
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
      "CandidateName": "William Samoei Ruto",
      "Votes": 6562405,
      "Percentage": 49.33,
      "Party": "Uda",
      "UpdatedAt": "2022-08-12 18:00:20.767119"
    },
    {
      "CandidateName": "Raila  Odinga",
      "Votes": 6553978,
      "Percentage": 49.27,
      "Party": "Azimio",
      "UpdatedAt": "2022-08-12 18:00:20.767245"
    },
    {
      "CandidateName": "George Luchiri Wajackoyah",
      "Votes": 57840,
      "Percentage": 0.43,
      "Party": "Roots",
      "UpdatedAt": "2022-08-12 18:00:20.767349"
    },
    {
      "CandidateName": "David Mwaure Waihiga",
      "Votes": 29731,
      "Percentage": 0.22,
      "Party": "Agano",
      "UpdatedAt": "2022-08-12 18:00:20.767455"
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
