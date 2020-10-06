import json
import random
import urllib.request

HOST = "localhost"
PORT = 8069
DB = "odoodb"
USER = "admin"
PASS = "admin"


def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(
        url=url,
        data=json.dumps(data).encode(),
        headers={"Content-Type": "application/json",},
    )
    reply = json.loads(urllib.request.urlopen(req).read().decode("UTF8"))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]


def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})


# log in the given database
url = "http://{}:{}/jsonrpc".format(HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

# create a new note
args = {
    "name": "Python Masterclass",
}
note_id = call(
    url, "object", "execute", DB, uid, PASS, "openacademy.course", "create", args
)
