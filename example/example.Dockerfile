FROM ubuntu

WORKDIR /opt/example
COPY . /opt/example

RUN apt-get update \
    && apt-get upgrade -y \
    # && apt-get install python3 -y \
    && apt-get install python3-pip -y

RUN pip3 install azure-cosmosdb-table
CMD [ "python3", "main.py" ] 