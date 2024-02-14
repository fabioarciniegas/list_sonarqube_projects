import requests
import os

list_components_url = "https://dssonar.trendmicro.com/api/components/search?qualifiers=TRK"
show_components_url = "https://dssonar.trendmicro.com/api/components/show"

pages_left = True
# SONARQUBE_API_TOKEN can be defined directly on environment or on sq.env. This is of course .gitignored
token = os.environ['SONARQUBE_API_TOKEN']
page = 0
results = []
while pages_left:
    page += 1
    # Sonarqube expects basic authentication of the form ~~ Basic base64(user:pwd)
    # with the token as user and no password
    # TODO: f string
    projects = requests.get(list_components_url + "&p=" + str(page),
                            headers={'Authorization': f"Basic %s" % token})
    components = projects.json()
    comps_in_page = len(components['components'])
    print(f"Page {page} has {comps_in_page} components")
    for c in components['components']:
        details = requests.get(show_components_url + "?component=" + c['key'],
                               headers={'Authorization': f"Basic %s" % token})
        github_repo = details.json()['component']['description'] if 'description' in details.json()['component'].keys()  else ""
        results.append({"name":c['key'],"github_repo":github_repo})
    pages_left = comps_in_page > 0
print(results)