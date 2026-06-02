"""
Request entity for DescFilesetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescFilesetRequest(AbstractModel):
    """
    Request entity for DescFilesetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, fileset_id):
        """
        Initialize DescFilesetRequest request entity.

        :param instance_id: fileset所属PFS实例Id
        :type instance_id: str (required)

        :param fileset_id: fileset Id
        :type fileset_id: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.fileset_id = fileset_id

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.fileset_id is not None:
            result['filesetId'] = self.fileset_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescFilesetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('filesetId') is not None:
            self.fileset_id = m.get('filesetId')
        return self
