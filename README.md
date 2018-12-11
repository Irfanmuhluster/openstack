# openstack
Akses CRUD Openstack Neuron, Nova, Glance, keystone dengan Openstack Phyton Binding

***Update dulu ..***
**Create Project di buat di proyek Admin:**

```
(openstack-awBtF08N)  ✘ ★  Documents/Development/openstack  python test.py create_project irvan3 default coba...
create project
* <Project description=coba..., domain_id=default, enabled=True, id=a5406b8f8beb4478917f99b18d4dea48, is_domain=False, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/projects/a5406b8f8beb4478917f99b18d4dea48'}, name=irvan3, parent_id=default, tags=[]> 

* 
 Done  ✓ 

```
**Grant Proyek yang baru dibuat:**
python namafile.py cmd idmember iduser idproyek

```
python test.py grant_role adc3f57d47234406a0c6440b3bf07827 11517d688b954c758ddc2219b8b601d5 a5406b8f8beb4478917f99b18d4dea48
* 
 Done  ✓ 
```
login ke proyek baru//

**List Network:**
```
(openstack-awBtF08N)  ★  Documents/Development/openstack  python test.py list_networks
== List Network == 

---------------------

{'status': 'ACTIVE', 'router:external': False, 'availability_zone_hints': [], 'availability_zones': ['nova'], 'ipv4_address_scope': None, 'description': '', 'port_security_enabled': True, 'subnets': ['e0755bd4-3f14-431a-827c-7f3926551375'], 'updated_at': '2018-11-15T03:48:07Z', 'tenant_id': 'a131ae109e6c4927855b0e316410e444', 'created_at': '2018-11-15T03:48:06Z', 'tags': [], 'ipv6_address_scope': None, 'mtu': 1500, 'revision_number': 2, 'admin_state_up': True, 'shared': False, 'project_id': 'a131ae109e6c4927855b0e316410e444', 'id': '2c656fa0-0dc9-4148-80a2-a428b2bfb1f8', 'name': 'cobanetwork3'} 

{'status': 'ACTIVE', 'router:external': False, 'availability_zone_hints': [], 'availability_zones': ['nova'], 'ipv4_address_scope': None, 'description': '', 'port_security_enabled': True, 'subnets': ['3bb52fb4-46a5-443f-83db-019d8a4411f5'], 'updated_at': '2018-11-12T02:36:28Z', 'tenant_id': 'a131ae109e6c4927855b0e316410e444', 'created_at': '2018-11-12T02:36:27Z', 'tags': [], 'ipv6_address_scope': None, 'mtu': 1500, 'revision_number': 2, 'admin_state_up': True, 'shared': False, 'project_id': 'a131ae109e6c4927855b0e316410e444', 'id': 'a30b33d6-de34-4954-8445-ded87276cc59', 'name': 'cobanetwork2'} 

{'status': 'ACTIVE', 'router:external': True, 'availability_zone_hints': [], 'availability_zones': ['nova'], 'ipv4_address_scope': None, 'description': '', 'port_security_enabled': True, 'subnets': ['4639e018-1cc1-49cc-89d4-4cad49bd4b89'], 'updated_at': '2018-10-19T06:51:26Z', 'tenant_id': '8c3ff5ffe6794b1db42fca2d8fc45104', 'created_at': '2018-10-19T06:51:25Z', 'tags': [], 'ipv6_address_scope': None, 'mtu': 1500, 'is_default': False, 'revision_number': 1, 'admin_state_up': True, 'shared': True, 'project_id': '8c3ff5ffe6794b1db42fca2d8fc45104', 'id': 'd10dd06a-0425-49eb-a8ba-85abf55ac0f5', 'name': 'ext-net'} 
```
**Create Network**
```
(openstack-awBtF08N)  ★  Documents/Development/openstack  python test.py create_network cobanetwork3 subnet3 192.168.49.0/24        
== Create Network cobanetwork3== 

-----------------------------------

* Network 2c656fa0-0dc9-4148-80a2-a428b2bfb1f8 created ✓ 
* Created subnet {'subnets': [{'service_types': [], 'description': '', 'enable_dhcp': True, 'tags': [], 'network_id': '2c656fa0-0dc9-4148-80a2-a428b2bfb1f8', 'tenant_id': 'a131ae109e6c4927855b0e316410e444', 'created_at': '2018-11-15T03:48:07Z', 'dns_nameservers': [], 'updated_at': '2018-11-15T03:48:07Z', 'gateway_ip': '192.168.49.1', 'ipv6_ra_mode': None, 'allocation_pools': [{'start': '192.168.49.2', 'end': '192.168.49.254'}], 'host_routes': [], 'revision_number': 0, 'ip_version': 4, 'ipv6_address_mode': None, 'cidr': '192.168.49.0/24', 'project_id': 'a131ae109e6c4927855b0e316410e444', 'id': 'e0755bd4-3f14-431a-827c-7f3926551375', 'subnetpool_id': None, 'name': 'subnet3'}]} ✓ 
* Execution completed ✓ 

```
**Create Routes**
```

(openstack-awBtF08N)  ✘ ★  Documents/Development/openstack  python test.py create_route cobaroute2 ext-net subnet3     
== Create Routes == 

----------------------

* {'router': {'status': 'ACTIVE', 'external_gateway_info': {'network_id': 'd10dd06a-0425-49eb-a8ba-85abf55ac0f5', 'enable_snat': True, 'external_fixed_ips': [{'subnet_id': '4639e018-1cc1-49cc-89d4-4cad49bd4b89', 'ip_address': '103.30.145.205'}]}, 'availability_zone_hints': [], 'availability_zones': ['nova'], 'description': '', 'tags': [], 'tenant_id': 'a131ae109e6c4927855b0e316410e444', 'created_at': '2018-11-15T03:56:48Z', 'admin_state_up': True, 'updated_at': '2018-11-15T03:56:50Z', 'flavor_id': None, 'revision_number': 2, 'routes': [], 'project_id': 'a131ae109e6c4927855b0e316410e444', 'id': 'af42f18c-32e8-4ad6-81db-36a71108f33c', 'name': 'cobaroute2'}} ✓ 
* {'network_id': '2c656fa0-0dc9-4148-80a2-a428b2bfb1f8', 'tenant_id': 'a131ae109e6c4927855b0e316410e444', 'subnet_id': 'e0755bd4-3f14-431a-827c-7f3926551375', 'subnet_ids': ['e0755bd4-3f14-431a-827c-7f3926551375'], 'port_id': '61bebefc-681b-4052-b74f-fd6ceacdca23', 'id': 'af42f18c-32e8-4ad6-81db-36a71108f33c'} ✓ 
* Execution completed ✓ 

```
**Membuat Instance:**
Python file.py cmd namainstances namaflavors namaimage namanetwork namasecuritygroup "namakeypairs"
```

(openstack-awBtF08N)  ★  Documents/Development/openstack  python test.py create_instance instance2 jc010120 CentOS-7-x86_64-GenericCloud cobanetwork2 default "Laptop Hp"
== Create Instance == 

------------------------

934557fe-1be7-447e-842b-95a92d3d7f0a
* Processing … 
* Create Instance Success ✓ 
* List Instance : 
[<Server: instance2>, <Se
```rver: instance1>]
* Execution Completed ✓ 

 **Create Floating IP** 
