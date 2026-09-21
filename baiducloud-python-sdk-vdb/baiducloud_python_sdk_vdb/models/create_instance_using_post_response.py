"""
Request entity for CreateInstanceUsingPOSTResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateInstanceUsingPOSTResponse(BceResponse):
    """
    CreateInstanceUsingPOSTResponse
    """

    def __init__(self, enable_encryption=None, instance_id_list=None, order_id=None):
        """
        Initialize CreateInstanceUsingPOSTResponse response.

        :param enable_encryption: enable_encryption field
        :type enable_encryption: bool (optional)

        :param instance_id_list: instance_id_list field
        :type instance_id_list: List[str] (optional)

        :param order_id: order_id field
        :type order_id: str (optional)
        """
        super().__init__()
        self.enable_encryption = enable_encryption
        self.instance_id_list = instance_id_list
        self.order_id = order_id

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.enable_encryption is not None:
            result['enableEncryption'] = self.enable_encryption
        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateInstanceUsingPOSTResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enableEncryption') is not None:
            self.enable_encryption = m.get('enableEncryption')
        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self
