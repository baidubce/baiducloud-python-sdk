"""
Request entity for DeleteAccountRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteAccountRequest(AbstractModel):
    """
    Request entity for DeleteAccountRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, user_name):
        """
        Initialize DeleteAccountRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param user_name: 要删除的账号名称。
        :type user_name: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.user_name = user_name

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
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAccountRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self
