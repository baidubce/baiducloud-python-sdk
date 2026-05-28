"""
Request entity for DeleteBlbServerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteBlbServerRequest(AbstractModel):
    """
    Request entity for DeleteBlbServerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, backend_server_list, client_token=None):
        """
        Initialize DeleteBlbServerRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param backend_server_list: 所有待释放的后端服务器标识符，一起组成一个数组
        :type backend_server_list: List[str] (required)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.backend_server_list = backend_server_list

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
        if self.backend_server_list is not None:
            result['backendServerList'] = self.backend_server_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteBlbServerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('backendServerList') is not None:
            self.backend_server_list = m.get('backendServerList')
        return self
