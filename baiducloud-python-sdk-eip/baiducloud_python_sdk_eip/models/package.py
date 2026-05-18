"""
Package information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Package(AbstractModel):
    """
    Package
    """

    def __init__(
        self,
        id=None,
        deduct_policy=None,
        package_type=None,
        status=None,
        capacity=None,
        used_capacity=None,
        create_time=None,
        active_time=None,
        expire_time=None,
    ):
        """
        Initialize Package instance.

        :param id: 共享流量包id
        :type id: str (optional)

        :param deduct_policy: deduct_policy attribute
        :type deduct_policy: str (optional)

        :param package_type: 共享流量包线路类型，当前支持 \"WebOutBytes\" 动态
        :type package_type: str (optional)

        :param status: 共享流量包状态，包含 \"RUNNING\" 使用中；\"EXPIRED\" 已过期；\"USED_UP\" 已用完
        :type status: str (optional)

        :param capacity: 共享流量包总容量，容量单位 Byte
        :type capacity: str (optional)

        :param used_capacity: 共享流量包已使用容量，容量单位 Byte
        :type used_capacity: str (optional)

        :param create_time: 共享流量包创建时间
        :type create_time: str (optional)

        :param active_time: 共享流量包激活时间
        :type active_time: str (optional)

        :param expire_time: 共享流量包过期时间
        :type expire_time: str (optional)
        """
        super().__init__()
        self.id = id
        self.deduct_policy = deduct_policy
        self.package_type = package_type
        self.status = status
        self.capacity = capacity
        self.used_capacity = used_capacity
        self.create_time = create_time
        self.active_time = active_time
        self.expire_time = expire_time

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
        if self.deduct_policy is not None:
            result['deductPolicy'] = self.deduct_policy
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.status is not None:
            result['status'] = self.status
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.used_capacity is not None:
            result['usedCapacity'] = self.used_capacity
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.active_time is not None:
            result['activeTime'] = self.active_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Package

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('deductPolicy') is not None:
            self.deduct_policy = m.get('deductPolicy')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('usedCapacity') is not None:
            self.used_capacity = m.get('usedCapacity')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('activeTime') is not None:
            self.active_time = m.get('activeTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        return self
