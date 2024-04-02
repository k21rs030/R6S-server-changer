import configparser
config=configparser.ConfigParser()
config_location= "Random ID"
config.read(config_location)
from time import sleep


options="""default (ping based)
playfab/australiaeast
playfab/brazilsouth
playfab/centralus
playfab/eastasia
playfab/eastus
playfab/japaneast
playfab/northeurope
playfab/southafricanorth
playfab/southcentralus
playfab/southeastasia
playfab/uaenorth
playfab/westeurope
playfab/westus""".split("\n")

for number, option in enumerate(options):
    print(str(number)+": ", option)
print("curent location is >>> " + config["ONLINE"]["DATACENTERHINT"])
while True:
    selected = input("set server as (ctrl_c to cancel)>>> ")
    try:
        selected=int(selected)
        config["ONLINE"]["DataCenterHint"]=options[selected]
        print("set server as: " + config["ONLINE"]["DataCenterHint"])
        with open(config_location,"w") as f:
            config.write(f)
        break
    except KeyboardInterrupt:
        print("! closed config without updating")
    except ValueError:
        print("? not an available option, try again")

sleep(2)
