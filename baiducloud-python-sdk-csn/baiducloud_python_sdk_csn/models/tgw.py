"""
Tgw information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Tgw(AbstractModel):
    """
    Tgw
    """

    def __init__(self, tgw_id=None, csn_id=None, name=None, region=None, description=None):
        """
        Initialize Tgw instance.

        :param tgw_id: TGW的ID
        :type tgw_id: str (optional)

        :param csn_id: 云智能网的ID
        :type csn_id: str (optional)

        :param name: TGW的名称
        :type name: str (optional)

        :param region: TGW的region
        :type region: str (optional)

        :param description: TGW的描述信息
        :type description: str (optional)
        """
        super().__init__()
        self.tgw_id = tgw_id
        self.csn_id = csn_id
        self.name = name
        self.region = region
        self.description = description

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
        if self.tgw_id is not None:
            result['tgwId'] = self.tgw_id
        if self.csn_id is not None:
            result['csnId'] = self.csn_id
        if self.name is not None:
            result['name'] = self.name
        if self.region is not None:
            result['region'] = self.region
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Tgw

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tgwId') is not None:
            self.tgw_id = m.get('tgwId')
        if m.get('csnId') is not None:
            self.csn_id = m.get('csnId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
