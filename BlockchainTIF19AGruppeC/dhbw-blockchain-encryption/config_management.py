import json
import datetime
import dateutil.parser
import dateutil.tz

options = []
end_timestamp = ""
end_time = datetime.datetime.now()

#Initialize by reading in the config information
with open("./config/config.json") as config_file:
    config_data = json.load(config_file)
    options = config_data["Partei"]
    end_timestamp = config_data["Date"]
    end_time = dateutil.parser.isoparse(end_timestamp)

def get_options():
    return options

def is_election_over():
    current_time = datetime.datetime.now(dateutil.tz.UTC)
    if current_time > end_time:
        return True
    else:
        return False