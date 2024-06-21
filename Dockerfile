FROM python:3.10.2-slim

RUN apt update && apt install -y --no-install-recommends

COPY ./requirements.txt /tmp
COPY . ./

RUN pip install -r /tmp/requirements.txt

ENTRYPOINT ["/bin/entrypoint.sh"]