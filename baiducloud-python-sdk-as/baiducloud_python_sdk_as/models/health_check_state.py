"""
HealthCheckState information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_as.models.check_entity import CheckEntity


class HealthCheckState(AbstractModel):
    """
    HealthCheckState
    """

    def __init__(
        self, check_id=None, group_id=None, account_id=None, state=None, check_entities=None, create_time=None
    ):
        """
        Initialize HealthCheckState instance.

        :param check_id: 检查id
        :type check_id: str (optional)

        :param group_id: 伸缩组id
        :type group_id: str (optional)

        :param account_id: 账号id
        :type account_id: str (optional)

        :param state: 检查状态（CHECKING-正在检查、CHECK_SUCCESS-检查通过、CHECK_FAILED-检查失败）
        :type state: str (optional)

        :param check_entities: 检查项列表
        :type check_entities: List[CheckEntity] (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)
        """
        super().__init__()
        self.check_id = check_id
        self.group_id = group_id
        self.account_id = account_id
        self.state = state
        self.check_entities = check_entities
        self.create_time = create_time

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
        if self.check_id is not None:
            result['checkId'] = self.check_id
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.state is not None:
            result['state'] = self.state
        if self.check_entities is not None:
            result['checkEntities'] = [i.to_dict() for i in self.check_entities]
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HealthCheckState

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('checkId') is not None:
            self.check_id = m.get('checkId')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('checkEntities') is not None:
            self.check_entities = [CheckEntity().from_dict(i) for i in m.get('checkEntities')]
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self
