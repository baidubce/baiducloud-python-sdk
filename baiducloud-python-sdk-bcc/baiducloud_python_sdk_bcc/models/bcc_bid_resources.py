"""
BccBidResources information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.bcc_bid_flavors import BccBidFlavors


class BccBidResources(AbstractModel):
    """
    BccBidResources
    """

    def __init__(self, instance_type=None, flavors=None):
        """
        Initialize BccBidResources instance.

        :param instance_type: 实例类型
        :type instance_type: str (optional)

        :param flavors: 套餐规格列表
        :type flavors: List[BccBidFlavors] (optional)
        """
        super().__init__()
        self.instance_type = instance_type
        self.flavors = flavors

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
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.flavors is not None:
            result['flavors'] = [i.to_dict() for i in self.flavors]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BccBidResources

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('flavors') is not None:
            self.flavors = [BccBidFlavors().from_dict(i) for i in m.get('flavors')]
        return self
