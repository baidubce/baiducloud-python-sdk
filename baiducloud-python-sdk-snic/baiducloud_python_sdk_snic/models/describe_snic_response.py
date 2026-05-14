"""
Request entity for DescribeSnicResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_snic.models.tag_model import TagModel


class DescribeSnicResponse(BceResponse):
    """
    DescribeSnicResponse
    """

    def __init__(
        self,
        endpoint_id=None,
        name=None,
        ip_address=None,
        status=None,
        service=None,
        subnet_id=None,
        description=None,
        create_time=None,
        product_type=None,
        vpc_id=None,
        tags=None,
    ):
        """
        Initialize DescribeSnicResponse response.

        :param endpoint_id: 服务网卡的id
        :type endpoint_id: str (optional)

        :param name: 服务网卡的名称
        :type name: str (optional)

        :param ip_address: 服务网卡ip
        :type ip_address: str (optional)

        :param status: 服务网卡状态，取值：available/dead，分别表示：可挂载/不可挂载
        :type status: str (optional)

        :param service: 服务唯一域名
        :type service: str (optional)

        :param subnet_id: 子网id
        :type subnet_id: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param product_type: 付费类型
        :type product_type: str (optional)

        :param vpc_id: vpc的id
        :type vpc_id: str (optional)

        :param tags: 标签
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.endpoint_id = endpoint_id
        self.name = name
        self.ip_address = ip_address
        self.status = status
        self.service = service
        self.subnet_id = subnet_id
        self.description = description
        self.create_time = create_time
        self.product_type = product_type
        self.vpc_id = vpc_id
        self.tags = tags

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id
        if self.name is not None:
            result['name'] = self.name
        if self.ip_address is not None:
            result['ipAddress'] = self.ip_address
        if self.status is not None:
            result['status'] = self.status
        if self.service is not None:
            result['service'] = self.service
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.description is not None:
            result['description'] = self.description
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeSnicResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ipAddress') is not None:
            self.ip_address = m.get('ipAddress')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
