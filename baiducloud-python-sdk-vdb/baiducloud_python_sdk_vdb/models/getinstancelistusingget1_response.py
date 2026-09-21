"""
Getinstancelistusingget1Response information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_vdb.models.instance import Instance


class Getinstancelistusingget1Response(BceResponse):
    """
    Getinstancelistusingget1Response
    """

    def __init__(self, instances=None):
        """
        Initialize Getinstancelistusingget1Response instance.

        :param instances:
        :type instances: List[Instance] (optional)
        """
        super().__init__()
        self.instances = instances

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.instances is not None:
            result['instances'] = [i.to_dict() for i in self.instances]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Getinstancelistusingget1Response

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = [Instance().from_dict(i) for i in m.get('instances')]
        return self
