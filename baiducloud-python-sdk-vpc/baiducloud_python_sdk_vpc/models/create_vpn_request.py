from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.tag_model import TagModel
from baiducloud_python_sdk_vpc.models.billing import Billing


class CreateVpnRequest(AbstractModel):
    """
    创建VPN请求类

    Attributes:
        vpc_id (str): VPC ID
        vpn_name (str): VPN名称
        billing (Billing): 计费信息
        client_token (str, optional): 客户端token
        subnet_id (str, optional): 子网ID
        type (str, optional): VPN类型
        description (str, optional): 描述信息
        eip (str, optional): 弹性IP
        tags (list[TagModel], optional): 标签列表
        resource_group_id (str, optional): 资源组ID
        max_connection (int, optional): 最大连接数
        delete_protect (bool, optional): 删除保护
    """

    def __init__(self, vpc_id, vpn_name, billing, client_token=None, subnet_id=None, type=None, description=None, eip=None, tags=None, resource_group_id=None, max_connection=None, delete_protect=None):
        super().__init__()
        self.client_token = client_token
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.vpn_name = vpn_name
        self.type = type
        self.description = description
        self.eip = eip
        self.tags = tags
        self.resource_group_id = resource_group_id
        self.billing = billing
        self.max_connection = max_connection
        self.delete_protect = delete_protect

    def to_dict(self):
        """
        将对象转换为字典

        Returns:
            dict: 包含对象属性的字典
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.vpn_name is not None:
            result['vpnName'] = self.vpn_name
        if self.type is not None:
            result['type'] = self.type
        if self.description is not None:
            result['description'] = self.description
        if self.eip is not None:
            result['eip'] = self.eip
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.max_connection is not None:
            result['maxConnection'] = self.max_connection
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        return result


    def from_dict(self, m):
        """
        从字典初始化对象

        Args:
            m (dict): 包含对象属性的字典

        Returns:
            CreateVpnRequest: 初始化后的对象
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('vpnName') is not None:
            self.vpn_name = m.get('vpnName')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('tags') is not None:
            self.tags = [
            TagModel().from_dict(i)
            for i in m.get('tags')
            ]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('maxConnection') is not None:
            self.max_connection = m.get('maxConnection')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self