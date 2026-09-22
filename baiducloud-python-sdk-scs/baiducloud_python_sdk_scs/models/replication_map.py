"""
ReplicationMap information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReplicationMap(AbstractModel):
    """
    ReplicationMap
    """

    def __init__(self, availability_zone=None, subnet_id=None, is_master=None):
        """
        Initialize ReplicationMap instance.

        :param availability_zone: availability_zone attribute
        :type availability_zone: str (optional)

        :param subnet_id: 子网Id
        :type subnet_id: str (optional)

        :param is_master: 是否是主节点 1代表主 0代表从。主节点有且仅有一个。
        :type is_master: int (optional)
        """
        super().__init__()
        self.availability_zone = availability_zone
        self.subnet_id = subnet_id
        self.is_master = is_master

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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplicationMap

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
        return self
