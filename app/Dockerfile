FROM python:3.9-slim

RUN apt-get update 
RUN apt-get install -y libcap2-bin
RUN setcap cap_net_raw+ep $(readlink -f $(which python))

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install --no-cache-dir flask

RUN useradd -u 1000 hiredscore
USER hiredscore

WORKDIR /opt/venv
EXPOSE 5000
COPY pizza_order.py /opt/venv/

CMD [ "python", "/opt/venv/pizza_order.py" ]