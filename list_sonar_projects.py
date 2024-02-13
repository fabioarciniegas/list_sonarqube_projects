import requests
import os

list_components_url = "https://dssonar.trendmicro.com/api/components/search?qualifiers=TRK"

pages_left = True
# SONARQUBE_API_TOKEN can be defined directly on environment or on sq.env. This is of course .gitignored
token = os.environ['SONARQUBE_API_TOKEN']
print(token)
while pages_left:
    response = requests.get(list_components_url,
                            headers={'Authorization': f"Basic %s"%token })
    pages_left = False
