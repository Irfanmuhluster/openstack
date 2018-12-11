import sys
import os
import ui
import time
import json
import re
# from utils import print_values
from keystoneclient.v3 import client as ksclient
from novaclient import client as nvclient
from keystoneauth1 import identity
from keystoneauth1 import session
from keystoneauth1 import loading
from glanceclient import Client as glclient
from neutronclient.v2_0 import client as nwclient


auth_url = os.environ.get("OS_AUTH_URL")
username = os.environ.get("OS_USERNAME")
user_domain_name = os.environ.get("OS_USER_DOMAIN_NAME")
project_name = os.environ.get("OS_PROJECT_NAME")
project_domain_name = os.environ.get("OS_PROJECT_DOMAIN_NAME")
password = os.environ.get("OS_PASSWORD")


auth = ksclient.Client(auth_url=auth_url, version=(3,),
                       username=username, password=password,
                       user_domain_name=user_domain_name,
                       project_name=project_name,
                       project_domain_name=project_domain_name)
sess = session.Session(auth=auth)
ks = ksclient.Client(session=sess)


def create_project(args, name, domain, description):
    '''
        Perintah untuk membuat project
        create_project name domain description
        Args:
            args (str): argument function create_project.
            name (str): name project.
            domain    : id domain untuk project
            description: deskripsi project
        contoh: python test.py create_project irvan3 default coba...
    '''
    ui.info_section(f'== create project {name}== \n')
    try:
        enabled = True
        create = ks.projects.create(name=name, domain=domain,
                                    description=description, enabled=enabled)
        ui.info_3(create, '\n')
        ui.info_3('\n Done ', ui.check)
    except Exception as e:
        '''jika tidak ada nama'''
        ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def create_user(args, name, domain, project, password, email=None, description=None):
    '''
        Perintah untuk membuat user
        create_user name domain project password email description
        Args:
            args (str): argument function create_user.
            name (str): name project.
            domain    : id domain untuk user
            project   : id project untuk user
            password  : password untuk user yg dibuat
            email     : email (optional)
            description: deskripsi user (optional)
        contoh:  python test.py create_user irvan8 default 6bd9cebb746c420783039ce7606f8aa1 M0nalisa testemail@gmail.com fojijbgigtr
    '''
    ui.info_section(f'== Create User == \n')
    if email is None and description is None:
        '''jika diisi hanya sampai password'''
        try:
            enabled = True
            create = ks.users.create(name=name, domain=domain, project=project,
                                     password=password, enabled=enabled)
            ui.info_3(create, '\n')
            ui.info_3('\n Done ', ui.check)
        except Exception as e:
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)
    elif description is None:
        '''description kosong'''
        try:
            enabled = True
            create = ks.users.create(name=name, domain=domain, project=project,
                                     password=password, email=email,
                                     enabled=enabled)
            ui.info_3(create, '\n')
            ui.info_3('\n Done ', ui.check)
        except Exception as e:
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)
    else:
        try:
            enabled = True
            # cek = (f'{ks.projects.list(name=name)[0]}')
            # baca = cek.strip().split(',')
            # result = [i for i in baca if i.startswith(' id')]
            # oke = result[0]
            # id_project = oke.strip().strip('id=')
            create = ks.users.create(name=name, domain=domain, project=project,
                                     password=password, email=email,
                                     description=description, enabled=enabled)
            ui.info_3(create, '\n')
            ui.info_3('\n Done ', ui.check)
        except Exception as e:
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def update_user(args, user, name, domain, project, password, email=None, description=None):
    '''
        Perintah untuk update user
        create_project(args, name, domain, project, password,
                       email=None, description=None)
        Args:
            args (str): argument function create_project.
            name (str): name user.
            domain    : id domain untuk user
            password  : password untuk user yg dibuat
            email     : email (optional)
            description: deskripsi user (optional)
        contoh:  python test.py create_user irvan8 default 6bd9cebb746c420783039ce7606f8aa1 M0nalisa testemail@gmail.com fojijbgigtr
    '''
    ui.info_section(f'== Update User == \n')
    if email is None and description is None:
        '''jika diisi hanya sampai password'''
        try:
            enabled = True
            update = ks.users.update(user=user, name=name, domain=domain, project=project,
                                     password=password, enabled=enabled)
            ui.info_3(update, '\n')
            ui.info_3('\n Done ', ui.check)
        except Exception as e:
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)
    elif description is None:
        '''description kosong'''
        try:
            enabled = True
            update = ks.users.update(user=user, name=name, domain=domain, project=project,
                                     password=password, email=email,
                                     enabled=enabled)
            ui.info_3(update, '\n')
            ui.info_3('\n Done ', ui.check)
        except Exception as e:
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)
    else:
        try:
            enabled = True
            # cek = (f'{ks.projects.list(name=name)[0]}')
            # baca = cek.strip().split(',')
            # result = [i for i in baca if i.startswith(' id')]
            # oke = result[0]
            # id_project = oke.strip().strip('id=')
            update = ks.users.update(user=user, name=name, domain=domain, project=project,
                                     password=password, email=email,
                                     description=description, enabled=enabled)
            ui.info_3(update, '\n')
            ui.info_3('\n Done ', ui.check)
        except Exception as e:
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def delete_user(args, user):
    '''
        Perintah untuk menghapus user
        create_project(args, user)
        Args:
            args (str): argument function create_project.
            user : id user yg ingin dihapus
        contoh:  python test.py delete_user 83cadda8794743e7923821a38fea2683
    '''
    try:
        delete = ks.users.delete(user=user)
        ui.info_3(delete, '\n')
        ui.info_3('\n Done ', ui.check)
    except Exception as e:
        ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def delete_users(args, *users):
    '''delete beberapa user by name'''
    ui.info_section('== Delete Users== \n')
    for item in users:
        try:
            ui.info_3(' -----')
            cek = (f'{ks.users.list(name=item)[0]}')
            baca = cek.strip().split(',')
            result = [i for i in baca if i.startswith(' id')]
            oke = result[0]
            id_user = oke.strip().strip('id=')
            ui.info_3(f'Deleting Users {id_user} \n', ui.ellipsis)
            delete = ks.users.delete(user=id_user)
            ui.info_3(delete, '\n')
            ui.info_3('Delete Succes', ui.check)
        except Exception as e:
            ui.info(ui.red, ui.bold, 'Error: nama user gk ada', ui.reset, e)
            continue


