"""
AlarmTarget information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_apm.models.tag import Tag


class AlarmTarget(AbstractModel):
    """
    AlarmTarget
    """

    def __init__(self, type=None, tags=None, services=None):
        """
        Initialize AlarmTarget instance.

        :param type: type attribute
        :type type: str (optional)

        :param tags: 若type=SERVICE_TAGS，填写目标tags
        :type tags: List[Tag] (optional)

        :param services: 若type=SERVICES，填写目标服务名称列表
        :type services: List[str] (optional)
        """
        super().__init__()
        self.type = type
        self.tags = tags
        self.services = services

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
        if self.type is not None:
            result['type'] = self.type
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.services is not None:
            result['services'] = self.services
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlarmTarget

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('services') is not None:
            self.services = m.get('services')
        return self
