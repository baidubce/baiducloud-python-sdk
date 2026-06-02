"""
Request entity for MountTargetListClientsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MountTargetListClientsRequest(AbstractModel):
    """
    Request entity for MountTargetListClientsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, mount_target_id, manner, max_keys=None, marker=None):
        """
        Initialize MountTargetListClientsRequest request entity.

        :param mount_target_id: 挂载服务ID
        :type mount_target_id: str (required)

        :param max_keys: 返回客户端挂载列表长度，默认为100个，取值范围为【1, 500】，超过范围的规整为1或500
        :type max_keys: int (optional)

        :param manner: 请求的分段类型，必须指定marker
        :type manner: str (required)

        :param marker: 按照internalIp的字典序排列，从marker之后的第一个开始返回（不包括marker）
        :type marker: str (optional)
        """
        super().__init__()
        self.mount_target_id = mount_target_id
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
        if self.mount_target_id is not None:
            result['mountTargetId'] = self.mount_target_id
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
        :rtype: MountTargetListClientsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('mountTargetId') is not None:
            self.mount_target_id = m.get('mountTargetId')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('manner') is not None:
            self.manner = m.get('manner')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self
