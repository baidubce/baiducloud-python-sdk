"""
Request entity for ViewSecurityGroupResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.group import Group
from baiducloud_python_sdk_scs.models.rule import Rule


class ViewSecurityGroupResponse(BceResponse):
    """
    ViewSecurityGroupResponse
    """

    def __init__(self, groups=None, active_rules=None):
        """
        Initialize ViewSecurityGroupResponse response.

        :param groups: 安全组列表。
        :type groups: List[Group] (optional)

        :param active_rules: 安全组规则列表。
        :type active_rules: List[Rule] (optional)
        """
        super().__init__()
        self.groups = groups
        self.active_rules = active_rules

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
        if self.groups is not None:
            result['groups'] = [i.to_dict() for i in self.groups]
        if self.active_rules is not None:
            result['activeRules'] = [i.to_dict() for i in self.active_rules]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ViewSecurityGroupResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groups') is not None:
            self.groups = [Group().from_dict(i) for i in m.get('groups')]
        if m.get('activeRules') is not None:
            self.active_rules = [Rule().from_dict(i) for i in m.get('activeRules')]
        return self
