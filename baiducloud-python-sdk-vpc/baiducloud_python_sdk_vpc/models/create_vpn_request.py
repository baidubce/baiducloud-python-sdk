"""
Request entity for CreateVpnRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.tag_model import TagModel
from baiducloud_python_sdk_vpc.models.billing import Billing


class CreateVpnRequest(AbstractModel):
    """
    Request entity for CreateVpnRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        vpc_id,
        vpn_name,
        billing,
        client_token=None,
        subnet_id=None,
        type=None,
        description=None,
        eip=None,
        tags=None,
        resource_group_id=None,
        max_connection=None,
        delete_protect=None,
    ):
        """
        Initialize CreateVpnRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param vpc_id: 所属VPC的ID
        :type vpc_id: str (required)

        :param subnet_id: 所属SUBNET的ID
        :type subnet_id: str (optional)

        :param vpn_name: VPN的名称，大小写字母、数字以及-_/.特殊字符，必须以字母开头，长度1-65
        :type vpn_name: str (required)

        :param type: VPN网关类型，值“IPSec”表示IPSec-VPN网关，值“SSL”表示SSL-VPN网关，默认为“IPSec”
        :type type: str (optional)

        :param description: VPN的描述
        :type description: str (optional)

        :param eip: VPN绑定的eip
        :type eip: str (optional)

        :param tags: VPN绑定的标签
        :type tags: List[TagModel] (optional)

        :param resource_group_id: VPN绑定的资源组
        :type resource_group_id: str (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param max_connection: SSL-VPN最大客户端连接数。可选 [5, 10, 20, 50, 100, 200, 500, 1000]。仅SSL-VPN需要选这个参数。
        :type max_connection: int (optional)

        :param delete_protect: 是否开启释放保护。缺省值为false，代表允许删除
        :type delete_protect: bool (optional)
        """
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
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
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
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateVpnRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
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
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('maxConnection') is not None:
            self.max_connection = m.get('maxConnection')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self
