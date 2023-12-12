FROM alpine:3.18
RUN apk upgrade --no-cache
RUN apk add python3
RUN apk add py3-pip
COPY ./compra_ahorra /opt/app/compra_ahorra

WORKDIR /opt/app/compra_ahorra
RUN pip install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:9000