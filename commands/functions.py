from util import CommandInvocationError, CommandExecutionError
import requests

ADD_API_ENDPOINT = 'apis'


def post_request(endpoint, payload, cert=None, key=None):
    if cert is None or key is None:
        response = requests.post(endpoint, data=payload)
    else:
        response = requests.post(endpoint, data=payload, cert=(cert, key), verify=False)
    if response.status_code == 201:
        print("API successfully created.")
    else:
        raise CommandExecutionError('Error creating API. Error response: %s' % response.text)


def create_api(**kwargs):
    http_method = 'http'
    if 'client_ssl' in kwargs:
        client_ssl = bool(kwargs['client_ssl'])
        if client_ssl is True:
            http_method = 'https'
            if 'cert' not in kwargs or 'key' not in kwargs:
                raise CommandInvocationError('Please specify cert and key parameters when using client_ssl.')
            cert = kwargs['cert']
            key = kwargs['key']
    endpoint = '%s://%s/%s' \
        % (http_method, kwargs['server'], ADD_API_ENDPOINT)
    payload = {'uris': kwargs['uri'],
               'name': kwargs['name'],
               'upstream_url': kwargs['upstream_url'],
               'hosts': kwargs['host'],
               'strip_uri': kwargs['strip_uri']}
    post_request(endpoint, payload, cert, key)
