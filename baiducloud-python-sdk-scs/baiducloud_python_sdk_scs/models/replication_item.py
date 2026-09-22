"""
ReplicationItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReplicationItem(AbstractModel):
    """
    ReplicationItem
    """

    def __init__(self, availability_zone=None, subnet_id=None, is_master=None, weight=None):
        """
        Initialize ReplicationItem instance.

        :param availability_zone: 可用区。示例：cn-bj-a
        :type availability_zone: str (optional)

        :param subnet_id: 子网ID。示例：sbn-x94w3r601111
        :type subnet_id: str (optional)

        :param is_master: 是否是主节点。主节点有且仅有一个。  <li>1：主节点 <li> 0：从节点
        :type is_master: int (optional)

        :param weight: 只读实例权重，取值 1~100（只读实例时需要）
        :type weight: int (optional)
        """
        super().__init__()
        self.availability_zone = availability_zone
        self.subnet_id = subnet_id
        self.is_master = is_master
        self.weight = weight

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
        if self.availability_zone is not None:
            result['availabilityZone'] = self.availability_zone
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.is_master is not None:
            result['isMaster'] = self.is_master
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplicationItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('availabilityZone') is not None:
            self.availability_zone = m.get('availabilityZone')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('isMaster') is not None:
            self.is_master = m.get('isMaster')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self
