
from kafka import KafkaProducer, KafkaConsumer

import json

producer= KafkaProducer(
  bootstrap_servers='localhost:9092',
  value_serializer= lambda v: json.dumps(v).encode('utf-8')
)

message= {
"website" : "https://coderbyte.com",
"activity" :"click",
"id" :"start-button",
"date" :"2021-10-10"
}

producer.send('activity-log',value=message)
producer.flush()

consumer= KafkaConsumer(
  'activity-log',
  bootstrap_servers='localhost:9092',
  value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
for msg in consumer:
  print(f"Received message: {msg}")