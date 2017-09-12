from urllib.parse import urlencode
from urllib.parse import urljoin


class ApiUrl:
    _base = '{}://{}{}/{}'

    def __init__(self, api_name, scheme='https', host='api.zaif.jp', port=None, path='', params=None):
        self._scheme = scheme
        self._host = host
        self._api_name = api_name
        self._port = port
        self._params = QueryParam(params)
        self._path = path

    def base_url(self):
        return self._base.format(self._scheme, self._host, self._get_port(), self._api_name)

    def full_url(self):
        url = self.base_url()
        url = urljoin(url, self._path)

        if len(self._params) == 0:
            return url

        url += '?' + self._params.encode()
        return url

    def _get_port(self):
        if self._port:
            return ':{}'.format(self._port)
        return ''

    def add_path(self, path):
        self._path = urljoin(self._path, path)


class QueryParam:
    def __init__(self, params=None):
        self._params = params or {}

    def encode(self):
        return urlencode(self._params)

    def __str__(self):
        return self.encode()

    def add_param(self, k, v):
        self._params[k] = v

    def add_params(self, dictionary):
        for k, v in dictionary.items():
            self._params[k] = v

    def __len__(self):
        return len(self._params)


class PublicBaseUrl(ApiUrl):
    def __init__(self, api_name, version, **kwargs):
        super().__init__(api_name, **kwargs)
        self._version = version

    def base_url(self):
        base = super().base_url()
        return base + '/{}'.format(self._version)


class TradeBaseUrl(ApiUrl):
    pass


class StreamBaseUrl(ApiUrl):
    pass
