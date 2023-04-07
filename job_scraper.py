import requests
response = requests.get('https://www.nocsdegree.com/jobs/')

if (response.status_code) == 200:
    print("successful request")
else: 
    print("request failed")

html_content = response.text

print(html_content)