"""
Request entity for HotGroupForbidWriteRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HotGroupForbidWriteRequest(AbstractModel):
    """
    Request entity for HotGroupForbidWriteRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, forbid_write_flag):
        """
        Initialize HotGroupForbidWriteRequest request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param forbid_write_flag: 禁写标识（false 未禁写 true 禁写）
        :type forbid_write_flag: bool (required)
        """
        super().__init__()
        self.group_id = group_id
        self.forbid_write_flag = forbid_write_flag

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
        if self.forbid_write_flag is not None:
            result['forbidWriteFlag'] = self.forbid_write_flag
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HotGroupForbidWriteRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('forbidWriteFlag') is not None:
            self.forbid_write_flag = m.get('forbidWriteFlag')
        return self