def update_project(args, name, nameedit, description=None):
    '''update projects'''
    if description is None:
        try:
            cek = (f'{ks.projects.list(name=name)[0]}')
            baca = cek.strip().split(',')
            result = [i for i in baca if i.startswith(' id')]
            oke = result[0]
            id_project = oke.strip().strip('id=')
            update = ks.projects.update(
                project=id_project, name=nameedit)
            ui.info_3(update, '\n')
            ui.info_3('\n Done ', ui.check)
        except Exception as e:
            '''jika tidak ada nama'''
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)
    else:
        try:
            cek = (f'{ks.projects.list(name=name)[0]}')
            baca = cek.strip().split(',')
            result = [i for i in baca if i.startswith(' id')]
            oke = result[0]
            id_project = oke.strip().strip('id=')
            update = ks.projects.update(
                project=id_project, name=nameedit, description=description)
            ui.info_3(update, '\n')
            ui.info_3('\n Done ', ui.check)
        except Exception as e:
            '''jika tidak ada nama'''
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def delete_project(args, name):
    '''delete project by name'''
    try:
        '''memcoba'''
        cek = (f'{ks.projects.list(name=name)[0]}')
        baca = cek.strip().split(',')
        result = [i for i in baca if i.startswith(' id')]
        oke = result[0]
        id_project = oke.strip().strip('id=')
        ks.projects.delete(id_project)
        ui.info_3(f'Delete {id_project} success', ui.check)
    except Exception as e:
        '''jika tidak ada nama'''
        ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def grant_role(args, role, user, project):
    '''tanpa di grant gk bisa login, grant ke member saja'''
    try:
        ex = ks.roles.grant(role=role,
                            user=user,
                            system=None,
                            project=project)
        ui.info_3(ex)
        ui.info_3('\n Done ', ui.check)
    except Exception as e:
        '''jika tidak ada nama'''
        ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def grant_role2(args, role, user, project):
    '''grant role berdasarkan nama'''
    '''ex : python test.py grant_role2 roleirvan irvan irvan3'''
    ui.info_section(f'== Grant Role == \n')
    try:
        # mendapatkan id role dr nama
        cek = (f'{ks.roles.list(name=role)[0]}')
        baca = cek.strip().split(',')
        result = [i for i in baca if i.startswith(' id')]
        oke = result[0]
        id_role = oke.strip().strip('id=')

        # mendapatkan id user dr nama
        cek2 = (f'{ks.users.list(name=user)[0]}')
        baca2 = cek2.strip().split(',')
        result2 = [i for i in baca2 if i.startswith(' id')]
        oke2 = result2[0]
        id_user = oke2.strip().strip('id=')

        # mendapaktan id project dr nama
        cek3 = (f'{ks.projects.list(name=project)[0]}')
        baca3 = cek3.strip().split(',')
        result3 = [i for i in baca3 if i.startswith(' id')]
        oke3 = result3[0]
        id_project = oke3.strip().strip('id=')

        ex = ks.roles.grant(role=id_role,
                            user=id_user,
                            system=None,
                            project=id_project)
        ui.info_3(ex)
        ui.info_3('\n Done ', ui.check)
    except Exception as e:
        '''jika tidak ada nama'''
        ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


