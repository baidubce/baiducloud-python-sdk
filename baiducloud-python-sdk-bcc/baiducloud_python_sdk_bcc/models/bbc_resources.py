"""
BbcResources information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.bbc_flavor_group import BbcFlavorGroup


class BbcResources(AbstractModel):
    """
    BbcResources
    """

    def __init__(self, flavor_groups=None):
        """
        Initialize BbcResources instance.

        :param flavor_groups: 实例套餐规格信息
        :type flavor_groups: List[BbcFlavorGroup] (optional)
        """
        super().__init__()
        self.flavor_groups = flavor_groups

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
        if self.flavor_groups is not None:
            result['flavorGroups'] = [i.to_dict() for i in self.flavor_groups]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BbcResources

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('flavorGroups') is not None:
            self.flavor_groups = [BbcFlavorGroup().from_dict(i) for i in m.get('flavorGroups')]
        return self
