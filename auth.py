import os
from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client as nova
from keystoneclient.v3 import client as keystone
from cinderclient import client as cinder
from glanceclient import client as glance

class AuthenticationAPI:
    def __init__(self):
        self.url = os.environ.get('OS_AUTH_URL') + '/v3'
        self.username = os.environ.get('OS_USERNAME')
        self.password = os.environ.get('OS_PASSWORD')
        self.user_domain_id = os.environ.get('OS_USER_DOMAIN_ID')
        self.project_id = os.environ.get('OS_TENANT_ID')

    def project_scoped_session(self):
        auth = v3.Password(auth_url=self.url,
                           username=self.username,
                           password=self.password,
                           user_domain_id=self.user_domain_id,
                           project_id=self.project_id)
        return session.Session(auth=auth)

    def domain_scoped_session(self):
        auth = v3.Password(auth_url=self.url,
                           username=self.username,
                           password=self.password,
                           user_domain_id=self.user_domain_id,
                           domain_id=self.user_domain_id)
        return session.Session(auth=auth)

    def keystone_api(self):
        return keystone.Client(session=self.domain_scoped_session())

    def nova_api(self):
        return nova.Client("2.1", session=self.project_scoped_session())

    def cinder_api(self):
        return cinder.Client("2", session=self.project_scoped_session())

    def glance_api(self):
        return glance.Client("2", session=self.project_scoped_session())
