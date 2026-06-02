"""
Request entity for InstanceListClientsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceListClientsRequest(AbstractModel):
    """
    Request entity for InstanceListClientsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, manner, max_keys=None, marker=None):
        """
        Initialize InstanceListClientsRequest request entity.

        :param instance_id: PFS实例ID
        :type instance_id: str (required)

        :param max_keys: 返回客户端挂载列表长度，默认为100个，取值范围为【1, 500】，超过范围的规整为1或500
        :type max_keys: int (optional)

        :param manner: 请求的分段类型，必须指定marker
        :type manner: str (required)

        :param marker: 按照internalIp的字典序排列，从marker之后的第一个开始返回（不包括marker）
        :type marker: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.max_keys = max_keys
        self.manner = manner
        self.marker = marker

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.manner is not None:
            result['manner'] = self.manner
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceListClientsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('manner') is not None:
            self.manner = m.get('manner')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self
