"""
Request entity for AdjustNumV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AdjustNumV2Request(AbstractModel):
    """
    Request entity for AdjustNumV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, adjust_node, adjust_num):
        """
        Initialize AdjustNumV2Request request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param adjust_node: adjust_node parameter
        :type adjust_node: str (required)

        :param adjust_num: 期望调整到的节点数
        :type adjust_num: int (required)
        """
        super().__init__()
        self.group_id = group_id
        self.adjust_node = adjust_node
        self.adjust_num = adjust_num

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
        if self.adjust_num is not None:
            result['adjustNum'] = self.adjust_num
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AdjustNumV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('adjustNode') is not None:
            self.adjust_node = m.get('adjustNode')
        if m.get('adjustNum') is not None:
            self.adjust_num = m.get('adjustNum')
        return self
