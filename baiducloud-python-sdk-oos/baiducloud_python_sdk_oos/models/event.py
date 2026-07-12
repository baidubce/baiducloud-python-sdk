"""
Event information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.resource import Resource


class Event(AbstractModel):
    """
    Event
    """

    def __init__(self, name=None, description=None, service=None, region=None, resource=None):
        """
        Initialize Event instance.

        :param name: 事件名称
        :type name: str (optional)

        :param description: 事件描述
        :type description: str (optional)

        :param service: 事件来源服务
        :type service: str (optional)

        :param region: 事件所属地域
        :type region: str (optional)

        :param resource: resource attribute
        :type resource: Resource (optional)
        """
        super().__init__()
        self.name = name
        self.description = description
        self.service = service
        self.region = region
        self.resource = resource

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
        if self.description is not None:
            result['description'] = self.description
        if self.service is not None:
            result['service'] = self.service
        if self.region is not None:
            result['region'] = self.region
        if self.resource is not None:
            result['resource'] = self.resource.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Event

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('resource') is not None:
            self.resource = Resource().from_dict(m.get('resource'))
        return self
