"""
AppBackendServer information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.app_rs_port_model import AppRsPortModel


class AppBackendServer(AbstractModel):
    """
    AppBackendServer
    """

    def __init__(self, instance_id=None, weight=None, private_ip=None, port_list=None):
        """
        Initialize AppBackendServer instance.

        :param instance_id: 后端服务器标识符
        :type instance_id: str (optional)

        :param weight: 后端服务器权重，取值范围0-100
        :type weight: int (optional)

        :param private_ip: 查询时返回值，后端绑定的该服务器ip地址
        :type private_ip: str (optional)

        :param port_list: 查询时返回值，设置了相应策略，RS开放的端口列表
        :type port_list: List[AppRsPortModel] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.weight = weight
        self.private_ip = private_ip
        self.port_list = port_list

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.weight is not None:
            result['weight'] = self.weight
        if self.private_ip is not None:
            result['privateIp'] = self.private_ip
        if self.port_list is not None:
            result['portList'] = [i.to_dict() for i in self.port_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppBackendServer

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('privateIp') is not None:
            self.private_ip = m.get('privateIp')
        if m.get('portList') is not None:
            self.port_list = [AppRsPortModel().from_dict(i) for i in m.get('portList')]
        return self
