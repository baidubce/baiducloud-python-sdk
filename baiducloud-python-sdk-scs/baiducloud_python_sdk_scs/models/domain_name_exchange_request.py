"""
Request entity for DomainNameExchangeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DomainNameExchangeRequest(AbstractModel):
    """
    Request entity for DomainNameExchangeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, source_instance_id, target_instance_id):
        """
        Initialize DomainNameExchangeRequest request entity.

        :param source_instance_id: 源实例ID
        :type source_instance_id: str (required)

        :param target_instance_id: 目标实例ID
        :type target_instance_id: str (required)
        """
        super().__init__()
        self.source_instance_id = source_instance_id
        self.target_instance_id = target_instance_id

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
        if self.source_instance_id is not None:
            result['sourceInstanceId'] = self.source_instance_id
        if self.target_instance_id is not None:
            result['targetInstanceId'] = self.target_instance_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DomainNameExchangeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sourceInstanceId') is not None:
            self.source_instance_id = m.get('sourceInstanceId')
        if m.get('targetInstanceId') is not None:
            self.target_instance_id = m.get('targetInstanceId')
        return self
