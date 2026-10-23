"""
Request entity for DeleteL3AccessRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteL3AccessRuleRequest(AbstractModel):
    """
    Request entity for DeleteL3AccessRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, access_group_name, zone_name, access_rule_id):
        """
        Initialize DeleteL3AccessRuleRequest request entity.

        :param access_group_name: 权限组名称
        :type access_group_name: str (required)

        :param zone_name: 可用区名称
        :type zone_name: str (required)

        :param access_rule_id: 要删除的规则 ID
        :type access_rule_id: int (required)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.zone_name = zone_name
        self.access_rule_id = access_rule_id

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
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.access_rule_id is not None:
            result['accessRuleId'] = self.access_rule_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteL3AccessRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('accessRuleId') is not None:
            self.access_rule_id = m.get('accessRuleId')
        return self
