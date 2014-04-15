import requests
import re
pageUrls= [
	"https://www.facebook.com/Intel",
]

def printOutput(output):
    # print the output (key-value)
    pages = "pages =    [\n"
    for k in output:
        pages += "\t\"%s\", # %s\n" % (k, output[k])
    pages += "\t]"
    print pages

def getPageIds(pageUrls):
    # Get IDs for a list of pages
    # return: a dictionary with key: Page's ID and value: Page's Url
    output  = {}

    for url in pageUrls:
        payload = {}
        payload['fb_profile_url'] = url
        payload['unsanitized'] = url
        # using the service from findmyfacebookid to get the Id
        p = requests.post("http://findmyfacebookid.com/", data=payload)

        m = re.search('<span id="code">([0-9]+)</span>', p.text)
        if m is None:
            continue
        if m.group(1) in output:
            continue
        output[m.group(1)] = url

    return output

printOutput(getPageIds(pageUrls))