python namafile cmd ip_ext ip_int

```
(openstack-awBtF08N)  ✘ ★  Documents/Development/openstack  python test.py create_floatingip ext-net 192.168.80.5
== Create Floating Ip == 

---------------------------

* Processing {'floatingip': {'router_id': '8450aa50-6660-4df5-8adf-be86558fdd0b', 'status': 'DOWN', 'description': '', 'tags': [], 'tenant_id': 'a131ae109e6c4927855b0e316410e444', 'created_at': '2018-11-15T10:04:38Z', 'updated_at': '2018-11-15T10:04:38Z', 'floating_network_id': 'd10dd06a-0425-49eb-a8ba-85abf55ac0f5', 'port_details': {'status': 'ACTIVE', 'name': '', 'admin_state_up': True, 'network_id': 'a30b33d6-de34-4954-8445-ded87276cc59', 'device_owner': 'compute:nova', 'mac_address': 'fa:16:3e:c2:ad:8a', 'device_id': '39752f95-84ce-4e7e-923d-427f53dd62de'}, 'fixed_ip_address': '192.168.80.5', 'floating_ip_address': '103.30.145.216', 'revision_number': 0, 'project_id': 'a131ae109e6c4927855b0e316410e444', 'port_id': '25118769-1253-4d9e-9e33-6987bc0b1533', 'id': '4165abdb-8556-4487-bff1-5493b5aff121'}} … 
* Create Floating Ip Success ✓ 
* Execution Completed ✓ 

```
**Update project:**

