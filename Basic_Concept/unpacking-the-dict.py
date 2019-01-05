headers = {
    'Accept': 'text/plain',
    'Content-Length': 348,
    'Host': 'http://mingrammer.com'
}

def pre_process(**headers):
    content_length = headers['Content-Length']
    print('Content length: ', content_length)

    host = headers['Host']
    if 'https' not in host:
        raise ValueError('You must use SSL for http communication')


pre_process(**headers)