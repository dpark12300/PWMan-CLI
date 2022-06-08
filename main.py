#Credit goes to @Discoverypark And @Schniz for codin'
import json, os, sys, pprint, replit
from pathlib import Path
args = sys.argv
default_file = "pw.json"
commands = '''
Commandz
--------

add NAME: Add an entry to the database.

read NAME: Read an entry from the database.

delete NAME: Delete an entry from the database.

list: List database entries.

--help: Show help menu

Add/Modify Options
-------

-p PW, --password PW
-n USERNAME, --name USERNAME
-u URL, --url URL

'''

usage = '''
Usage: python3 pwman.py COMMAND [NAME]
'''

name_cmds = ["add", "read", "rm"]
if len(args) < 2:
    print(usage)
    exit(1)

args.pop(0)
cmd = args.pop(0)
if cmd in name_cmds:
    name = args.pop(0)

# Option variables
password = ""
username = ""
url = ""
path = ""

# -p password -n me -u example.com
i = 0
while i < len(args):
    a = args[i]
    if a == "-p" or a == "--password":
        i += 1
        password = args[i]
    elif a == "-n" or a == "--name":
        i += 1
        username = args[i]
    elif a == "-u" or a == "--url":
        i += 1
        url = args[i]
    elif a == "-f" or a == "--file":
        i += 1
        path = args[i]
    i += 1

if path == "":
    path = Path.home().joinpath(default_file)

def read_file(filename):
    with open(filename, "r") as pwfile:
        data = json.load(pwfile)
        pwfile.close()
        return data


def write_file(filename, data):
    with open(str(Path.home().joinpath(filename)), "w") as pwfile:
        json.dump(data, pwfile)
        pwfile.close()
        return str(Path.home().joinpath(filename))


# Check if file exists, if not, create it.
if not os.path.exists(path):
    write_file(path, {"entries":[]})

if cmd == "add":
    print("Reading file")
    data = read_file(path)
    print("Adding entry")
    data["entries"].append({
        "name":name,
        "url":url,
        "username":username,
        "passwd":password
    })
    print("Saving password data")
    write_file(path, data)
    print("Done")
elif cmd == "list":
    data = read_file(path)
    names = ""
    for i in data["entries"]:
        names += i["name"] + "\n"
    print(names)
elif cmd == "read":
    data = read_file(path)
    # print password, given entry
    for entry in data["entries"]:
        if entry["name"] == name:
            print("Password: " + entry["passwd"])
            print("Username: " + entry["username"])
            print("URL: " + entry["url"])
            # print data in entry i
elif cmd == "rm":
    print("Reading file...")
    data = read_file(path)
    for i in range(len(data["entries"])):
        print('Finding entry "' + name + '"')
        if data["entries"][i]["name"] == name:
            data["entries"].pop(i)
            print('Removing entry "' + name + '"')
    write_file(path, data)
elif cmd == "--help":
    print(commands)
#TODO: save file add

# Example password data
'''
{
    "entries":
        [
            {"name": "my_name", "url": "my_url", "username": "my_user", "passwd": "my_password"}
        ]
}
'''
