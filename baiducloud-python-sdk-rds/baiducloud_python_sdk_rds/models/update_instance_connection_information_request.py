"""
Request entity for UpdateInstanceConnectionInformationRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateInstanceConnectionInformationRequest(AbstractModel):
    """
    Request entity for UpdateInstanceConnectionInformationRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, address):
        """
        Initialize UpdateInstanceConnectionInformationRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param address: 域名前缀。域名前缀 由小写字母和数字组 成，以小写字母开头 ，长度在3-30之间
        :type address: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.address = address

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateInstanceConnectionInformationRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('address') is not None:
            self.address = m.get('address')
        return self