# revoke role
def revoke_role(args, role, user, project):
    '''mencabut role'''
    try:
        '''revoke roles'''
        cek = (f'{ks.roles.list(name=role)[0]}')
        baca = cek.strip().split(',')
        result = [i for i in baca if i.startswith(' id')]
        oke = result[0]
        id_roles = oke.strip().strip('id=')

        cek1 = (f'{ks.projects.list(name=project)[0]}')
        baca1 = cek1.strip().split(',')
        result1 = [i for i in baca1 if i.startswith(' id')]
        oke1 = result1[0]
        id_project = oke1.strip().strip('id=')

        cek2 = (f'{ks.users.list(name=user)[0]}')
        baca2 = cek2.strip().split(',')
        result2 = [i for i in baca2 if i.startswith(' id')]
        oke2 = result2[0]
        id_user = oke2.strip().strip('id=')

        cabut = ks.roles.revoke(
            role=id_roles, user=id_user, project=id_project)
        ui.info_3('revoke role success', ui.check)
        ui.info_3(cabut, '\n')
        ui.info_3('Done ', ui.check)
    except Exception as e:
        '''jika tidak ada nama'''
        ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def list_roles(args):
    for list in ks.roles.list():
        print(list)
        print('------')


def list_users(args, name=None):
    '''menampilkan daftar user'''
    if name is None:
        ui.info_section(f'== List Users == \n')
        cek = (f'{ks.users.list()}')
        # mencari name:
        baca = cek.strip().split(',')
        result = [i for i in baca if i.startswith(' name')]

        # mencari id:
        baca2 = cek.strip().split(',')
        result2 = [i for i in baca2 if i.startswith(' id')]

        headers = ['id', 'name']
        data = []
        for (id, name) in zip(result2, result):
            id = id[4:]
            name = name[6:]
            data.append(
                [
                    (ui.teal, id),
                    (ui.yellow, name)
                ]
            )
        ui.info_table(data, headers=headers)
    else:
        try:
            ui.info_section(f'== Detail User {name} == \n')
            # ks = ksclient.Client(session=sess)
            cek = (f'{ks.users.list(name=name)[0]}')
            # print(cek)
            baca = cek.strip().strip('>').strip('<').split(',')
            # print(baca)
            oke = baca[0:8]
            hello = [x.strip(' ') for x in oke]
            # print(hello)
            str1 = '\n'.join(hello)
            print(str1, '\n')
        except Exception as e:
            '''jika tidak ada nama'''
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def list_projects(args):
    '''
        Perintah untuk melihat list project
        list_projects
        contoh:  python test.py list_projects
    '''
    ui.info_section('== List Projects == \n')
    cek = (f'{ks.projects.list()}')
    # mencari name:
    baca = cek.strip().split(',')
    result = [i for i in baca if i.startswith(' name')]

    # mencari id:
    baca2 = cek.strip().split(',')
    result2 = [i for i in baca2 if i.startswith(' id')]

    # mencari domain id
    baca3 = cek.strip().split(',')
    result3 = [i for i in baca3 if i.startswith(' domain_id')]

    headers = ['id Project', 'name', 'id domain']
    data = []
    for (id, name, domain_id) in zip(result2, result, result3):
        id = id[4:]
        name = name[6:]
        domain_id = domain_id[11:]
        data.append(
            [
                (ui.teal, id),
                (ui.yellow, name),
                (ui.yellow, domain_id)
            ]
        )
    ui.info_table(data, headers=headers)


