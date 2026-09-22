"""
Request entity for ModifyEntranceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyEntranceRequest(AbstractModel):
    """
    Request entity for ModifyEntranceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, is_defer):
        """
        Initialize ModifyEntranceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param is_defer: 是否维护时间内执行。 <li>true：维护时间内执行 <li>false：立即执行
        :type is_defer: bool (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.is_defer = is_defer

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
        if self.is_defer is not None:
            result['isDefer'] = self.is_defer
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyEntranceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isDefer') is not None:
            self.is_defer = m.get('isDefer')
        return self
