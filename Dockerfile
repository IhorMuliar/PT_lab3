FROM python

COPY . /orders.py

WORKDIR /orders.py

CMD ["python3", "orders"]