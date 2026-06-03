"""
TagResource information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rapidfs.models.tag import Tag


class TagResource(AbstractModel):
    """
    TagResource
    """

    def __init__(self, instance_id=None, tags=None):
        """
        Initialize TagResource instance.

        :param instance_id: RapidFS 实例ID
        :type instance_id: str (optional)

        :param tags: 需要创建或者修改绑定的实例标签，解绑所有标签时则传空数组即可，见Tag
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
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
        :rtype: TagResource

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
