import sys
import os
import ui
import json
import requests
import subprocess


def token(args):
    url = "http://rocky-controller.jcamp.net:5000/v3/auth/tokens"
    # json_data = open('data.txt', 'r').read()
    # data = json.loads(json_data)
    data = """{
        "auth": {
            "identity": {
            "methods": ["password"],
                "password": {
                    "user": {
                        "domain": {
                        "name": "Default"
                        },
                        "name": "irvan",
                        "password": "M0nalisa"
                        }
                    }
                },
            "scope": {
                "project": {
                    "domain": {
                        "name": "Default"
                    },
                    "name": "irvan"
                }
            }
        }
    }"""
    r = requests.post(url, data)
    OS_TOKEN = r.headers['X-Subject-Token']
    # os.environ["test"] = "gugugu"
    # j = json.loads(r.content)
    print(f'Token = {OS_TOKEN}')
    subprocess.run("export mi='sdsdww'", shell=True, check=True)
    # os.system("bash")


def instance(args, id=None):
    r = os.environ.get("OS_TOKEN")
    header = {'X-Auth-Token': r}
    if id is None:
        ui.info_section('== List instance ==\n')
        instance = requests.get(
            "http://rocky-controller.jcamp.net:8774/v2.1/servers", headers=header)
        readjson = json.loads(instance.content)
        coba = json.dumps(readjson, sort_keys=True, indent=2)
        print(coba)
    elif id == "create":
        ui.info_section('== Create Instance == \n')
        url = "http://rocky-controller.jcamp.net:8774/v2.1/servers"
        data = """
        {
            "server": {
                "name": "percobaan",
                "imageRef": "82189ef1-2c20-475c-9d40-325eb567df56",
                "flavorRef": "afc68ef6-1985-4d59-ac63-a6f2c4405756",
                "availability_zone": "nova",
                "key_name": "Laptop Hp",
                "OS-DCF:diskConfig": "AUTO",
                "networks": [{
                    "uuid": "4b73b027-0231-42e8-9253-153f342119d9"
                }],
                "security_groups": [{
                    "name": "default"
                }]
            }
        }
        """
        ui.info('loading', ui.ellipsis)
        r = requests.post(url, data, headers=header)
        readjson = json.loads(r.content)
        coba = json.dumps(readjson, sort_keys=True, indent=2)
        print(coba)
        ui.info_3('\n Done ', ui.check)
    else:
        try:
            ui.info_section(ui.bold, '== Detail Image == \n')
            images = requests.get(
                f"http://rocky-controller.jcamp.net:8774/v2.1/servers/{id}", headers=header)
            readjson = json.loads(images.content)
            showjson = json.dumps(readjson, sort_keys=True, indent=2)
            print(showjson)
        except ValueError as e:
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)
            ui.info("Id Image tidak ada")


def flavors(args):
    # os.system("echo $oke")
    print("== List Flavor ==\n")
    r = os.environ.get("OS_TOKEN")
    # print(os.environ.get("OS_TOKEN"))
    header = {'X-Auth-Token': r}

    flavors = requests.get(
        "http://rocky-controller.jcamp.net:8774/v2.1/flavors", headers=header)
    readjson = json.loads(flavors.content)
    showjson = json.dumps(readjson, sort_keys=True, indent=2)
    print(showjson)


def network(args):
    print("== List Network ==\n")
    r = os.environ.get("OS_TOKEN")
    # print(os.environ.get("OS_TOKEN"))
    header = {'X-Auth-Token': r}

    networks = requests.get(
        "http://rocky-controller.jcamp.net:9696/v2.0/networks", headers=header)
    readjson = json.loads(networks.content)
    showjson = json.dumps(readjson, sort_keys=True, indent=2)
    print(showjson)


def images(args, id=None):
    r = os.environ.get("OS_TOKEN")
    # print(os.environ.get("OS_TOKEN"))
    header = {'X-Auth-Token': r}

    if id is None:
        try:
            ui.info_section(ui.bold, '== List Image == \n')
            images = requests.get(
                "http://rocky-controller.jcamp.net:9292/v2/images", headers=header)
            readjson = json.loads(images.content)
            showjson = json.dumps(readjson, sort_keys=True, indent=2)
            print(showjson)
        except ValueError as e:
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)
    else:
        try:
            ui.info(ui.bold, "== Detail Image == \n")
            images = requests.get(
                f"http://rocky-controller.jcamp.net:9292/v2/images/{id}", headers=header)
            readjson = json.loads(images.content)
            showjson = json.dumps(readjson, sort_keys=True, indent=2)
            print(showjson)
        except ValueError as e:
            ui.info(ui.red, ui.bold, 'Error: ', ui.reset, e)
            ui.info("Id Image tidak ada")


if __name__ == "__main__":
    args = (sys.argv[1])

    if(args == "token"):
        token(args)
    elif(args == "flavors"):
        flavors(args)
    elif(args == "instance"):
        if len(sys.argv) == 2:
            instance(args)
        elif (sys.argv[2]) == "create":
            tes = "create"
            instance(args, tes)
        else:
            tes = (sys.argv[2])
            instance(args, tes)
    elif(args == "network"):
        network(args)
    elif(args == "image"):
        if len(sys.argv) == 2:
            images(args)
        else:
            tes = (sys.argv[2])
            images(args, tes)

    else:
        print("Keyword salah")
