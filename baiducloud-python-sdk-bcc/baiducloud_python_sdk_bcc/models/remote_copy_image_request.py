"""
Request entity for RemoteCopyImageRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoteCopyImageRequest(AbstractModel):
    """
    Request entity for RemoteCopyImageRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image_id, dest_region, name=None):
        """
        Initialize RemoteCopyImageRequest request entity.

        :param image_id: image_id parameter
        :type image_id: str (required)

        :param name: 复制镜像名
        :type name: str (optional)

        :param dest_region: 目的regionId，可以传多个
        :type dest_region: List[str] (required)
        """
        super().__init__()
        self.image_id = image_id
        self.name = name
        self.dest_region = dest_region

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
        if self.name is not None:
            result['name'] = self.name
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoteCopyImageRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        return self
