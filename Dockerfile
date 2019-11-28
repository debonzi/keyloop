FROM python:3.7.5-buster

ADD . /app

WORKDIR /app
RUN pip install -e .

EXPOSE 8000
CMD ["pserve", "development.ini"]
