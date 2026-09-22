"""
Request entity for QueryMemoryScalingConfigResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.mem_spec import MemSpec


class QueryMemoryScalingConfigResponse(BceResponse):
    """
    QueryMemoryScalingConfigResponse
    """

    def __init__(self, mem_spec=None):
        """
        Initialize QueryMemoryScalingConfigResponse response.

        :param mem_spec: mem_spec field
        :type mem_spec: MemSpec (optional)
        """
        super().__init__()
        self.mem_spec = mem_spec

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
        if self.mem_spec is not None:
            result['memSpec'] = self.mem_spec.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryMemoryScalingConfigResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('memSpec') is not None:
            self.mem_spec = MemSpec().from_dict(m.get('memSpec'))
        return self
