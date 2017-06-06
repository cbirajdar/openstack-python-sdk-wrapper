from auth import AuthenticationAPI

auth = AuthenticationAPI()

# Example project service
keystone = auth.keystone_api()

for project in keystone.projects.list():
    print project.id, project.name

# Example compute service
nova = auth.nova_api(project_id='YOUR_PROJECT_ID')

for server in nova.servers.list():
    print server.id, server.name
