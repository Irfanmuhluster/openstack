from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client


# def token(args):
auth = v3.Password(auth_url="http://rocky-controller.jcamp.net:5000/v3",
                   username="irvan", password="M0nalisa",
                   project_name="irvan",
                   user_domain_name="Default", project_domain_name="Default")
sess = session.Session(auth=auth)
keystone = client.Client(session=sess, include_metadata=True)
dir(keystone)
# oke = keystone.projects.list()
# print(oke)
