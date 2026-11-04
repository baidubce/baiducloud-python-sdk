"""
Request entity for CreateL3MountTargetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateL3MountTargetRequest(AbstractModel):
    """
    Request entity for CreateL3MountTargetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, instance_id, vpc_id, subnet_id, name=None, access_group_name=None, protocol=None, ip_address=None
    ):
        """
        Initialize CreateL3MountTargetRequest request entity.

        :param instance_id: PFS实例ID
        :type instance_id: str (required)

        :param vpc_id: PFS实例vip所属VPC的短Id
        :type vpc_id: str (required)

        :param subnet_id: MountTarget所属子网，subnet属于PFS实例所在vpc，为短id
        :type subnet_id: str (required)

        :param name: 挂载点名称，默认default
        :type name: str (optional)

        :param access_group_name: 权限组名称，默认DEFAULT_ACCESS_GROUP_NAME
        :type access_group_name: str (optional)

        :param protocol: 协议类型，默认bpfs，当前只支持bpfs/nfs
        :type protocol: str (optional)

        :param ip_address: 挂载点IP地址
        :type ip_address: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.name = name
        self.access_group_name = access_group_name
        self.protocol = protocol
        self.ip_address = ip_address

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
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.name is not None:
            result['name'] = self.name
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateL3MountTargetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        return self
