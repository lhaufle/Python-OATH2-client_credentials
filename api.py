from cgitb import reset
from pydoc import cli
from tracemalloc import start
import requests
import base64
import time


class TD_API:

    token = ""  # token retrieved from client_credential authentication
    job_id = ""  # job id returned after a request for a report is submitted
    report_type = ""  # Just for easy access for url building when needed

    # Initialize with encoded client_id and client_secret
    # and send a post request to assign value to the token that create reports
    # and retrieve them.
    def __init__(self, client_id, client_secret, base_url):
        # combine string for encoding
        base_string = client_id + ":" + client_secret
        # encode to ascii text, which was before base64 encoding
        data_bytes = base_string.encode('ascii')
        # encode to base64
        key64 = base64.b64encode(data_bytes)
        # decode the new encoded value to a string
        message64 = key64.decode('ascii')
        # create headers and payload for the post request.
        payload = {
            'grant_type': 'client_credentials',
            "scope": "reports:read reports:write data-reports:write data-reports:read",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        headers = {
            "Accept": "application/json",
            "Authorization": "Basic " + message64
        }
        # send the post request to retrieve the token
        response = requests.request(
            "POST", base_url, data=payload, headers=headers)
        self.token = response.json()['access_token']

    def token_value(self):
        return self.token

    # The create_report function takes the type of report, the time range,
    # and the name the report will be called
    def create_report(self, report_type, start_date, end_date, name):
        # add report type to url
        url = "removed" + report_type + "/jobs"
        # Body for the post request
        payload = {
            "format": "json",
            "timespan": {
                "from": start_date,
                "to": end_date
            },
            "name": name
        }
        # header values with the token
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json"
        }
        # make the request
        response = requests.request("POST", url, json=payload, headers=headers)
        # display response to the console
        print("---Create Report Response--")
        print(response.text)
        print("----------------------")
        # print(response.text)
        job_id = response.json()['id']
        # assign variables or later use
        self.job_id = job_id
        self.report_type = report_type

    # The get report method checks the status of the report after the create report is posted
    # then will return the values as a json object when 'Done'
    def get_report(self):
        # build the url
        url = "removed/" + \
            self.report_type + "/jobs/" + self.job_id
        # values to pass in the header
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.token
        }
        # check on the job status
        response = requests.request("GET", url, headers=headers)
        while 'Content-Length' not in response.headers:
            time.sleep(3)  # pause 3 sec between each request
            response = requests.request("GET", url, headers=headers)
        return response.json()
