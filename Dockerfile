FROM python:3.10-slim-buster

RUN mkdir -p /api

WORKDIR /api

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copy api
COPY . .


CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
