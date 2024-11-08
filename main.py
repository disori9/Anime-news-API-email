import requests
import send_email as se

api_key = 'fb63e499cc284155baae7a1541c6447b'
url = ('https://newsapi.org/v2/everything?q=anime release&from=2024-11-07&to=2024-11-07&'
       'sortBy=popularity&apiKey=fb63e499cc284155baae7a1541c6447b')

# Request url from given to a variable
request = requests.get(url)

# Convert request to a json file, creating a dict variable
content = request.json()

# Iterate over the articles in the variable content (dict), then message all top articles to user in one email
email_message = "Subject: Anime News \n"
for article in content['articles']:
    if article['title'] is None:
        continue
    email_message = email_message + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2*"\n"

se.send_email(email_message)
