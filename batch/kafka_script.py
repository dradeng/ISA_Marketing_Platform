from kafka import KafkaConsumer
import json
import time
from elasticsearch import Elasticsearch

c = None #KafkaConsumer
es = None #ElasticSearch
while c is None:
    try:
        c = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
        es = Elasticsearch(['es'])
    except:
        time.sleep(1)

es_load = False
ad = {"user": 1, "image": "", "duration": 10, "cost": 20.00, "url": "www.google.com", "site_title": "Google"}
time.sleep(10)
while not es_load:
    try:
        es.index(index='listing_index', doc_type='listing', id=ad['id'], body=ad)
        es.indices.refresh(index="listing_index")
        es_load = True
    except:
        time.sleep(1)

#consistent loop
while True:
    for message in c:
        message_dict = json.loads((message.value).decode('utf-8'))
        es.index(index='listing_index', doc_type='listing', id=message_dict['id'], body=message_dict)
    es.indices.refresh(index="listing_index")