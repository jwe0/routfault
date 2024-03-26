import json


"""

This program searches the database given by the parser

"""


art = """
╦═╗╔═╗╦ ╦╔╦╗╔═╗╔═╗╦ ╦╦ ╔╦╗
╠╦╝║ ║║ ║ ║ ╠╣ ╠═╣║ ║║  ║ 
╩╚═╚═╝╚═╝ ╩ ╚  ╩ ╩╚═╝╩═╝╩ 
> A default router password enumerator
> Developed by /jwe0
> Run &help for commands
"""

print(art)


while True:

    name = input("[COMND] > ")


    if name == "&models":
        print()
        for model in config:
            print(f"[MODEL] > {model}")
        print() 

    elif "&search " in name:


        with open("database.json") as f:
            config = json.load(f)

            model = name.split(" ")[1].lower()

            if model in config:

                username = config[model]["username"]
                password = config[model]["password"]

                print(f"\n{model}\n----------\nUsername: {username}\nPassword: {password}\n")
            else:
                print("\n[ERROR] > Model not found in database\n")

    elif name == "&help":
        options = """
&search [ROUTER MODEL]     >     Displays the username and password of the given router model
&models                    >     Display all models in database
&help                      >     Returns this help message 
        """
        print(options)

    else:
        print("\n[ERROR] > Command not found\n")
        