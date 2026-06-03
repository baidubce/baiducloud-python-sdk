"""
Request entity for TestTriggerTargetAddressRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TestTriggerTargetAddressRequest(AbstractModel):
    """
    Request entity for TestTriggerTargetAddressRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, address, headers=None):
        """
        Initialize TestTriggerTargetAddressRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param address: 目标URL
        :type address: str (required)

        :param headers: header key仅支持“Authorization”
        :type headers: object (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.address = address
        self.headers = headers

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
        if self.address is not None:
            result['address'] = self.address
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TestTriggerTargetAddressRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        return self
