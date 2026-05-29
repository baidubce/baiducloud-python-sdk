"""
Request entity for UpdateFileSystemLabelsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cfs.models.tag import Tag


class UpdateFileSystemLabelsRequest(AbstractModel):
    """
    Request entity for UpdateFileSystemLabelsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, tag, fs_id, tags=None):
        """
        Initialize UpdateFileSystemLabelsRequest request entity.

        :param tag: tag parameter
        :type tag: str (required)

        :param fs_id: FileSystem ID 列表
        :type fs_id: List[str] (required)

        :param tags: tags parameter
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.tag = tag
        self.fs_id = fs_id
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
        if self.fs_id is not None:
            result['fsId'] = self.fs_id
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
        :rtype: UpdateFileSystemLabelsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('fsId') is not None:
            self.fs_id = m.get('fsId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
