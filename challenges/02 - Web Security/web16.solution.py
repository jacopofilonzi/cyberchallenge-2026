import requests
from bs4 import BeautifulSoup as soup, Comment



found = False
page_seen = []

def doPage(base_url, page_url):
    global found

    if page_url in page_seen:
        return
    page_seen.append(page_url)

    print(f"Visiting page: {len(page_seen)}")
    response = requests.get(f"{base_url}{page_url}")

    zuppa = soup(response.text, 'html.parser')

    h1 = zuppa.find("h1")
    if h1 and "flag" in h1.text.lower():
        print(f"Flag found in page: {page_url}")
        print("Content:")
        print(h1.text)
        found = True
        return
    

    links = zuppa.find_all("a", attrs={"href": True})

    for link in links:
        href = link.get("href")
        if not found:
            doPage(base_url, href)

# Start looking for the flag from the initial page
doPage("http://web-16.challs.olicyber.it", "/")
