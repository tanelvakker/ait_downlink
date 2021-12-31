import logging
import time

from paho.mqtt.client import Client as MQTTClient

from config import NIBE_UPLINK_CONF, MQTT_CONF
from myupway_downlink import MyUpwayDownlink

logger = logging.getLogger()

nd = MyUpwayDownlink(**MYUPWAY_CONF)
mqtt_client = MQTTClient()
if 'auth' in MQTT_CONF:
  mqtt_client.username_pw_set(**MQTT_CONF['auth'])
mqtt_client.connect(MQTT_CONF['hostname'])
mqtt_client.loop_start()

while True:
  try:
    online, values = nd.getValues()
    # print values
    mqtt_client.publish(MQTT_CONF['prefix'] + '/online', 1 if online else 0, retain=True)
    if values:
      for key, value in values.iteritems():
        mqtt_client.publish(MQTT_CONF['prefix'] + '/variables/' + str(key), value, retain=True)
  except Exception as e:
    logger.exception("Failed to get MyUpway values")
  time.sleep(60)
