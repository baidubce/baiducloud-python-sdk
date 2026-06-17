"""
Request entity for ModifyReservedInstancesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.reserved_instance import ReservedInstance


class ModifyReservedInstancesRequest(AbstractModel):
    """
    Request entity for ModifyReservedInstancesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, reserved_instances):
        """
        Initialize ModifyReservedInstancesRequest request entity.

        :param reserved_instances: 要调整的预留实例券列表
        :type reserved_instances: List[ReservedInstance] (required)
        """
        super().__init__()
        self.reserved_instances = reserved_instances

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
        if self.reserved_instances is not None:
            result['reservedInstances'] = [i.to_dict() for i in self.reserved_instances]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyReservedInstancesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('reservedInstances') is not None:
            self.reserved_instances = [ReservedInstance().from_dict(i) for i in m.get('reservedInstances')]
        return self
