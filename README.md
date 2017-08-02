# cta-bustracker-python
This is a Python wrapper for the Chicago Transit Authority's Bus Tracker API.

## Directions

### Initializing the API
Put your own api key as the argument for the API constructor
```python
import bustracker

api = bustracker.Api('api-key')	# put your api key here
```

### getTimes

```python
>>> api.getTime()
>>> {'tm': '20170802 16:04:55'}}
```
