import base64

KL_PULSE_STATUS_WEB = "https://kk.knowledgelens.com/"
KL_PULSE_CREATE_STATUS_API_ENDPOINT = 'https://kk.knowledgelens.com/'
kl_name = "Rama Hruday Bandaru"
kl_mail = ""

# bit bucket style
BIT_BUCKET_API_ENDPOINT = 'https://api.bitbucket.org/2.0/'
bit_bucket_user_cred = 
bit_bucket_headers = {'Authorization': 'Basic %s' % bit_bucket_user_cred}
bit_bucket_status_headers = {
    'Authorization': 'Basic %s' % bit_bucket_user_cred}
bit_bucket_user = ""

# git lab style
GIT_LAB_API_ENDPOINT = "https://gitlab.example.com/api/v4/projects/5/repository/commits"
git_lab_access_token = ""
git_lab_status_headers = {'PRIVATE-TOKEN': git_lab_access_token}
git_lab_user = ""

time_format_of_received_string = "%Y-%m-%dT%H:%M:%S+00:00"


def process_request(self, req):
    action = req.get("result").get("action")
    print("starting processRequest...", action)
    if action != "klpulse":
        return {}
    data = get_commits()
    res = convert_web_hook(fill_status(data))
    return res

