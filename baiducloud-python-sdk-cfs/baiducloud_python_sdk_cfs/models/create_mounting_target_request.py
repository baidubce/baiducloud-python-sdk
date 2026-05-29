"""
Request entity for CreateMountingTargetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateMountingTargetRequest(AbstractModel):
    """
    Request entity for CreateMountingTargetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, fs_id, subnet_id, vpc_id, access_group_name=None, address=None):
        """
        Initialize CreateMountingTargetRequest request entity.

        :param fs_id: fs_id parameter
        :type fs_id: str (required)

        :param subnet_id: MountTarget所属子网，subnet属于fs所在vpc，为短id
        :type subnet_id: str (required)

        :param vpc_id: fs实例vip所属VPC的短Id
        :type vpc_id: str (required)

        :param access_group_name: 绑定的权限组的名称，长度1~65个字节，字母开头，可包含字母数字和- _ .字符。
        :type access_group_name: str (optional)

        :param address: 创建MountTarget的指定IP地址
        :type address: str (optional)
        """
        super().__init__()
        self.fs_id = fs_id
        self.subnet_id = subnet_id
        self.vpc_id = vpc_id
        self.access_group_name = access_group_name
        self.address = address

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
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.address is not None:
            result['address'] = self.address
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateMountingTargetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fsId') is not None:
            self.fs_id = m.get('fsId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('address') is not None:
            self.address = m.get('address')
        return self
