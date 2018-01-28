import requests
from flask import Flask, redirect

app = Flask(__name__)

url = 'https://www.presearch.org/search'
payload = {
    'provider_id': 1,
}

@app.route('/<token>/<cookie>/<query>')
def search(token, cookie, query):
    payload['_token'] = token
    payload['term'] = query
    return redirect(requests.post(url, json=payload, headers={'cookie': cookie}).url)

if __name__ == '__main__':
    app.run()
