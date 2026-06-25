"""
MentionedUserConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MentionedUserConfig(AbstractModel):
    """
    MentionedUserConfig
    """

    def __init__(self, at_all=None, user_ids=None):
        """
        Initialize MentionedUserConfig instance.

        :param at_all: 是否 @ 所有人
        :type at_all: bool (optional)

        :param user_ids: 需要 @ 的用户 ID 列表
        :type user_ids: List[str] (optional)
        """
        super().__init__()
        self.at_all = at_all
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
        if self.at_all is not None:
            result['atAll'] = self.at_all
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
        :rtype: MentionedUserConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('atAll') is not None:
            self.at_all = m.get('atAll')
        if m.get('userIds') is not None:
            self.user_ids = m.get('userIds')
        return self
