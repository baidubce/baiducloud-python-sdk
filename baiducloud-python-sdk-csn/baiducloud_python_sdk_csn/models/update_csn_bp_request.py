"""
Request entity for UpdateCsnBpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateCsnBpRequest(AbstractModel):
    """
    Request entity for UpdateCsnBpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, csn_bp_id, name, client_token=None):
        """
        Initialize UpdateCsnBpRequest request entity.

        :param csn_bp_id: csn_bp_id parameter
        :type csn_bp_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 带宽包名称
        :type name: str (required)
        """
        super().__init__()
        self.csn_bp_id = csn_bp_id
        self.client_token = client_token
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
        :rtype: UpdateCsnBpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnBpId') is not None:
            self.csn_bp_id = m.get('csnBpId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self
