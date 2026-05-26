"""
Request entity for CreateNatRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.billing import Billing
from baiducloud_python_sdk_vpc.models.session_config import SessionConfig
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class CreateNatRequest(AbstractModel):
    """
    Request entity for CreateNatRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        vpc_id,
        cu_num,
        billing,
        client_token=None,
        ip_version=None,
        bind_eips=None,
        session_config=None,
        tags=None,
        resource_group_id=None,
        delete_protect=None,
    ):
        """
        Initialize CreateNatRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: NAT网关的名称，由大小写字母、数字以及-\\_ /.特殊字符组成，必须以字母开头，长度1-65
        :type name: str (required)

        :param vpc_id: VPC的ID
        :type vpc_id: str (required)

        :param cu_num: NAT网关的CU数量
        :type cu_num: int (required)

        :param ip_version: NAT IP类型，默认v4
        :type ip_version: str (optional)

        :param bind_eips: 关联NAT网关EIP或者共享带宽中的一个或多个EIP
        :type bind_eips: List[str] (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param session_config: session_config parameter
        :type session_config: SessionConfig (optional)

        :param tags: 待创建的标签键值对列表。
        :type tags: List[TagModel] (optional)

        :param resource_group_id: 资源组
        :type resource_group_id: str (optional)

        :param delete_protect: 是否开启释放保护。缺省值为false，代表允许删除
        :type delete_protect: bool (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.vpc_id = vpc_id
        self.cu_num = cu_num
        self.ip_version = ip_version
        self.bind_eips = bind_eips
        self.billing = billing
        self.session_config = session_config
        self.tags = tags
        self.resource_group_id = resource_group_id
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
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.cu_num is not None:
            result['cuNum'] = self.cu_num
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.bind_eips is not None:
            result['bindEips'] = self.bind_eips
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.session_config is not None:
            result['sessionConfig'] = self.session_config.to_dict()
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
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
        :rtype: CreateNatRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('cuNum') is not None:
            self.cu_num = m.get('cuNum')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('bindEips') is not None:
            self.bind_eips = m.get('bindEips')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('sessionConfig') is not None:
            self.session_config = SessionConfig().from_dict(m.get('sessionConfig'))
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self
