def main(request, response):
    if request.method == u'OPTIONS':
        # CORS preflight
        response.headers.set(b'Access-Control-Allow-Origin', b'*')
        response.headers.set(b'Access-Control-Allow-Methods', b'*')
        response.headers.set(b'Access-Control-Allow-Headers', b'*')
        return 'done'

    url_dir = u'/'.join(request.url_parts.path.split(u'/')[:-1]) + u'/'
    key = request.GET.first(b"key")
    value = request.GET.first(b"value")
    request.server.stash.put(key, value, url_dir)
    response.headers.set(b'Access-Control-Allow-Origin', b'*')
    return "done"
