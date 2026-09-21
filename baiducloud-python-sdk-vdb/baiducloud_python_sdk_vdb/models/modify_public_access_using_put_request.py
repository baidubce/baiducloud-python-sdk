"""
Request entity for ModifyPublicAccessUsingPUTRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyPublicAccessUsingPUTRequest(AbstractModel):
    """
    Request entity for ModifyPublicAccessUsingPUTRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, public_access=None):
        """
        Initialize ModifyPublicAccessUsingPUTRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param public_access: public_access parameter
        :type public_access: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.public_access = public_access

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
        if self.public_access is not None:
            result['publicAccess'] = self.public_access
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyPublicAccessUsingPUTRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('publicAccess') is not None:
            self.public_access = m.get('publicAccess')
        return self
