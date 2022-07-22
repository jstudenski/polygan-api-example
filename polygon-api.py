import requests

parameters = {
  "apiKey": "",
  "sort": "asc",
  "limit": "120",
  "adjusted": "true"
}

# The ticker symbol of the stock/equity.
stocksTicker = 'AAPL'
# The size of the timespan multiplier.
multiplier = '1'
# The size of the time window.
# minute, hour, day, week, month, quarter, year
timespan = 'day'
# The start of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
startDate = '2021-07-22'
# The end of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
endDate = '2021-07-22'

url = "https://api.polygon.io/v2/aggs/ticker/" + stocksTicker + "/range/" + multiplier + "/" + timespan + "/" + startDate + "/" + endDate

response = requests.get(url, params=parameters)

print(response.json())

