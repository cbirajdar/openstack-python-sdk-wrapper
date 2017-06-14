from auth import AuthenticationAPI

auth = AuthenticationAPI()

# Example project service
keystone = auth.keystone_api()

for project in keystone.projects.list():
    print project.id, project.name

# Example compute service
nova = auth.nova_api()

for server in nova.servers.list():
    print server.id, server.name

# Example block storage service
cinder = auth.cinder_api()

for volume in cinder.volumes.list():
    print volume.id, volume.name
