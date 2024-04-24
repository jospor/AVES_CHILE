import requests
import json
from string import Template

def request_get(url):
    return json.loads(requests.get(url).text)

url = 'https://aves.ninjas.cl/api/birds'
results = request_get(url)[:20]

img_template = Template('<img src="$url" alt="$name">')

html_template = Template('''<!DOCTYPE html>
<html>
<head>
<title>Aves de Chile</title>
</head>
<body>

<h1>Aves de Chile</h1>

$body

</body>
</html>
''')

body_content = ''
for bird in results:
    image_url = bird['images']['main']
    name_spanish = bird['name']['spanish']
    name_english = bird['name']['english']
    image_html = img_template.substitute(url=image_url, name=name_spanish)
    body_content += f'<div><h2>{name_spanish}</h2><h3>{name_english}</h3>{image_html}</div>\n'

html_content = html_template.substitute(body=body_content)

with open('index.html', 'w') as f:
    f.write(html_content)