"""
Request entity for UpdateProbeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateProbeRequest(AbstractModel):
    """
    Request entity for UpdateProbeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, probe_id, client_token=None, name=None, description=None, dest_ip=None, dest_port=None):
        """
        Initialize UpdateProbeRequest request entity.

        :param probe_id: probe_id parameter
        :type probe_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 网络探测名称，长度不超过65个字符，可由数字、字符、下划线组成
        :type name: str (optional)

        :param description: 网络探测描述，不超过200字符
        :type description: str (optional)

        :param dest_ip: 探测目的IP
        :type dest_ip: str (optional)

        :param dest_port: 探测目的端口
        :type dest_port: int (optional)
        """
        super().__init__()
        self.probe_id = probe_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.dest_ip = dest_ip
        self.dest_port = dest_port

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.dest_ip is not None:
            result['destIp'] = self.dest_ip
        if self.dest_port is not None:
            result['destPort'] = self.dest_port
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateProbeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('probeId') is not None:
            self.probe_id = m.get('probeId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('destIp') is not None:
            self.dest_ip = m.get('destIp')
        if m.get('destPort') is not None:
            self.dest_port = m.get('destPort')
        return self
