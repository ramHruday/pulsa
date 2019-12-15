import base64

KL_PULSE_STATUS_WEB = "https://klpulse.knowledgelens.com/kpulse/templates/addStatus.html"
KL_PULSE_CREATE_STATUS_API_ENDPOINT = 'https://klpulse.knowledgelens.com/status/createStatus'
kl_name = "Rama Hruday Bandaru"
kl_mail = "rama@knowledgelens.com"

# bit bucket style
BIT_BUCKET_API_ENDPOINT = 'https://api.bitbucket.org/2.0/repositories/zs_businesstech/amgen-search/commits'
bit_bucket_user_cred = base64.b64encode(b"rh21686:zsa!21686h").decode("ascii")
bit_bucket_headers = {'Authorization': 'Basic %s' % bit_bucket_user_cred}
bit_bucket_status_headers = {
    'Authorization': 'Basic %s' % bit_bucket_user_cred}
bit_bucket_user = "rama.hruday@zs.com"

# git lab style
GIT_LAB_API_ENDPOINT = "https://gitlab.example.com/api/v4/projects/5/repository/commits"
git_lab_access_token = "git access token"
git_lab_status_headers = {'PRIVATE-TOKEN': git_lab_access_token}
git_lab_user = "rama@knowledgelens.com"

time_format_of_received_string = "%Y-%m-%dT%H:%M:%S+00:00"


def process_request(self, req):
    action = req.get("result").get("action")
    print("starting processRequest...", action)
    if action != "klpulse":
        return {}
    data = get_commits()
    res = convert_web_hook(fill_status(data))
    return res

