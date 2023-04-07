import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.nocsdegree.com/jobs/')

if (response.status_code) == 200:
    print("successful request")
else: 
    print("request failed")

html_content = response.text

soup = BeautifulSoup(response.text, 'html.parser')

for job_title in soup.find_all('h2', class_='feed-title'):
    print(job_title.text)

for job_description in soup.find_all('div', class_='feed-excerpt'):
    print(job_description.text)