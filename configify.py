import json, os

def config():
    with open(f"{os.environ['SLAROSDIR']}/sysconfig.json") as f:
        sysconfig = json.load(f)
    if sysconfig["lightmode"] == "yes":
        color1 = (255, 255, 255)
        color2 = (0, 0, 0)
    else:
        color2 = (255, 255, 255)
        color1 = (0, 0, 0)

    return color1, color2