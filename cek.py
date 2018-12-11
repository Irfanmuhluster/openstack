import sys
import itertools
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


def whm_list_accounts(arg):
    '''
    fungsi low level whmapi1
    return nya sebuah list
    '''
    # id = []
    cek2 = "[<User default_project_id=56a2cb6964d94577af24a7aa0269f25e, description=dibikin pake api3.py, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=48709c0294184454a0a2be2e60cb3283, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/48709c0294184454a0a2be2e60cb3283'}, name=aji6, options={}, password_expires_at=None>, <User domain_id=default, enabled=True, id=dc1c1313279347bc82bb60862d1e70e0, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/dc1c1313279347bc82bb60862d1e70e0'}, name=myuser, options={}, password_expires_at=None>, <User domain_id=default, enabled=True, id=bd70a58ce2aa48908684e666922888ce, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/bd70a58ce2aa48908684e666922888ce'}, name=glance, options={}, password_expires_at=None>, <User domain_id=default, enabled=True, id=40f0d6ff67f643d3b4640d7fe7d0a709, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/40f0d6ff67f643d3b4640d7fe7d0a709'}, name=nova, options={}, password_expires_at=None>, <User domain_id=default, enabled=True, id=80de48f643c3405e88761483aa8e5490, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/80de48f643c3405e88761483aa8e5490'}, name=placement, options={}, password_expires_at=None>, <User domain_id=default, enabled=True, id=8570d22e3fb14e32b5900072b9fd9151, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/8570d22e3fb14e32b5900072b9fd9151'}, name=neutron, options={}, password_expires_at=None>, <User default_project_id=49b51908c2424ce28f5ac922be2da36c, domain_id=default, email=fajar.4w@gmail.com, enabled=True, id=32983e36c8a248ca859b2e2ad981a91b, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/32983e36c8a248ca859b2e2ad981a91b'}, name=mbog, options={}, password_expires_at=None>, <User default_project_id=56a2cb6964d94577af24a7aa0269f25e, description=dibikin pake api3.py, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=6f71ce681c624915b99bf35829e086ad, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/6f71ce681c624915b99bf35829e086ad'}, name=aji5, options={}, password_expires_at=None>, <User default_project_id=56a2cb6964d94577af24a7aa0269f25e, description=dibikin pake api3.py, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=0c394bb284b74c0cbf3fd9879eb1be2c, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/0c394bb284b74c0cbf3fd9879eb1be2c'}, name=aji4, options={}, password_expires_at=None>, <User default_project_id=56a2cb6964d94577af24a7aa0269f25e, description=dibikin pake api3.py, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=f6df8190ceeb47a1a513c85dfa328e91, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/f6df8190ceeb47a1a513c85dfa328e91'}, name=aji3, options={}, password_expires_at=None>, <User default_project_id=56a2cb6964d94577af24a7aa0269f25e, description=dibikin pake api3.py, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=de4656ecd25f41a79963154639f1d826, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/de4656ecd25f41a79963154639f1d826'}, name=[6~aji4, options={}, password_expires_at=None>, <User default_project_id=8c3ff5ffe6794b1db42fca2d8fc45104, domain_id=default, email=, enabled=True, id=6aa8a9c2eb514577ab768bd7bdad71af, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/6aa8a9c2eb514577ab768bd7bdad71af'}, name=admin, options={}, password_expires_at=None>, <User default_project_id=56a2cb6964d94577af24a7aa0269f25e, description=dibikin pake api3.py, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=893b76734d354e339dc795b590e7baeb, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/893b76734d354e339dc795b590e7baeb'}, name=ajio4, options={}, password_expires_at=None>, <User createdby=aji2, description=dibikin pake api3.py, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=a77efcc49b3a483da5cf1d1ced01e13b, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/a77efcc49b3a483da5cf1d1ced01e13b'}, name=user.aji, options={}, password_expires_at=None>, <User default_project_id=82f25d549c774d1eaf9c0b9b45079e7b, domain_id=default, email=, enabled=True, id=11517d688b954c758ddc2219b8b601d5, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/11517d688b954c758ddc2219b8b601d5'}, name=irvan, options={}, password_expires_at=None>, <User default_project_id=6c39ed979c504f62ad406c946292ff3d, domain_id=default, enabled=True, id=ebf9a86b2d094f31b61ce18794120196, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/ebf9a86b2d094f31b61ce18794120196'}, name=adhi, options={}, password_expires_at=None>, <User default_project_id=f4aa63dc85294d5abe97010d7ae057e0, domain_id=default, enabled=True, id=384f038da28d4baa91d0d8ba7f20b64b, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/384f038da28d4baa91d0d8ba7f20b64b'}, name=jajalan, options={}, password_expires_at=None>, <User createdby=aji2, description=dibikin pake api3.py, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=2f7434267dc3481988244a466eba2822, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/2f7434267dc3481988244a466eba2822'}, name=user2.aji, options={}, password_expires_at=None>, <User createdby=aji2, description=dibikin pake api3.py, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=d31e526b513344a692b4e1cd31826c83, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/d31e526b513344a692b4e1cd31826c83'}, name=user3.aji, options={}, password_expires_at=None>, <User domain_id=default, enabled=True, id=10464ae0164749fdb25d6515862133b2, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/10464ae0164749fdb25d6515862133b2'}, name=help, options={}, password_expires_at=None>, <User createdby=admin, default_project_id=1c9f9000989b41939b18f670a8792bd8, description=dibikin pake api3.py, domain_id=7116d90f0d1446bd95a6be3d34341680, enabled=True, id=e17dc8e867a44cdfacaacde1cf6802fd, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/e17dc8e867a44cdfacaacde1cf6802fd'}, name=user.aji, options={}, password_expires_at=None>, <User default_project_id=c0b89f614b5a457cb5acef8fe8c2b320, domain_id=default, email=haryadi@jogjacamp.co.id, enabled=True, id=2661ef095ffc4899a62cd8afd8b422fc, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/2661ef095ffc4899a62cd8afd8b422fc'}, name=aji, options={}, password_expires_at=None>, <User createdby=admin, default_project_id=1c9f9000989b41939b18f670a8792bd8, description=dibikin pake api3.py, domain_id=default, enabled=True, id=9bb859eb47e04369b6a02da7d4e8f8aa, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/9bb859eb47e04369b6a02da7d4e8f8aa'}, name=user.aji, options={}, password_expires_at=None>, <User default_project_id=ba0fcb3be0d54a47b3439efbf474a0e7, description=create by irvan, domain_id=7116d90f0d1446bd95a6be3d34341680, enabled=True, id=57ceac3c118f4311a3a6a054dfb25d2b, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/57ceac3c118f4311a3a6a054dfb25d2b'}, name=Rosalina, options={}, password_expires_at=None>, <User default_project_id=56a2cb6964d94577af24a7aa0269f25e, description=bikin pake python keystoneclient, domain_id=449309895ba3410cb0d565bba1342b93, email=haryadi@jogjacamp.co.id, enabled=True, id=1c79eb43981a42998e5d239d20b310df, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/1c79eb43981a42998e5d239d20b310df'}, name=aji2, options={}, password_expires_at=None>, <User default_project_id=8c3ff5ffe6794b1db42fca2d8fc45104, description=bino oetomo, domain_id=default, email=bino@jogjacamp.co.id, enabled=True, id=b5e8583dffa942b38bc08fda9f26d87f, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/b5e8583dffa942b38bc08fda9f26d87f'}, name=bino, options={}, password_expires_at=None>, <User default_project_id=6bd9cebb746c420783039ce7606f8aa1, description=cobairvan4, domain_id=default, email=irfan4@gmail.com, enabled=True, id=83cadda8794743e7923821a38fea2683, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/83cadda8794743e7923821a38fea2683'}, name=irvan4, options={}, password_expires_at=None>, <User createdby=aji, default_project_id=33adf9c09bab4d4e84371879ce6a2839, description=dibikin pake api3.py, domain_id=f5787a7b36ab4437850beff84c41aaec, enabled=True, id=c0ee686f7b37458290e80a9251567937, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/c0ee686f7b37458290e80a9251567937'}, name=aji3, options={}, password_expires_at=None>, <User default_project_id=6bd9cebb746c420783039ce7606f8aa1, description=cobairvan3, domain_id=default, email=testemail@gmail.com, enabled=True, id=4e986e27112d4465bdaa368580992283, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/4e986e27112d4465bdaa368580992283'}, name=irvan3, options={}, password_expires_at=None>, <User default_project_id=696c0d55ce374ab581ae17fd269e776f, domain_id=449309895ba3410cb0d565bba1342b93, enabled=True, id=e0afec8e7f0c481398cdb055949b18f4, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/e0afec8e7f0c481398cdb055949b18f4'}, name=test.aji, options={}, password_expires_at=None>, <User domain_id=fbbe15c29bb44a99a00b2a66458e9786, enabled=True, id=d4eb8f2a79d544f98fc308ead73dd67b, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/d4eb8f2a79d544f98fc308ead73dd67b'}, name=jasmine, options={}, password_expires_at=None>, <User description=dibikin pake api3.py, domain_id=3b933e86a4ea4fffbd688a52de24b31c, enabled=True, id=64705ff9c887462f9c3172803d164570, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/64705ff9c887462f9c3172803d164570'}, name=aji4, options={}, password_expires_at=None>, <User description=dibikin pake api3.py, domain_id=cd2ee5b4f8744b2aa57708a7dd2580f0, enabled=True, id=6c93648f42e14c1d9bc857381f6e89cc, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/6c93648f42e14c1d9bc857381f6e89cc'}, name=aji4, options={}, password_expires_at=None>, <User default_project_id=696c0d55ce374ab581ae17fd269e776f, domain_id=3b933e86a4ea4fffbd688a52de24b31c, enabled=True, id=a3d762eabf834ac4aa8e11a9f212da7b, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/a3d762eabf834ac4aa8e11a9f212da7b'}, name=aji3, options={}, password_expires_at=None>, <User domain_id=default, enabled=True, id=e101409fe039499981e6be603f29aa2d, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/e101409fe039499981e6be603f29aa2d'}, name=irvan2, options={}, password_expires_at=None>, <User default_project_id=1c9f9000989b41939b18f670a8792bd8, description=dibikin pake api3.py, domain_id=default, enabled=True, id=094033f8618a410686337c222569345f, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/094033f8618a410686337c222569345f'}, name=aji3, options={}, password_expires_at=None>, <User default_project_id=1c9f9000989b41939b18f670a8792bd8, description=dibikin pake api3.py, domain_id=default, enabled=True, id=12407755ed2348e2b440a1e39f5d724d, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/12407755ed2348e2b440a1e39f5d724d'}, name=ajiajiaji, options={}, password_expires_at=None>, <User default_project_id=1c9f9000989b41939b18f670a8792bd8, description=dibikin pake api3.py, domain_id=default, enabled=True, id=c97c3d003e0f4b27ac96d1b01fa8cd14, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/c97c3d003e0f4b27ac96d1b01fa8cd14'}, name=ajiaji, options={}, password_expires_at=None>, <User default_project_id=1c9f9000989b41939b18f670a8792bd8, description=dibikin pake api3.py, domain_id=default, enabled=True, id=8171c5c0ad034389b36775bb069407a9, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/8171c5c0ad034389b36775bb069407a9'}, name=aji4, options={}, password_expires_at=None>]"
    baca = cek2.strip().split(',')
    id = [i for i in baca if i.startswith(' name')]

    # mencari id:
    baca2 = cek2.strip().split(',')
    name = [i for i in baca2 if i.startswith(' id')]

    print(id)
    # print(dict(enumerate(id)))
    print(name)


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
            print(list['name'])
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


def cek(args):
    for x in whm_list_accounts(args):
        print(x['id'])


if __name__ == "__main__":
    args = (sys.argv[1])

    if(args == 'list_users'):
        # nomer = sys.argv[2:]
        list_users(args)
    elif(args == 'whm_list_accounts'):
        whm_list_accounts(args)
    elif(args == 'cek'):
        cek(args)
    elif(args == 'list_networks'):
        if len(sys.argv) == 2:
            list_networks(args)
        else:
            nama = (sys.argv[2])
            list_networks(args, nama)
    else:
        print('keyword salah')
