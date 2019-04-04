from kafka import KafkaConsumer
import json
import time
from elasticsearch import Elasticsearch

consumer = None
es = None
while consumer is None:
    try:
        consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
        es = Elasticsearch(['es'])
    except:
        time.sleep(1)

loaded_es = False
ad1 = {"user": 1, "image": "", "duration": 10, "cost": 20.00, "url": "www.google.com", "site_title": "Google", "id": 1}
time.sleep(10)
while not loaded_es:
    try:
        es.index(index='listing_index', doc_type='listing', id=ad1['id'], body=ad1)
        es.indices.refresh(index="listing_index")
        loaded_es = True
    except:
        time.sleep(1)

while True:
    for message in consumer:
        message_dict = json.loads((message.value).decode('utf-8'))
        es.index(index='listing_index', doc_type='listing', id=message_dict['id'], body=message_dict)
    es.indices.refresh(index="listing_index")
