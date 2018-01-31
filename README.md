# presearch-proxy
A simple flask app that enables queries to [presearch](https://www.presearch.org) to be made as your browser's default search engine (e.g. from the chrome omnibox).

*Disclaimer: It is unclear whether or not the usage of this proxy violates presearch's [terms and conditions](https://presearch.org/terms), which prohibits running automated programs or bots.*
**Use at your own risk!**

## Quickstart

First, make sure you have flask, requests and pycookiecheat installed. To start a server locally, run the command `python presearch.py`. 
By default, this will listen locally on port 5000.
The server expects requests to be of the form `http://localhost:5000/<query>`

### Login (Must use Chrome)

This proxy does *NOT* log you in. You must already be logged into presearch.org through the chrome browser. If you find this useful, feel free to make PR to support other browsers. 

### Chrome

In chrome open the settings menu (or navigate to chrome://settings/), and click "Manage search engines". 
Click ADD to add a new search engine. 
The `Search engine` and `keyword` fields should not matter, but it's proabably easiest just to use presearch and presearch.org, respectively. 
The `URL` is the important field, and needs to be of the form `http://localhost:5000/%s`.
Once you've added your custom search engine, click the vertical elipses `⋮` next to it, and select "Make default".
Now when you perform a search from the chrome omnibox, it will simulate a query made from the main presearch.org page, and redirect you to the result.

### Firefox

### Brave

## TODO List

- Firefox/brave documentation
- Create proper python module
- Dockerize?
- Terms and conditions clarification
