"""
AccessGroupModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cfs.models.access_rule_model import AccessRuleModel


class AccessGroupModel(AbstractModel):
    """
    AccessGroupModel
    """

    def __init__(self, access_group_name=None, access_rules=None, create_time=None, description=None, fs_count=None):
        """
        Initialize AccessGroupModel instance.

        :param access_group_name:
        :type access_group_name: str (optional)

        :param access_rules:
        :type access_rules: List[AccessRuleModel] (optional)

        :param create_time:
        :type create_time: str (optional)

        :param description:
        :type description: str (optional)

        :param fs_count:
        :type fs_count: int (optional)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.access_rules = access_rules
        self.create_time = create_time
        self.description = description
        self.fs_count = fs_count

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
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        if self.access_rules is not None:
            result['accessRules'] = [i.to_dict() for i in self.access_rules]
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.fs_count is not None:
            result['fsCount'] = self.fs_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AccessGroupModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('accessRules') is not None:
            self.access_rules = [AccessRuleModel().from_dict(i) for i in m.get('accessRules')]
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('fsCount') is not None:
            self.fs_count = m.get('fsCount')
        return self
