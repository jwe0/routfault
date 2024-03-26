import json, os

database = {}


"""

This program parses the data that was scraped by the enumerator
and dumps it into a json database

"""



for file in os.listdir("Passwords/"):
    print(file)
    with open("Passwords/" + file) as f:
        content = f.read().splitlines()

        for line in content:
            try:
                router_info = line.split("|")
                print(router_info)
                name = router_info[0].replace(" ", "")
                username = router_info[1].replace(" ", "")
                password = router_info[2].replace(" ", "")

                database[name.lower()] = {"username" : username, "password" : password}
            except:
                continue

            

with open("database.json", 'w') as f:
    f.write(json.dumps(database, indent=4)) 