"""
EriInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EriInfo(AbstractModel):
    """
    EriInfo
    """

    def __init__(self, name=None, eri_id=None):
        """
        Initialize EriInfo instance.

        :param name: eri网卡名（查询实例列表、查询指定实例详情）
        :type name: str (optional)

        :param eri_id: eri网卡ID（查询实例列表、查询指定实例详情）
        :type eri_id: str (optional)
        """
        super().__init__()
        self.name = name
        self.eri_id = eri_id

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
        if self.eri_id is not None:
            result['eriId'] = self.eri_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EriInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('eriId') is not None:
            self.eri_id = m.get('eriId')
        return self
