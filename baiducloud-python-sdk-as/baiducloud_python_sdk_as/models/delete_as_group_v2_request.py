"""
Request entity for DeleteAsGroupV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteAsGroupV2Request(AbstractModel):
    """
    Request entity for DeleteAsGroupV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_ids):
        """
        Initialize DeleteAsGroupV2Request request entity.

        :param group_ids: 伸缩组id列表
        :type group_ids: List[str] (required)
        """
        super().__init__()
        self.group_ids = group_ids

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
        if self.group_ids is not None:
            result['groupIds'] = self.group_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAsGroupV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupIds') is not None:
            self.group_ids = m.get('groupIds')
        return self
