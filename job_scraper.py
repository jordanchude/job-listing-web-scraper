import requests
response = requests.get('https://www.indeed.com/jobs?q=software+engineer&l=Remote&sc=0kf%3Aattr%28DSQF7%29explvl%28ENTRY_LEVEL%29%3B&vjk=1435860112a9a13b')

if (response.status_code) == 200:
    print("successful request")
else: 
    print("request failed")

html_content = response.text

print(html_content)

urls = []

for url in urls:
    response = requests.get(url)
    print(response.content)