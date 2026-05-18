"""
BandwidthPackage information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BandwidthPackage(AbstractModel):
    """
    BandwidthPackage
    """

    def __init__(
        self,
        name=None,
        id=None,
        bind_type=None,
        bandwidth_in_mbps=None,
        instance_id=None,
        eips=None,
        create_time=None,
        auto_release_time=None,
        type=None,
        region=None,
    ):
        """
        Initialize BandwidthPackage instance.

        :param name: 带宽包名称
        :type name: str (optional)

        :param id: 带宽包id
        :type id: str (optional)

        :param bind_type: 带宽包所绑定的资源的类型，\"eip\"（弹性公网EIP）或\"eipgroup\"（共享带宽）
        :type bind_type: str (optional)

        :param bandwidth_in_mbps: 带宽包的带宽值
        :type bandwidth_in_mbps: int (optional)

        :param instance_id: 带宽包绑定资源的id
        :type instance_id: str (optional)

        :param eips: eips attribute
        :type eips: List[str] (optional)

        :param create_time: 带宽包创建时间
        :type create_time: str (optional)

        :param auto_release_time: 带宽包的自动释放时间,若未设置则同所绑定资源的到期时间一致
        :type auto_release_time: str (optional)

        :param type: 带宽包的类型，BandwidthPackage（带宽包）或 AccelerationPackage（跨境加速包）
        :type type: str (optional)

        :param region: 带宽包所属区域
        :type region: str (optional)
        """
        super().__init__()
        self.name = name
        self.id = id
        self.bind_type = bind_type
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.instance_id = instance_id
        self.eips = eips
        self.create_time = create_time
        self.auto_release_time = auto_release_time
        self.type = type
        self.region = region

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
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.bind_type is not None:
            result['bindType'] = self.bind_type
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.eips is not None:
            result['eips'] = self.eips
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.auto_release_time is not None:
            result['autoReleaseTime'] = self.auto_release_time
        if self.type is not None:
            result['type'] = self.type
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BandwidthPackage

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('bindType') is not None:
            self.bind_type = m.get('bindType')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('eips') is not None:
            self.eips = m.get('eips')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('autoReleaseTime') is not None:
            self.auto_release_time = m.get('autoReleaseTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self
