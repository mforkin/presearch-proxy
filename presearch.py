import requests
import re
from flask import Flask, redirect
from pycookiecheat import chrome_cookies

app = Flask(__name__)

base_url = 'https://www.presearch.org'
url = base_url + '/search'
payload = {
    'provider_id': 1,
}

@app.route('/<query>')
def search(query):
    cookies = chrome_cookies(url)
    html = requests.get(url, cookies=cookies).text
    token = re.compile('csrf-token" content="(.*)">').search(html).group(1)
    payload['_token'] = token
    payload['term'] = query
    return redirect(requests.post(url, json=payload, cookies=cookies).url)

if __name__ == '__main__':
    app.run()
