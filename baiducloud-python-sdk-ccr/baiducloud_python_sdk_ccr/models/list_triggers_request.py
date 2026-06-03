"""
Request entity for ListTriggersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListTriggersRequest(AbstractModel):
    """
    Request entity for ListTriggersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, policy_name=None, page_no=None, page_size=None):
        """
        Initialize ListTriggersRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param policy_name: policy_name parameter
        :type policy_name: str (optional)

        :param page_no: page_no parameter
        :type page_no: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.policy_name = policy_name
        self.page_no = page_no
        self.page_size = page_size

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
        :rtype: ListTriggersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
