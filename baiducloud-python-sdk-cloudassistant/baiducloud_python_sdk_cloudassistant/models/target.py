"""
Target information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Target(AbstractModel):
    """
    Target
    """

    def __init__(
        self,
        instance_type=None,
        instance_id=None,
        instance_name=None,
        internal_ip=None,
        external_ip=None,
        bandwidth=None,
    ):
        """
        Initialize Target instance.

        :param instance_type: 实例类型。枚举值：BCC，BBC
        :type instance_type: str (optional)

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param instance_name: 实例名称
        :type instance_name: str (optional)

        :param internal_ip: 内网IP
        :type internal_ip: str (optional)

        :param external_ip: 外网IP
        :type external_ip: str (optional)

        :param bandwidth: 带宽
        :type bandwidth: str (optional)
        """
        super().__init__()
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.internal_ip = internal_ip
        self.external_ip = external_ip
        self.bandwidth = bandwidth

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
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.internal_ip is not None:
            result['internalIp'] = self.internal_ip
        if self.external_ip is not None:
            result['externalIp'] = self.external_ip
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Target

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('internalIp') is not None:
            self.internal_ip = m.get('internalIp')
        if m.get('externalIp') is not None:
            self.external_ip = m.get('externalIp')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        return self
