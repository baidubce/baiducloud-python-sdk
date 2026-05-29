"""
AppIpGroupMemberPortModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppIpGroupMemberPortModel(AbstractModel):
    """
    AppIpGroupMemberPortModel
    """

    def __init__(self, health_check_port_type=None, status=None):
        """
        Initialize AppIpGroupMemberPortModel instance.

        :param health_check_port_type: 健康检查端口协议类型
        :type health_check_port_type: str (optional)

        :param status: 端口状态，\"Alive\"/\"Dead\"/\"Unknown\"
        :type status: str (optional)
        """
        super().__init__()
        self.health_check_port_type = health_check_port_type
        self.status = status

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
        if self.health_check_port_type is not None:
            result['healthCheckPortType'] = self.health_check_port_type
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppIpGroupMemberPortModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('healthCheckPortType') is not None:
            self.health_check_port_type = m.get('healthCheckPortType')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
