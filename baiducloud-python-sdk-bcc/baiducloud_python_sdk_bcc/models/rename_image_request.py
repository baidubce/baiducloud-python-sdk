"""
Request entity for RenameImageRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RenameImageRequest(AbstractModel):
    """
    Request entity for RenameImageRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image_ids=None, name=None):
        """
        Initialize RenameImageRequest request entity.

        :param image_ids: 自定义镜像的ID列表
        :type image_ids: List[str] (optional)

        :param name: 待创建的自定义镜像名称，支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65。
        :type name: str (optional)
        """
        super().__init__()
        self.image_ids = image_ids
        self.name = name

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
        if self.image_ids is not None:
            result['imageIds'] = self.image_ids
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RenameImageRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageIds') is not None:
            self.image_ids = m.get('imageIds')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
