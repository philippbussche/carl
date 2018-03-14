from util import CommandInvocationError, CommandExecutionError
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

API_ENDPOINT = 'apis'


def post_request(endpoint, payload, cert=None, key=None):
    if cert is None or key is None:
        response = requests.post(endpoint, data=payload)
    else:
        response = requests.post(endpoint, data=payload, cert=(cert, key), verify=False)
    return response


def get_request(endpoint, cert=None, key=None):
    if cert is None or key is None:
        response = requests.get(endpoint)
    else:
        response = requests.get(endpoint, cert=(cert, key), verify=False)
    return response


def delete_request(endpoint, cert=None, key=None):
    if cert is None or key is None:
        response = requests.delete(endpoint)
    else:
        response = requests.delete(endpoint, cert=(cert, key), verify=False)
    return response


def update_request(endpoint, payload, cert=None, key=None):
    if cert is None or key is None:
        response = requests.patch(endpoint, data=payload)
    else:
        response = requests.patch(endpoint, data=payload, cert=(cert, key), verify=False)
    return response


def get_endpoint(**kwargs):
    http_method = 'http'
    if 'client_ssl' in kwargs:
        client_ssl = bool(kwargs['client_ssl'])
        if client_ssl is True:
            http_method = 'https'
            if 'cert' not in kwargs or 'key' not in kwargs:
                raise CommandInvocationError("Both cert and key have to be specified when client_ssl is set to true.")
    endpoint = '%s://%s/%s' \
        % (http_method, kwargs['server'], API_ENDPOINT)
    return endpoint


def create_api(**kwargs):
    endpoint = get_endpoint(**kwargs)
    if 'cert' in kwargs:
        cert = kwargs['cert']
    if 'key' in kwargs:
        key = kwargs['key']
    payload = {'uris': kwargs['uri'],
               'name': kwargs['name'],
               'upstream_url': kwargs['upstream_url'],
               'hosts': kwargs['host'],
               'strip_uri': kwargs['strip_uri']}
    response = post_request(endpoint, payload, cert, key)
    if response.status_code == 201:
        print("API '%s' successfully created." % kwargs['name'])
    else:
        raise CommandExecutionError("Error creating API '%s'. Error response: %s" % (kwargs['name'], response.text))


def get_all_apis(**kwargs):
    endpoint = get_endpoint(**kwargs)
    if 'cert' in kwargs:
        cert = kwargs['cert']
    if 'key' in kwargs:
        key = kwargs['key']
    get_response = get_request(endpoint, cert, key)
    if get_response.status_code == 200:
        try:
            response_dict = json.loads(get_response.text)
            data = response_dict['data']
        except:
            raise CommandExecutionError("Error parsing response.")
    else:
        raise CommandExecutionError("Error querying APIs.")
    return data


def delete_apis(**kwargs):
    data = None
    endpoint = get_endpoint(**kwargs)
    if 'cert' in kwargs:
        cert = kwargs['cert']
    if 'key' in kwargs:
        key = kwargs['key']
    if 'all' in kwargs:
        data = get_all_apis(**kwargs)
    if data is not None and len(data) > 0:
        for api in data:
            delete_response = delete_request("%s/%s" % (endpoint, api['id']), cert, key)
            if delete_response.status_code == 204:
                print("API '%s' successfully deleted." % api['name'])
            else:
                raise CommandExecutionError("Error deleting API '%s'. Error response: %s" % (api['name'], delete_response.text))
    else:
        print("No APIs to delete.")


def update_api(**kwargs):
    endpoint = get_endpoint(**kwargs)
    if 'cert' in kwargs:
        cert = kwargs['cert']
    if 'key' in kwargs:
        key = kwargs['key']
    data = get_all_apis(**kwargs)
    payload = {'uris': kwargs['uri'],
               'upstream_url': kwargs['upstream_url'],
               'hosts': kwargs['host'],
               'strip_uri': kwargs['strip_uri']}
    api_exists = False
    if len(data) > 0:
        for api in data:
            if kwargs['uri'] == api['uris'][0] and kwargs['host'] == api['hosts'][0]:
                api_exists = True
                update_response = update_request("%s/%s" % (endpoint, api['id']), payload, cert, key)
                if update_response.status_code == 200:
                    print("API '%s' successfully updated." % api['name'])
                else:
                    raise CommandExecutionError("Error updating API '%s'. Error response: %s" % (api['name'], update_response.text))
                break
    if not api_exists:
        payload['name'] = "%s_%s" % (kwargs['uri'].replace("/", "_").strip("_"), kwargs['host'].replace(".", "_"))
        post_response = post_request(endpoint, payload, cert, key)
        if post_response.status_code == 201:
            print("API '%s' successfully created." % payload['name'])
        else:
            raise CommandExecutionError("Error creating API '%s'. Error response: %s" % (payload['name'], post_response.text))
