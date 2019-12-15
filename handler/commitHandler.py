from datetime import datetime
import json

from common.Appconfigurations import KL_PULSE_CREATE_STATUS_API_ENDPOINT
import requests

from common.Appconfigurations import BIT_BUCKET_API_ENDPOINT, bit_bucket_headers, bit_bucket_user, \
    time_format_of_received_string, kl_name, kl_mail


class CommitHandler(object):
    def __init__(self):
        try:
            print('intialized')
        except Exception as e:
            print("Exception while initializing Project Handler.")

    def get_commits(self):
        try:
            commits_for_today = ""
            current_date = datetime.now()
            projects_assigned_to_me = [{
                "CODE_BASE_URL": BIT_BUCKET_API_ENDPOINT,
                "headers": bit_bucket_headers,
                "code_base_type": "BIT-BUCKET",
                "date_key": "date",
                "unique_user_mail": bit_bucket_user
            }]
            for each_project in projects_assigned_to_me:
                api_response = requests.get(
                    url=each_project['CODE_BASE_URL'], headers=each_project['headers'])

                commit_data = api_response.json()
                # print(commit_data)

                if commit_data:
                    if each_project['code_base_type'] == "BIT-BUCKET":
                        my_commits = commit_data['values']
                    else:
                        my_commits = commit_data  # git response

                    for each_commit in my_commits:

                        converted_date = datetime.strptime(
                            each_commit[each_project['date_key']], time_format_of_received_string)

                        days_diff = (current_date.replace(hour=0, minute=0, second=0, microsecond=0) -
                                     converted_date.replace(hour=0, minute=0, second=0, microsecond=0))

                        if each_project['code_base_type'] == "BIT-BUCKET":
                            unique_user_key = each_commit['author']['raw'].split('<')[
                                                  1][:-1]
                            commit_message = each_commit['summary']['raw']
                        else:
                            unique_user_key = each_commit['committer_email']
                            commit_message = each_commit['title']

                        if each_project['unique_user_mail'] == unique_user_key and days_diff.days == 0:
                            commits_for_today += commit_message + "↵"
                            print(commit_message)
        except Exception as e:
            print(e)
            pass

        request_status_template = {"startDate": current_date.strftime('%m/%d/%Y'), "name": kl_name, "email": kl_mail,
                                   "taskToday": "commits_for_today"}

        # res_status = fill_status(request_status_template)
        return request_status_template

    def fill_status(self, request_status_template):
        create_status_response = requests.post(url=KL_PULSE_CREATE_STATUS_API_ENDPOINT,
                                               data=json.dumps(request_status_template), headers={
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}, verify=False)

        return create_status_response.json()

    def convert_web_hook(self, speech):
        print(speech)
        return {
            "speech": speech,
            "displayText": speech, }

    def process_request(self, req):
        action = req.get("queryResult").get("action")
        print("starting processRequest...", action)
        if action != "klpulse":
            return {}
        data = self.get_commits()
        res = self.convert_web_hook(self.fill_status(data))
        return res
