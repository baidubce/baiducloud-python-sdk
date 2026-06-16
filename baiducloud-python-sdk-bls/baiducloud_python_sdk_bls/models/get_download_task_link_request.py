"""
Request entity for GetDownloadTaskLinkRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetDownloadTaskLinkRequest(AbstractModel):
    """
    Request entity for GetDownloadTaskLinkRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, uuid):
        """
        Initialize GetDownloadTaskLinkRequest request entity.

        :param uuid: uuid parameter
        :type uuid: str (required)
        """
        super().__init__()
        self.uuid = uuid

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetDownloadTaskLinkRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self
