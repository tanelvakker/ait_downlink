# MyUpway Downlink
Get variables from MyUpway. Based on https://github.com/yozik04/nibe_downlink

# Requirements
Your heatpump should be registered in MyUpway. This module fetches data from MyUpway

# Installation

    pip install git+https://github.com/tanelvakker/myupway_downlink.git

# Usage

``` python
from pprint import pprint

from nibe_downlink import MyUpwayDownlink

MYUPWAY_CONF = {
  'username': "example@example.com",
  'password': "myupway_pass",
  "hpid": "99999", # heat pump id
  'variables': [47011,48132,47041,40008,40012,40015,40016,43005,43416,43420,43424,43136,43439,43437,40004,40013,10069] # variables you want to fetch
}

nd = MyUpwayDownlink(**MYUPWAY_CONF)

online, values = nd.getValues()

print "Is online: %s" % str(online)
pprint(values)
```

### Heat Pump ID: hpid
Get your **hpid** from Nibe Uplink web site. Open a heatpump and it's id will be in your address bar:
https://www.myupway.com/System/**99999**/Status/Overview

### Variable IDs
See https://github.com/openhab/openhab1-addons/wiki/Nibe-Heat-Pump-Binding

# Examples

Copy *examples/config.py.dist* to *examples/config.py* and change settings inside the file

### MyUpway -> MQTT bridge service

See *examples/mqtt.py*
