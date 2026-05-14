"""
Request entity for CreateSnicRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_snic.models.billing import Billing
from baiducloud_python_sdk_snic.models.tag_model import TagModel


class CreateSnicRequest(AbstractModel):
    """
    Request entity for CreateSnicRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        vpc_id,
        name,
        subnet_id,
        service,
        bandwidth,
        billing,
        client_token=None,
        description=None,
        ip_address=None,
        tags=None,
        resource_group_id=None,
    ):
        """
        Initialize CreateSnicRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param vpc_id: 所属vpc的id
        :type vpc_id: str (required)

        :param name: 服务网卡的名称，大小写字母、数字以及-_/.特殊字符、中文，必须以字母开头，长度1-65
        :type name: str (required)

        :param subnet_id: 所在子网的id
        :type subnet_id: str (required)

        :param service: 挂载的服务域名
        :type service: str (required)

        :param description: 服务网卡描述
        :type description: str (optional)

        :param ip_address: 指定服务网卡ip地址,不传自动分配ip地址
        :type ip_address: str (optional)

        :param bandwidth: 指定服务网卡带宽
        :type bandwidth: int (required)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param tags: 标签
        :type tags: List[TagModel] (optional)

        :param resource_group_id: 资源组
        :type resource_group_id: str (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.vpc_id = vpc_id
        self.name = name
        self.subnet_id = subnet_id
        self.service = service
        self.description = description
        self.ip_address = ip_address
        self.bandwidth = bandwidth
        self.billing = billing
        self.tags = tags
        self.resource_group_id = resource_group_id

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
        if self.name is not None:
            result['name'] = self.name
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.service is not None:
            result['service'] = self.service
        if self.description is not None:
            result['description'] = self.description
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSnicRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        return self
