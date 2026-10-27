"""
L3ClientModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class L3ClientModel(AbstractModel):
    """
    L3ClientModel
    """

    def __init__(
        self,
        client_ip=None,
        client_id=None,
        mount_id=None,
        mount_target_name=None,
        vpc_id=None,
        zone_name=None,
        server_ip=None,
        protocol=None,
    ):
        """
        Initialize L3ClientModel instance.

        :param client_ip: 客户端 IP
        :type client_ip: str (optional)

        :param client_id: 客户端 ID
        :type client_id: int (optional)

        :param mount_id: 客户端所挂载的挂载点 ID
        :type mount_id: str (optional)

        :param mount_target_name: 客户端所挂载的挂载点名称
        :type mount_target_name: str (optional)

        :param vpc_id: 客户端所在 VPC ID
        :type vpc_id: str (optional)

        :param zone_name: 客户端所在可用区
        :type zone_name: str (optional)

        :param server_ip: 为该客户端提供服务的服务端 IP
        :type server_ip: str (optional)

        :param protocol: 挂载使用的协议类型，bpfs / nfs
        :type protocol: str (optional)
        """
        super().__init__()
        self.client_ip = client_ip
        self.client_id = client_id
        self.mount_id = mount_id
        self.mount_target_name = mount_target_name
        self.vpc_id = vpc_id
        self.zone_name = zone_name
        self.server_ip = server_ip
        self.protocol = protocol

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
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.mount_id is not None:
            result['mountId'] = self.mount_id
        if self.mount_target_name is not None:
            result['mountTargetName'] = self.mount_target_name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.server_ip is not None:
            result['serverIp'] = self.server_ip
        if self.protocol is not None:
            result['protocol'] = self.protocol
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: L3ClientModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('mountId') is not None:
            self.mount_id = m.get('mountId')
        if m.get('mountTargetName') is not None:
            self.mount_target_name = m.get('mountTargetName')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('serverIp') is not None:
            self.server_ip = m.get('serverIp')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        return self
