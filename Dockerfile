FROM python:3.12-alpine
WORKDIR /tests
COPY requirements.txt .
COPY wait-for-it.sh .
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN chmod +x wait-for-it.sh
COPY . .
CMD ["pytest"]

