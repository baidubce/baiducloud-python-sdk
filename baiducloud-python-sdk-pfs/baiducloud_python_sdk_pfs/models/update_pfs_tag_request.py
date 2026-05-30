"""
Request entity for UpdatePFSTagRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_pfs.models.tag import Tag


class UpdatePFSTagRequest(AbstractModel):
    """
    Request entity for UpdatePFSTagRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, tags=None):
        """
        Initialize UpdatePFSTagRequest request entity.

        :param instance_id: 实例ID列表
        :type instance_id: List[str] (required)

        :param tags: 标签列表
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.tags = tags

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdatePFSTagRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
