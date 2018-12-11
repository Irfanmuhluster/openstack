from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver


auth_username = 'irvan'
auth_password = 'M0nalisa'
auth_url = 'http://rocky-controller.jcamp.net:5000'
project_name = 'irvan'

provider = get_driver(Provider.OPENSTACK)
conn = provider(auth_username, auth_password, ex_force_auth_url=auth_url,
                ex_force_auth_version='3.x_password',
                ex_tenant_name=project_name, ex_service_region='')
images = conn.list_images()
for image in images:
    print(image)
