"""
DnsResolver information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_privatezone.models.ip_model import IpModel


class DnsResolver(AbstractModel):
    """
    DnsResolver
    """

    def __init__(
        self,
        id=None,
        name=None,
        status=None,
        description=None,
        vpc_id=None,
        type=None,
        vpc_region=None,
        ip_models=None,
        create_time=None,
        update_time=None,
    ):
        """
        Initialize DnsResolver instance.

        :param id: 解析器ID
        :type id: str (optional)

        :param name: 解析器名称
        :type name: str (optional)

        :param status: status attribute
        :type status: str (optional)

        :param description: 解析器描述
        :type description: str (optional)

        :param vpc_id: VPC ID，解析器所有出站或入站的 DNS 查询流量都将经由该 VPC 进行流量转发
        :type vpc_id: str (optional)

        :param type: 解析器类型：outbound（出站解析器）、inbound（入站解析器）
        :type type: str (optional)

        :param vpc_region: 解析器所在的地区
        :type vpc_region: str (optional)

        :param ip_models: 入站 / 出站的流量地址
        :type ip_models: List[IpModel] (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.status = status
        self.description = description
        self.vpc_id = vpc_id
        self.type = type
        self.vpc_region = vpc_region
        self.ip_models = ip_models
        self.create_time = create_time
        self.update_time = update_time

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.description is not None:
            result['description'] = self.description
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.type is not None:
            result['type'] = self.type
        if self.vpc_region is not None:
            result['vpcRegion'] = self.vpc_region
        if self.ip_models is not None:
            result['ipModels'] = [i.to_dict() for i in self.ip_models]
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DnsResolver

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vpcRegion') is not None:
            self.vpc_region = m.get('vpcRegion')
        if m.get('ipModels') is not None:
            self.ip_models = [IpModel().from_dict(i) for i in m.get('ipModels')]
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
