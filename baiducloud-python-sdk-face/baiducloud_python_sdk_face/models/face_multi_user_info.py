"""
FaceMultiUserInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceMultiUserInfo(AbstractModel):
    """
    FaceMultiUserInfo
    """

    def __init__(self, score=None, group_id=None, user_id=None, user_info=None):
        """
        Initialize FaceMultiUserInfo instance.

        :param score: 用户的匹配得分，80分以上可判断为同一人
        :type score: float (optional)

        :param group_id: 用户所属的group_id
        :type group_id: str (optional)

        :param user_id: 用户的user_id
        :type user_id: str (optional)

        :param user_info: 注册用户时携带的user_info
        :type user_info: str (optional)
        """
        super().__init__()
        self.score = score
        self.group_id = group_id
        self.user_id = user_id
        self.user_info = user_info

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
        if self.score is not None:
            result['score'] = self.score
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_info is not None:
            result['user_info'] = self.user_info
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceMultiUserInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_info') is not None:
            self.user_info = m.get('user_info')
        return self
