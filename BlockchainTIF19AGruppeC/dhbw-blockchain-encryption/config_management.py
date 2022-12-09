import json
import datetime
import dateutil.parser
import dateutil.tz

voter_count = 0
options = []
start_timestamp = ""
start_time = datetime.datetime.now()
end_timestamp = ""
end_time = datetime.datetime.now()

#Initialize by reading in the config information
with open("./config/config.json") as config_file:
    config_data = json.load(config_file)
    voter_count = config_data["voterCount"]
    options = config_data["options"]
    start_timestamp = config_data["start"]
    start_time = dateutil.parser.isoparse(start_timestamp)
    end_timestamp = config_data["end"]
    end_time = dateutil.parser.isoparse(end_timestamp)

#Declare functions for accessing config variables
def get_voter_count():
    return voter_count

def get_options():
    return options

def has_election_started():
    current_time = datetime.datetime.now(dateutil.tz.UTC)
    if current_time > start_time:
        return True
    else:
        return False

def is_election_over():
    current_time = datetime.datetime.now(dateutil.tz.UTC)
    if current_time > end_time:
        return True
    else:
        return False