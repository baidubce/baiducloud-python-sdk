"""
Request entity for BatchCreationOfPermissionGroupRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cfs.models.rule_info import RuleInfo


class BatchCreationOfPermissionGroupRulesRequest(AbstractModel):
    """
    Request entity for BatchCreationOfPermissionGroupRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ag_name, access_rules):
        """
        Initialize BatchCreationOfPermissionGroupRulesRequest request entity.

        :param ag_name: 指定创建的规则的权限组名字。
        :type ag_name: str (required)

        :param access_rules: 批量添加的权限组规则列表，一次请求最多创建100条
        :type access_rules: List[RuleInfo] (required)
        """
        super().__init__()
        self.ag_name = ag_name
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
        if self.ag_name is not None:
            result['ag_name'] = self.ag_name
        if self.access_rules is not None:
            result['access_rules'] = [i.to_dict() for i in self.access_rules]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BatchCreationOfPermissionGroupRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ag_name') is not None:
            self.ag_name = m.get('ag_name')
        if m.get('access_rules') is not None:
            self.access_rules = [RuleInfo().from_dict(i) for i in m.get('access_rules')]
        return self
