from revproxy.views import ProxyView


class FlowerView(ProxyView):
    upstream = 'http://127.0.0.1:5555/flower/'
