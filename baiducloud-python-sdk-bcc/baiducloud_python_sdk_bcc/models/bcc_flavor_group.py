"""
BccFlavorGroup information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.bcc_flavor import BccFlavor


class BccFlavorGroup(AbstractModel):
    """
    BccFlavorGroup
    """

    def __init__(self, group_id=None, flavors=None):
        """
        Initialize BccFlavorGroup instance.

        :param group_id: 实例套餐规格族
        :type group_id: str (optional)

        :param flavors: 实例套餐规格
        :type flavors: List[BccFlavor] (optional)
        """
        super().__init__()
        self.group_id = group_id
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
        if self.group_id is not None:
            result['groupId'] = self.group_id
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
        :rtype: BccFlavorGroup

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('flavors') is not None:
            self.flavors = [BccFlavor().from_dict(i) for i in m.get('flavors')]
        return self
