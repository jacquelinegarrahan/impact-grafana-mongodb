import paramiko
from scp import SCPClient
from pymongo import MongoClient
import json
import dateutil.parser
import os 


MONGO_HOST = os.environ["MONGO_HOST"]
MONGO_PORT = os.environ["MONGO_PORT"]

dir_path = os.path.dirname(os.path.realpath(__file__))
impact_files = [f for f in os.listdir("output") if os.path.isfile(os.path.join("output", f))]

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client.impact
results = db.results


for filename in impact_files:
    with open(f"output/{filename}", "r") as f:
        try:
            document = json.load(f)
            path_name = document["outputs"]["plot_file"]
            document["isotime"] = dateutil.parser.isoparse(document["isotime"])
            scp.get(path_name, "files/")
            file_base = path_name.split("/")[-1]
            file_base = file_base.replace(":", "%3A")
            document["outputs"]["plot_file"] = f"https://raw.githubusercontent.com/jacquelinegarrahan/impact-grafana-mongodb/main/files/{file_base}"
            results.insert_one(document)
        except:
            pass