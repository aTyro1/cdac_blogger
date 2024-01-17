FROM python:3.10.12-alpine

RUN pip3 install --upgrade pip

COPY ./requirement.txt .
RUN pip3 install -r requirement.txt

COPY . /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
