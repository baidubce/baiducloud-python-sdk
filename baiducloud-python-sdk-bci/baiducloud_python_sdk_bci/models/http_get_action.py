"""
HTTPGetAction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bci.models.http_header import HTTPHeader


class HTTPGetAction(AbstractModel):
    """
    HTTPGetAction
    """

    def __init__(self, path=None, port=None, scheme=None, host=None, http_headers=None):
        """
        Initialize HTTPGetAction instance.

        :param path: HTTP Get请求检测路径
        :type path: str (optional)

        :param port: HTTP Get请求检测端口号
        :type port: int (optional)

        :param scheme: 协议类型：HTTP、HTTPS
        :type scheme: str (optional)

        :param host: host值
        :type host: str (optional)

        :param http_headers: http header
        :type http_headers: List[HTTPHeader] (optional)
        """
        super().__init__()
        self.path = path
        self.port = port
        self.scheme = scheme
        self.host = host
        self.http_headers = http_headers

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.port is not None:
            result['port'] = self.port
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.host is not None:
            result['host'] = self.host
        if self.http_headers is not None:
            result['httpHeaders'] = [i.to_dict() for i in self.http_headers]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HTTPGetAction

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('httpHeaders') is not None:
            self.http_headers = [HTTPHeader().from_dict(i) for i in m.get('httpHeaders')]
        return self
