"""
Mention information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Mention(AbstractModel):
    """
    Mention
    """

    def __init__(self, type=None, user_ids=None):
        """
        Initialize Mention instance.

        :param type: 提醒方式，可选值：NONE（不通知）/ ALL（通知全体）/ USERS（通知用户）
        :type type: str (optional)

        :param user_ids: 当type=USERS时必填，通知用户ID列表
        :type user_ids: List[str] (optional)
        """
        super().__init__()
        self.type = type
        self.user_ids = user_ids

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.user_ids is not None:
            result['userIds'] = self.user_ids
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Mention

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        return self
