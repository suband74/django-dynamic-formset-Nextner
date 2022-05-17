FROM python:3.10

WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code

COPY ./entrypoint.sh /code
RUN chmod 755 entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]