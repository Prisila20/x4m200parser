# Python parser for Novelda’s XeThru X4M300

The XeThru [X4M300](https://www.xethru.com/x4m300-presence-sensor.html) is Novelda’s presence and occupancy sensor powered by the XeThru X4 ultra wideband radar chip. This parser extracts the raw data from the radar, without Novelda’s processing.  

# Installing

X4M300 drivers for MacOs and Linux are added to the repository for easier access.  Other drivers are accessible [here](https://www.xethru.com/community/resources/).  For installing the drivers and the parser, write

```sh
./setup/install.sh
```

# Usage

Example python script for aquireing data from the sensor:

```python
sd = StreamData(USB_PORT)

for i_data, q_data in sd:
    print('i_data:', i_data)
    print('q_data:', q_data)
```
