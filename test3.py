import sys
import os
import ui
import json
import requests
import subprocess


def images(args, id=None):
    r = os.environ.get("OS_TOKEN")
    # print(os.environ.get("OS_TOKEN"))
    header = {
        'X-Auth-Token': r,
        "Content-Type": "application/json"
    }

    if id is None:
        print("== List Image == \n")
    elif id == "create":
        print("== create Image == \n")
        url = "http://rocky-controller.jcamp.net:8774/v2.1/servers"
        data = """
        {
            "server": {
                "name": "cobabuatlg",
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
        ui.info("loading .. \n")
        requests.post(url, data, headers=header)
        ui.info_3("::done::")
    else:
        try:
            print("== Detail Image == \n")
            images = requests.get(
                f"http://rocky-controller.jcamp.net:9292/v2/images/{id}", headers=header)
            readjson = json.loads(images.content)
            showjson = json.dumps(readjson, sort_keys=True, indent=2)
            print(showjson)
        except ValueError as e:
            ui.info(ui.red, 'Error: ', ui.reset, e)
            ui.info("Id Image tidak ada")


if __name__ == "__main__":
    args = (sys.argv[1])

    if(args == "image"):
        if len(sys.argv) == 2:
            images(args)
        elif (sys.argv[2]) == "create":
            tes = "create"
            images(args, tes)
        else:
            tes = (sys.argv[2])
            images(args, tes)
