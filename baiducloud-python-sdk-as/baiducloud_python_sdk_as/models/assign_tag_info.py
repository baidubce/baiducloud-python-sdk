"""
AssignTagInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.tag_info import TagInfo


class AssignTagInfo(AbstractModel):
    """
    AssignTagInfo
    """

    def __init__(self, resource_id=None, relation_tag=None, tags=None):
        """
        Initialize AssignTagInfo instance.

        :param resource_id: 资源id
        :type resource_id: str (optional)

        :param relation_tag: 是否绑定标签
        :type relation_tag: bool (optional)

        :param tags: 标签信息
        :type tags: List[TagInfo] (optional)
        """
        super().__init__()
        self.resource_id = resource_id
        self.relation_tag = relation_tag
        self.tags = tags

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
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.relation_tag is not None:
            result['relationTag'] = self.relation_tag
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AssignTagInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('relationTag') is not None:
            self.relation_tag = m.get('relationTag')
        if m.get('tags') is not None:
            self.tags = [TagInfo().from_dict(i) for i in m.get('tags')]
        return self
