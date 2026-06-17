"""
Request entity for BindInstanceToTagsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class BindInstanceToTagsRequest(AbstractModel):
    """
    Request entity for BindInstanceToTagsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, change_tags, attach_related_resource_tag=None):
        """
        Initialize BindInstanceToTagsRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param change_tags: 待绑定的标签列表
        :type change_tags: List[TagModel] (required)

        :param attach_related_resource_tag: attach_related_resource_tag parameter
        :type attach_related_resource_tag: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.change_tags = change_tags
        self.attach_related_resource_tag = attach_related_resource_tag

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.change_tags is not None:
            result['changeTags'] = [i.to_dict() for i in self.change_tags]
        if self.attach_related_resource_tag is not None:
            result['attachRelatedResourceTag'] = self.attach_related_resource_tag
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindInstanceToTagsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('changeTags') is not None:
            self.change_tags = [TagModel().from_dict(i) for i in m.get('changeTags')]
        if m.get('attachRelatedResourceTag') is not None:
            self.attach_related_resource_tag = m.get('attachRelatedResourceTag')
        return self
