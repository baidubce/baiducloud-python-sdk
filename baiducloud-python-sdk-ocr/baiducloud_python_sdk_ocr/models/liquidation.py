"""
Liquidation information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Liquidation(AbstractModel):
    """
    Liquidation
    """

    def __init__(self, leader=None, member=None):
        """
        Initialize Liquidation instance.

        :param leader: 清算组负责人
        :type leader: str (optional)

        :param member: 清算组成员
        :type member: str (optional)
        """
        super().__init__()
        self.leader = leader
        self.member = member

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
        if self.leader is not None:
            result['leader'] = self.leader
        if self.member is not None:
            result['member'] = self.member
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Liquidation

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('leader') is not None:
            self.leader = m.get('leader')
        if m.get('member') is not None:
            self.member = m.get('member')
        return self
