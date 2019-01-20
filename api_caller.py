import requests

access_token = 'access_token_here_if_necessary'

def call_api(method, id):
    endpoint = 'https://hostname/path/' + id

    request_url = endpoint + '?access_token=' + access_token
    req = requests.request(method, request_url)

    print(request_url)
    print(req.status_code)

    return str(req.content)[:100]


def clean_cache(id):
    request_url = 'https://hostname/path/' + id + '/cache/ban?access_token=' + access_token

    req = requests.request('DELETE', request_url)
    print(req)


with open('./ids.txt', 'r') as infile, open('./responses.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line)
        clean_cache(line)
        outfile.write(str(call_api('GET', line)))
        outfile.write("\n")
