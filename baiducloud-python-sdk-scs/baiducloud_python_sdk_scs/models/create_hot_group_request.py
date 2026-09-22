"""
Request entity for CreateHotGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.leader import Leader


class CreateHotGroupRequest(AbstractModel):
    """
    Request entity for CreateHotGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, leader):
        """
        Initialize CreateHotGroupRequest request entity.

        :param leader: leader parameter
        :type leader: Leader (required)
        """
        super().__init__()
        self.leader = leader

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
        if self.leader is not None:
            result['leader'] = self.leader.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateHotGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('leader') is not None:
            self.leader = Leader().from_dict(m.get('leader'))
        return self
