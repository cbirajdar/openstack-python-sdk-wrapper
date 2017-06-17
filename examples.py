from auth import AuthenticationAPI

auth = AuthenticationAPI()

# Keystone service
keystone = auth.keystone_api()

# List projects
for project in keystone.projects.list():
    print project.id, project.name

# List users
for user in keystone.users.list():
    print user.id, user.name

# Compute service
nova = auth.nova_api()
for server in nova.servers.list():
    print server.id, server.name

# Block storage service
cinder = auth.cinder_api()
for volume in cinder.volumes.list():
    print volume.id, volume.name

# Glance service
glance = auth.glance_api()
for image in glance.images.list():
    print image.id, image.name
