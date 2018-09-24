import json
import httplib2

from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
BASE_URL = "https://texttospeech.googleapis.com/v1/text:synthesize"

REQUEST_HEADERS = {
    'content-type': 'application/json',
    'accept-encoding': 'gzip, deflate',
    'accept': 'application/json',
    'user-agent': 'google-api-python-client/1.6.4 (gzip)'
}


def get_authorized_http(service_account_json):
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        service_account_json, scopes=SCOPES)
    http = credentials.authorize(httplib2.Http(timeout=120))

    return http


def main(service_account_json, json_body):
    http = get_authorized_http(service_account_json)

    try:
        a, result = http.request(BASE_URL, 'POST',
            body=json.dumps(json_body),
            headers=REQUEST_HEADERS
        )
    except Exception, e:
        return {
            "success": False,
            "message": "Something went wrong.",
            "code": 401
        }

    return result
