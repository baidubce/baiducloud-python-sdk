"""
AzInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AzInfo(AbstractModel):
    """
    AzInfo
    """

    def __init__(self, availability_zone=None, count=None, subnet_id=None):
        """
        Initialize AzInfo instance.

        :param availability_zone:
        :type availability_zone: str (optional)

        :param count:
        :type count: int (optional)

        :param subnet_id:
        :type subnet_id: str (optional)
        """
        super().__init__()
        self.availability_zone = availability_zone
        self.count = count
        self.subnet_id = subnet_id

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
        if self.count is not None:
            result['count'] = self.count
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AzInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('availabilityZone') is not None:
            self.availability_zone = m.get('availabilityZone')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        return self
