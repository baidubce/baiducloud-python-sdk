"""
Request entity for SetClusterAsSlaveRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SetClusterAsSlaveRequest(AbstractModel):
    """
    Request entity for SetClusterAsSlaveRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, master_domain, master_port):
        """
        Initialize SetClusterAsSlaveRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param master_domain: 热活主实例的访问域名，如果是跨region，需要打开对等链接的dns复制功能
        :type master_domain: str (required)

        :param master_port: 热活主实例的访问端口
        :type master_port: int (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.master_domain = master_domain
        self.master_port = master_port

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
        if self.master_domain is not None:
            result['masterDomain'] = self.master_domain
        if self.master_port is not None:
            result['masterPort'] = self.master_port
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SetClusterAsSlaveRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('masterDomain') is not None:
            self.master_domain = m.get('masterDomain')
        if m.get('masterPort') is not None:
            self.master_port = m.get('masterPort')
        return self