def list_domains(args):
    '''perintah untuk melihat list domain'''
    ui.info_section(f'== List Domains == \n')
    cek = (f'{ks.domains.list()}')
    # mencari name:
    baca = cek.strip().split(',')
    result = [i for i in baca if i.startswith(' name')]

    # mencari id:
    baca2 = cek.strip().split(',')
    result2 = [i for i in baca2 if i.startswith(' id')]

    headers = ['Id Domains', 'Name']
    data = []
    for (id, name) in zip(result2, result):
        id = id[4:]
        name = name[6:]
        data.append(
            [
                (ui.teal, id),
                (ui.yellow, name)
            ]
        )
    ui.info_table(data, headers=headers)


def create_network(args, name, subnetname, cidr):
    '''buat network'''
    '''namanetwork namasubnet networkaddress'''
    #  network_name = 'int_network1'
    ui.info_section(f'== Create Network {name}== \n')
    auth = identity.Password(auth_url=auth_url,
                             username=username,
                             password=password,
                             project_name=project_name,
                             project_domain_name=project_domain_name,
                             user_domain_name=user_domain_name)
    sess = session.Session(auth=auth)
    neutron = nwclient.Client(session=sess)
    try:
        body_sample = {'network': {'name': name,
                                   'admin_state_up': True}}

        netw = neutron.create_network(body=body_sample)
        net_dict = netw['network']
        network_id = net_dict['id']
        ui.info_3('Network %s created' % network_id, ui.check)

        body_create_subnet = {'subnets':
                              [{'cidr': cidr, 'name': subnetname,
                                'ip_version': 4, 'network_id': network_id}]}

        subnet = neutron.create_subnet(body=body_create_subnet)
        ui.info_3('Created subnet %s' % subnet, ui.check)
    finally:
        ui.info_3("Execution completed", ui.check)


def list_subnets(args):
    '''list subnets'''
    ui.info_section(f'== List Subnets == \n')
    auth = identity.Password(auth_url=auth_url,
                             username=username,
                             password=password,
                             project_name=project_name,
                             project_domain_name=project_domain_name,
                             user_domain_name=user_domain_name)
    sess = session.Session(auth=auth)
    neutron = nwclient.Client(session=sess)
    list = neutron.list_subnets()
    # for list in neutron.list_networks():
    #     print(list)
    coba = json.dumps(list, sort_keys=True, indent=2)
    print(coba)
    # print(list)


def list_networks(args, nama=None):
    '''List Network'''
    auth = identity.Password(auth_url=auth_url,
                             username=username,
                             password=password,
                             project_name=project_name,
                             project_domain_name=project_domain_name,
                             user_domain_name=user_domain_name)
    sess = session.Session(auth=auth)
    neutron = nwclient.Client(session=sess)
    if nama is None:
        '''JIka nama tidak dimasukkan'''
        ui.info_section(f'== List Network == \n')
        list = neutron.list_networks()
        for list in neutron.list_networks()['networks']:
            print(list, '\n')
        # coba = json.dumps(list, sort_keys=True, indent=2)
        # print(coba)
    else:
        '''menampilkan satu list nama'''
        try:
            ui.info_section(f'== Detail Network {nama}== \n')
            neutron = nwclient.Client(session=sess)
            list = neutron.list_networks(name=nama)

            coba = json.dumps(list, sort_keys=True, indent=2)
            print(coba)
        except Exception as e:
            '''jika tidak ada nama'''
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)
            # for network in neutron.networks.list():
            #     print(network)