```
(openstack-awBtF08N)  ★  Documents/Development/openstack  python test.py update_project irvan4 irvan5 update...
== update project irvan4== 

-----------------------------

* <Project description=update..., domain_id=default, enabled=True, extra={}, id=49c2bca80c064aa8bed3fc6f67917d04, is_domain=False, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/projects/49c2bca80c064aa8bed3fc6f67917d04'}, name=irvan5, parent_id=default, tags=[]> 

* 
 Done  ✓ 
```

**Delete Project:**

```
(openstack-awBtF08N)  ★  Documents/Development/openstack  python test.py delete_project irvan5                      
== Delete Project irvan5 == 

------------------------------

* Delete 49c2bca80c064aa8bed3fc6f67917d04 success ✓ 

```

**Revoke Role**
```

(openstack-awBtF08N)  ★  Documents/Development/openstack  python test.py revoke_role user irvan irvan3
* revoke role success ✓ 
* (<Response [204]>, None) 

* Done  ✓ 
```

**Create User**
python namafile.py cmd namauser domain_id id_project password email(opsional) deskripsi(opsional)
```
(openstack-awBtF08N)  ✘ ★  Documents/Development/openstack  python test.py create_user irvan6 default 6bd9cebb746c420783039ce7606f8aa1 M0nalisa               
== Create User == 

--------------------

* <User default_project_id=6bd9cebb746c420783039ce7606f8aa1, domain_id=default, enabled=True, id=d69e3e7c21d94fbda03ec01391e3b992, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/d69e3e7c21d94fbda03ec01391e3b992'}, name=irvan6, options={}, password_expires_at=None> 

* 
 Done  ✓ 
(openstack-awBtF08N)  ★  Documents/Development/openstack  python test.py create_user irvan7 default 6bd9cebb746c420783039ce7606f8aa1 M0nalisa testemail@gmail.com
== Create User == 

--------------------

* <User default_project_id=6bd9cebb746c420783039ce7606f8aa1, domain_id=default, email=testemail@gmail.com, enabled=True, id=61eb9b27b4c845559d84118034d34ab9, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/61eb9b27b4c845559d84118034d34ab9'}, name=irvan7, options={}, password_expires_at=None> 

* 
 Done  ✓ 
(openstack-awBtF08N)  ★  Documents/Development/openstack  python test.py create_user irvan8 default 6bd9cebb746c420783039ce7606f8aa1 M0nalisa testemail@gmail.com fojijbgigtr
== Create User == 

--------------------

* <User default_project_id=6bd9cebb746c420783039ce7606f8aa1, description=fojijbgigtr, domain_id=default, email=testemail@gmail.com, enabled=True, id=92ea7d1feef44994a3464dd82ebf718a, links={'self': 'http://rocky-controller.jcamp.net:5000/v3/users/92ea7d1feef44994a3464dd82ebf718a'}, name=irvan8, options={}, password_expires_at=None> 

* 
 Done  ✓ 
```

**Delete beberapa Users berdasarkan nama**
python namafile.py cmd namauser1 namauser2

```
(openstack-awBtF08N)  ★  Documents/Development/openstack  python test.py delete_users irvan5 irvan6
== Delete Users== 

--------------------

*  -----
* Deleting Users 59967e71c49346a3bf52c8701e012cd0 
 … 
* (<Response [204]>, None) 

* Delete Seucces ✓ 
*  -----
* Deleting Users 9a03277e70274c8fbd02fd5f08fe40e2 
 … 
* (<Response [204]>, None) 

* Delete Seucces ✓ 


```

