from revproxy.views import ProxyView
import environ


class FlowerView(ProxyView):
    upstream = environ.Env()('BACKGROUND_JOBS_PATH')