def delete_network(args, network_id):
    '''Hapus network'''
    ui.info_section(f'== Delete Network == \n')
    auth = identity.Password(auth_url=auth_url,
                             username=username,
                             password=password,
                             project_name=project_name,
                             project_domain_name=project_domain_name,
                             user_domain_name=user_domain_name)
    sess = session.Session(auth=auth)
    neutron = nwclient.Client(session=sess)
    # neutron.delete_network(network_id)
    try:
        '''memcoba'''
        neutron.delete_network(network_id)
        ui.info_3(f'Delete {network_id} success', ui.check)
    except Exception as e:
        '''jika gagal'''
        ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)


def create_route(args, name, ext_network, namesubnet):
    '''Membuat Routes'''
    '''Cmd : python test.py create_route cobaroute2 ext-net subnet3 '''
    try:
        ui.info_section(f'== Create Routes == \n')
        auth = identity.Password(auth_url=auth_url,
                                 username=username,
                                 password=password,
                                 project_name=project_name,
                                 project_domain_name=project_domain_name,
                                 user_domain_name=user_domain_name)
        sess = session.Session(auth=auth)
        neutron = nwclient.Client(session=sess)
        # mendapatkan id extnetwork
        net = neutron.list_networks(name=ext_network)
        id_network = net['networks'][0]['id']

        # mendapatkan id subnet
        subnet = neutron.list_subnets(name=namesubnet)
        subnet_id = subnet['subnets'][0]['id']
        neutron.format = 'json'
        request = {'router': {'name': name, 'external_gateway_info':
                              {"network_id": id_network},
                              'admin_state_up': True}}
        router = neutron.create_router(request)
        router_id = router['router']['id']
        # for example: '72cf1682-60a8-4890-b0ed-6bad7d9f5466'
        router = neutron.show_router(router_id)
        ui.info_3(router, ui.check)
        body = {'subnet_id': subnet_id}
        response = neutron.add_interface_router(
            router=router_id, body=body)

        ui.info_3(response, ui.check)
    finally:
        ui.info_3("Execution completed", ui.check)


def list_images(args):
    '''Daftar Images'''
    ui.info_section(f'== List Images == \n')
    loader = loading.get_plugin_loader('password')
    auth = loader.load_from_options(
        auth_url=auth_url,
        username=username,
        password=password,
        project_name=project_name,
        project_domain_name=project_domain_name,
        user_domain_name=user_domain_name
    )

    sess = session.Session(auth=auth)

    glance = glclient('2', session=sess)
    for image in glance.images.list():
        print(image)
        print('\n------\n')


def create_instance(args, name, flavors, image, network, securitygroups, keypairname):
    '''Membuat Instance'''
    try:
        ui.info_section(f'== Create Instance == \n')
        loader = loading.get_plugin_loader('password')
        auth = loader.load_from_options(
            auth_url=auth_url,
            username=username,
            password=password,
            project_name=project_name,
            project_domain_name=project_domain_name,
            user_domain_name=user_domain_name
        )

        sess = session.Session(auth=auth)
        nova_client = nvclient.Client('2', session=sess)

        image = nova_client.glance.find_image(image)
        flavor = nova_client.flavors.find(name=flavors)
        net = nova_client.neutron.find_network(name=network)
        nics = [{'net-id': net.id}]

        network = nwclient.Client(session=sess)
        sg = network.list_security_groups(name=securitygroups)
        id_sg = sg['security_groups'][0]['id']
        id_sg1 = print(id_sg)
        instance = nova_client.servers.create(name=name, image=image,
                                              flavor=flavor, key_name=keypairname,
                                              security_groups=id_sg1, nics=nics)
        # block_dev_mapping = {'vda':'uuid of the volume you want to use'}
        # https://ask.openstack.org/en/question/54104/create-an-instance-from-volume-in-openstach-with-python-novaclient/
        # https://stackoverflow.com/questions/27048292/create-an-instance-from-volume-in-openstach-with-python-novaclient/27136929#27136929
        # instance = nova.servers.create(name="python-test3", image='', block_device_mapping=block_dev_mapping,
        #                            flavor = flavor, key_name = "my-keypair", nics = nics)
        ui.info_3("Processing", ui.ellipsis)
        time.sleep(5)
        ui.info_3("Create Instance Success", ui.check)
        ui.info_3("List Instance : ")
        print(nova_client.servers.list())
    finally:
        ui.info_3("Execution Completed", ui.check)


