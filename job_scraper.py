import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.nocsdegree.com/jobs/')

if (response.status_code) == 200:
    print("successful request")
else: 
    print("request failed")

html_content = response.text

soup = BeautifulSoup(response.text, 'html.parser')


def jobs():
    job_titles = [title.text for title in soup.find_all('h2', class_='feed-title')]
    job_descriptions = [description.text for description in soup.find_all('div', class_='feed-excerpt')]
    for (title, description) in zip(job_titles, job_descriptions):
        print(f'Job: {title}\nDescription: {description}\n')
    
jobs()