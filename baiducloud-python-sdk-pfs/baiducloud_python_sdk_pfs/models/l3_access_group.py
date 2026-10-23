"""
L3AccessGroup information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class L3AccessGroup(AbstractModel):
    """
    L3AccessGroup
    """

    def __init__(
        self,
        access_group_name=None,
        description=None,
        rule_count=None,
        instance_count=None,
        mount_count=None,
        create_time=None,
        zone_name=None,
    ):
        """
        Initialize L3AccessGroup instance.

        :param access_group_name: 权限组名称
        :type access_group_name: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param rule_count: 规则数量
        :type rule_count: int (optional)

        :param instance_count: 关联实例数量
        :type instance_count: int (optional)

        :param mount_count: 关联挂载点数量
        :type mount_count: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param zone_name: 可用区名称
        :type zone_name: str (optional)
        """
        super().__init__()
        self.access_group_name = access_group_name
        self.description = description
        self.rule_count = rule_count
        self.instance_count = instance_count
        self.mount_count = mount_count
        self.create_time = create_time
        self.zone_name = zone_name

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
        if self.description is not None:
            result['description'] = self.description
        if self.rule_count is not None:
            result['ruleCount'] = self.rule_count
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count
        if self.mount_count is not None:
            result['mountCount'] = self.mount_count
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: L3AccessGroup

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('ruleCount') is not None:
            self.rule_count = m.get('ruleCount')
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')
        if m.get('mountCount') is not None:
            self.mount_count = m.get('mountCount')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        return self