def create_floatingip(args, ext_network, internal_ip):
    '''Membuat floating IP'''
    try:
        ui.info_section(f'== Create Floating Ip == \n')
        auth = identity.Password(auth_url=auth_url,
                                 username=username,
                                 password=password,
                                 project_name=project_name,
                                 project_domain_name=project_domain_name,
                                 user_domain_name=user_domain_name)
        sess = session.Session(auth=auth)
        neutron = nwclient.Client(session=sess)
        # mendapatkan id ext_network berdasarkan nama(external network)
        net = neutron.list_networks(name=ext_network)
        id_network = net['networks'][0]['id']
        # mendapatkan port id berdasarkan ip
        network = neutron.list_ports()['ports']

        tes = [
            elem['id'] for elem in network
            if(elem['fixed_ips'][0]['ip_address'] == internal_ip)
        ]

        port_id = tes[0]

        request = {
            "floatingip": {
                # ext network
                "floating_network_id": id_network,
                "port_id": port_id,
                "fixed_ip_address": internal_ip,
            }
        }
        floating_ip = neutron.create_floatingip(request)
        ui.info_3("Processing", floating_ip, ui.ellipsis)
        time.sleep(5)
        ui.info_3("Create Floating Ip Success", ui.check)
    finally:
        '''akhirnya'''
        ui.info_3("Execution Completed", ui.check)


def help(args, name=None):

    if(name == '-list_users'):
        print(list_users.__doc__)
    elif(name == '-create_project'):
        print(create_project.__doc__)
    elif(name == '-create_user'):
        print(create_user.__doc__)
    elif(name == '-update_user'):
        print(update_user.__doc__)
    elif(name == '-list_users'):
        print(list_users.__doc__)
    elif(name == '-list_projects'):
        print(list_projects.__doc__)
    elif(name == '-list_domains'):
        print(list_domains.__doc__)
    elif(name == '-grant_role'):
        print(grant_role.__doc__)
    elif(name == '-grant_role2'):
        print(grant_role2.__doc__)
    elif(name == '-create_network'):
        print(create_network.__doc__)
    elif(name == '-list_networks'):
        print(list_networks.__doc__)
    elif(name == '-create_instance'):
        print(create_instance.__doc__)
    elif(name == '-create_route'):
        print(create_router.__doc__)
    elif(name == '-create_floatingip'):
        print(create_floatingip.__doc__)
    elif(name == '-delete_users'):
        print(delete_users.__doc__)
    elif(name == '-delete_network'):
        print(delete_network.__doc__)
    elif(name == '-delete_project'):
        print(delete_project.__doc__)
    elif(name == '-revoke_role'):
        print(revoke_role.__doc__)
    elif(name == '-update_user'):
        print(update_user.__doc__)
    elif(name == '-delete_users'):
        print(update_users.__doc__)
    elif(name == '-update_project'):
        print(update_project.__doc__)
    elif name is None:
        print('')
        ui.info_1(
            'Untuk informasi command Anda bisa mengetik help <spasi> -cmd: \n')
        print(' -create_project \n -create_user \n -create_network \n -create_instance \n -create_route \n -create_floatingip')
        print(' -list_users \n -list_networks \n -list_projects \n -list_domains \n -list_images')
        print(' -grant_role \n -grant_role2 \n -delete_project \n -delete_network \n -delete_user \n -delete_users')
        print(' -update_user \n -update_project \n')
    else:
        print('command yang anda masukkan tidak tersedia')


