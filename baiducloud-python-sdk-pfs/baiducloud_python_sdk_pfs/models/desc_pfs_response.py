"""
Request entity for DescPfsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_pfs.models.subnet_detail import SubnetDetail
from baiducloud_python_sdk_pfs.models.tag import Tag


class DescPfsResponse(BceResponse):
    """
    DescPfsResponse
    """

    def __init__(
        self,
        capacity=None,
        create_time=None,
        description=None,
        endpoint=None,
        instance_id=None,
        instance_status=None,
        instance_type=None,
        name=None,
        payment_timing=None,
        subnet_model=None,
        usage=None,
        vpc_id=None,
        tags=None,
    ):
        """
        Initialize DescPfsResponse response.

        :param capacity: PFS实例最大容量（单位GB）
        :type capacity: int (optional)

        :param create_time: PFS实例创建时间
        :type create_time: str (optional)

        :param description: PFS实例描述信息
        :type description: str (optional)

        :param endpoint: PFS连接地址，仅basic、plus、base、baseX类型实例有该参数
        :type endpoint: str (optional)

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param instance_status: instance_status field
        :type instance_status: str (optional)

        :param instance_type: 实例类型
        :type instance_type: str (optional)

        :param name: 实例名称
        :type name: str (optional)

        :param payment_timing: 付款方式
        :type payment_timing: str (optional)

        :param subnet_model: subnet_model field
        :type subnet_model: SubnetDetail (optional)

        :param usage: PFS实例使用量（单位GB）
        :type usage: int (optional)

        :param vpc_id: PFS所在VPCID
        :type vpc_id: str (optional)

        :param tags: PFS绑定的标签
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.capacity = capacity
        self.create_time = create_time
        self.description = description
        self.endpoint = endpoint
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.name = name
        self.payment_timing = payment_timing
        self.subnet_model = subnet_model
        self.usage = usage
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
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.name is not None:
            result['name'] = self.name
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.subnet_model is not None:
            result['subnetModel'] = self.subnet_model.to_dict()
        if self.usage is not None:
            result['usage'] = self.usage
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
        :rtype: DescPfsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('subnetModel') is not None:
            self.subnet_model = SubnetDetail().from_dict(m.get('subnetModel'))
        if m.get('usage') is not None:
            self.usage = m.get('usage')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
