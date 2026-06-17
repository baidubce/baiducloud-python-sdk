"""
AlarmResource information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AlarmResource(AbstractModel):
    """
    AlarmResource
    """

    def __init__(self, scope=None, resource_type=None, region=None, identifiers=None, properties=None):
        """
        Initialize AlarmResource instance.

        :param scope: 云产品
        :type scope: str (optional)

        :param resource_type: 资源类型
        :type resource_type: str (optional)

        :param region: 实例所属地域
        :type region: str (optional)

        :param identifiers: 实例ID键值对，key为维度名，value为维度值
        :type identifiers: Dict[str, str] (optional)

        :param properties: 实例属性键值对
        :type properties: Dict[str, str] (optional)
        """
        super().__init__()
        self.scope = scope
        self.resource_type = resource_type
        self.region = region
        self.identifiers = identifiers
        self.properties = properties

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
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.region is not None:
            result['region'] = self.region
        if self.identifiers is not None:
            result['identifiers'] = self.identifiers
        if self.properties is not None:
            result['properties'] = self.properties
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlarmResource

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('identifiers') is not None:
            self.identifiers = m.get('identifiers')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        return self
