# presearch-proxy
A simple flask app that enables queries to [presearch](https://www.presearch.org) to be made as your browser's default search engine (e.g. from the chrome omnibox).

*Disclaimer: It is unclear whether or not the usage of this proxy violates presearch's [terms and conditions](https://presearch.org/terms), which prohibits running automated programs or bots.*
**Use at your own risk!**

## Quickstart

First, make sure you have both flask and requests installed. To start a server locally, run the command `python presearch.py`. 
By default, this will listen locally on port 5000.
The server expects requests to be of the form `http://localhost:5000/<token>/<cookie>/<query>`

### Finding `token` and `cookie`

To find your `token` and `cookie`, you'll need to login to presearch.org, open your browser's dev console, select the network tab, make sure "preserve log" is checked, and make a sample search.
You should see a POST request to "https://www.presearch.org/search". Select it, and the request headers will contain `cookie: ...`, and `_token: ...` in the form data.

### Chrome

In chrome open the settings menu (or navigate to chrome://settings/), and click "Manage search engines". 
Click ADD to add a new search engine. 
The `Search engine` and `keyword` fields should not matter, but it's proabably easiest just to use presearch and presearch.org, respectively. 
The `URL` is the important field, and needs to be of the form `http://localhost:5000/<token>/<cookie>/%s`.
Once you've added your custom search engine, click the vertical elipses `⋮` next to it, and select "Make default".
Now when you perform a search from the chrome omnibox, it will simulate a query made from the main presearch.org page, and redirect you to the result.

### Firefox

### Brave

## TODO List

- Firefox/brave documentation
- Create proper python module
- Automate token and cookie retrieval
- Dockerize?
- Terms and conditions clarification
