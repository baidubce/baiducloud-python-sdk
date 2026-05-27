"""
Request entity for UnbindCsnBpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UnbindCsnBpRequest(AbstractModel):
    """
    Request entity for UnbindCsnBpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, csn_bp_id, action, csn_id, client_token=None):
        """
        Initialize UnbindCsnBpRequest request entity.

        :param csn_bp_id: csn_bp_id parameter
        :type csn_bp_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param action: action parameter
        :type action: str (required)

        :param csn_id: 云智能网的ID
        :type csn_id: str (required)
        """
        super().__init__()
        self.csn_bp_id = csn_bp_id
        self.client_token = client_token
        self.action = action
        self.csn_id = csn_id

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
        if self.csn_id is not None:
            result['csnId'] = self.csn_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UnbindCsnBpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnBpId') is not None:
            self.csn_bp_id = m.get('csnBpId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('csnId') is not None:
            self.csn_id = m.get('csnId')
        return self
