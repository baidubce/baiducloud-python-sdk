"""
Request entity for DeletePermissionGroupRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeletePermissionGroupRuleRequest(AbstractModel):
    """
    Request entity for DeletePermissionGroupRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ag_name, ar_id):
        """
        Initialize DeletePermissionGroupRuleRequest request entity.

        :param ag_name: ag_name parameter
        :type ag_name: str (required)

        :param ar_id: ar_id parameter
        :type ar_id: str (required)
        """
        super().__init__()
        self.ag_name = ag_name
        self.ar_id = ar_id

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
        :rtype: DeletePermissionGroupRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('agName') is not None:
            self.ag_name = m.get('agName')
        if m.get('arId') is not None:
            self.ar_id = m.get('arId')
        return self
