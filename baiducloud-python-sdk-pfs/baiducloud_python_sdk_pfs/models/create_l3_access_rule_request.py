"""
Request entity for CreateL3AccessRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_pfs.models.l3_access_rule_create_info import L3AccessRuleCreateInfo


class CreateL3AccessRuleRequest(AbstractModel):
    """
    Request entity for CreateL3AccessRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, access_group_name, zone_name, access_rules):
        """
        Initialize CreateL3AccessRuleRequest request entity.

        :param access_group_name: 权限组名称
        :type access_group_name: str (required)

        :param zone_name: 可用区名称
        :type zone_name: str (required)

        :param access_rules: 待创建的规则列表，支持批量
        :type access_rules: list[L3AccessRuleCreateInfo] (required)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.zone_name = zone_name
        self.access_rules = access_rules

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
        if self.access_rules is not None:
            result['accessRules'] = [item.to_dict() for item in self.access_rules]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateL3AccessRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('accessRules') is not None:
            self.access_rules = [L3AccessRuleCreateInfo(None, None, None, None).from_dict(item)
                                 for item in m.get('accessRules')]
        return self
