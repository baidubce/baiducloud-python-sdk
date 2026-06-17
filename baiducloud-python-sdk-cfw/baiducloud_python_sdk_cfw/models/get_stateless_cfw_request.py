"""
Request entity for GetStatelessCfwRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetStatelessCfwRequest(AbstractModel):
    """
    Request entity for GetStatelessCfwRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cfw_id):
        """
        Initialize GetStatelessCfwRequest request entity.

        :param cfw_id: cfw_id parameter
        :type cfw_id: str (required)
        """
        super().__init__()
        self.cfw_id = cfw_id

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
        :rtype: GetStatelessCfwRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        return self
