import requests

api_key = 'fb63e499cc284155baae7a1541c6447b'
url = ('https://newsapi.org/v2/everything?q=anime&from=2024-10-08'
       '&sortBy=publishedAt&apiKey=fb63e499cc284155baae7a1541c6447b')

# Request url from given to a variable
request = requests.get(url)

# Convert request to a json file, creating a dict variable
content = request.json()

# Iterate over the articles in the variable content (dict), as it is a list, then print out each item title in the list
for article in content['articles']:
    print(article['title'])
    print(article['description'])
