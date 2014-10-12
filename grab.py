import mechanize
BASE_URL = "https://www.surveymonkey.com/s/KLCBNM5"
br = mechanize.Browser()
data = br.open(BASE_URL).get_data()
links = scrape_links(BASE_URL, data)

for link in links:
    data = br.follow_link(link).get_data()
scrape_articles(data)
br.back()

print ("data")