if __name__ == "__main__":
    args = (sys.argv[1])

    if(args == 'login'):
        login(args)
    elif(args == 'create_project'):
        name = (sys.argv[2])
        domain = (sys.argv[3])
        description = (sys.argv[4])
        create_project(args, name, domain, description)
    elif(args == 'create_user'):
        if len(sys.argv) == 6:
            name = (sys.argv[2])
            domain = (sys.argv[3])
            project = (sys.argv[4])
            password = (sys.argv[5])
            create_user(args, name, domain, project, password)
        elif len(sys.argv) == 7:
            name = (sys.argv[2])
            domain = (sys.argv[3])
            project = (sys.argv[4])
            password = (sys.argv[5])
            email = (sys.argv[6])
            create_user(args, name, domain, project, password,
                        email)
        else:
            name = (sys.argv[2])
            domain = (sys.argv[3])
            project = (sys.argv[4])
            password = (sys.argv[5])
            email = (sys.argv[6])
            description = (sys.argv[7])
            create_user(args, name, domain, project, password,
                        email, description)
    elif(args == 'update_user'):
        if len(sys.argv) == 7:
            user = (sys.argv[2])
            name = (sys.argv[3])
            domain = (sys.argv[4])
            project = (sys.argv[5])
            password = (sys.argv[6])
            update_user(args, user, name, domain, project, password)
        elif len(sys.argv) == 8:
            user = (sys.argv[2])
            name = (sys.argv[3])
            domain = (sys.argv[4])
            project = (sys.argv[5])
            password = (sys.argv[6])
            email = (sys.argv[7])
            update_user(args, user, name, domain, project, password,
                        email)
        else:
            user = (sys.argv[2])
            name = (sys.argv[3])
            domain = (sys.argv[4])
            project = (sys.argv[5])
            password = (sys.argv[6])
            email = (sys.argv[7])
            description = (sys.argv[8])
            update_user(args, user, name, domain, project, password,
                        email, description)
    elif(args == 'list_roles'):
        list_roles(args)
    elif(args == 'list_users'):
        if len(sys.argv) == 2:
            list_users(args)
        else:
            name = (sys.argv[2])
            list_users(args, name)
    elif(args == 'list_projects'):
        list_projects(args)
    elif(args == 'list_domains'):
        list_domains(args)
    elif(args == 'grant_role'):
        role = (sys.argv[2])
        user = (sys.argv[3])
        project = (sys.argv[4])
        grant_role(args, role, user, project)
    elif(args == 'create_network'):
        name = (sys.argv[2])
        subnetname = (sys.argv[3])
        cidr = (sys.argv[4])
        create_network(args, name, subnetname, cidr)
    elif(args == 'list_networks'):
        if len(sys.argv) == 2:
            list_networks(args)
        else:
            nama = (sys.argv[2])
            list_networks(args, nama)
    elif(args == 'delete_network'):
        network_id = (sys.argv[2])
        delete_network(args, network_id)
    elif(args == 'delete_project'):
        name = (sys.argv[2])
        delete_project(args, name)
    elif(args == 'create_route'):
        name = (sys.argv[2])
        ext_network = (sys.argv[3])
        namesubnet = (sys.argv[4])
        create_route(args, name, ext_network, namesubnet)
    elif(args == 'list_images'):
        list_images(args)
    elif(args == 'grant_role2'):
        role = (sys.argv[2])
        user = (sys.argv[3])
        project = (sys.argv[4])
        grant_role2(args, role, user, project)
    elif(args == 'create_instance'):
        name = (sys.argv[2])
        flavors = (sys.argv[3])
        image = (sys.argv[4])
        network = (sys.argv[5])
        securitygroups = (sys.argv[6])
        keypairname = (sys.argv[7])
        create_instance(args, name, flavors, image, network,
                        securitygroups, keypairname)
    elif(args == 'create_floatingip'):
        ext_network = (sys.argv[2])
        internal_ip = (sys.argv[3])
        create_floatingip(args, ext_network, internal_ip)
    elif(args == 'list_subnets'):
        list_subnets(args)
    elif(args == 'revoke_role'):
        role = (sys.argv[2])
        user = (sys.argv[3])
        project = (sys.argv[4])
        revoke_role(args, role, user, project)
    elif(args == 'update_project'):
        if len(sys.argv) == 4:
            name = (sys.argv[2])
            nameedit = (sys.argv[3])
            update_project(args, name, nameedit)
        else:
            name = (sys.argv[2])
            nameedit = (sys.argv[3])
            description = (sys.argv[4])
            update_project(args, name, nameedit, description)
    elif(args == 'delete_user'):
        delete_user(args)
    elif(args == 'delete_users'):
        users = sys.argv[2:]
        delete_users(args, *users)
    elif(args == 'help'):
        if len(sys.argv) == 2:
            help(args)
        else:
            name = (sys.argv[2])
            help(args, name)
    else:
        print("Keyword salah")
