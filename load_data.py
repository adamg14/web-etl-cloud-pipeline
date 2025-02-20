# loading the cleaned data into google cloud SQL
from googleapiclient import discovery

service = discovery.build('sqladmin', 'v1beta4', http=http)

request = service.instance().list(project='PROJECT_ID')
response = request.execute()
print(json.dump(resp, indent=2))