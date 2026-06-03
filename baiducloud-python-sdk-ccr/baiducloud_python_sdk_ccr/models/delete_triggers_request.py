"""
Request entity for DeleteTriggersRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteTriggersRequest(AbstractModel):
    """
    Request entity for DeleteTriggersRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, items):
        """
        Initialize DeleteTriggersRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param items: 触发器策略ID数组
        :type items: List[int] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.items = items

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
        if self.items is not None:
            result['items'] = self.items
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteTriggersRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('items') is not None:
            self.items = m.get('items')
        return self
