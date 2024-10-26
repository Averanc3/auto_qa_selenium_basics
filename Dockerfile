FROM python:3.12-alpine
WORKDIR /tests
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["pytest"]
CMD ["--browser"]

