"""
AppList information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppList(AbstractModel):
    """
    AppList
    """

    def __init__(
        self,
        app_id=None,
        app_name=None,
        weight=None,
        ro_group_id=None,
        source_app_id=None,
        status=None,
        create_time=None,
        update_time=None,
        app_status=None,
        app_id_short=None,
    ):
        """
        Initialize AppList instance.

        :param app_id: 只读实例ID。
        :type app_id: str (optional)

        :param app_name: 只读实例名称。
        :type app_name: str (optional)

        :param weight: 只读实例权重。
        :type weight: int (optional)

        :param ro_group_id: 只读组ID。
        :type ro_group_id: str (optional)

        :param source_app_id: 资源ID。
        :type source_app_id: str (optional)

        :param status: status attribute
        :type status: str (optional)

        :param create_time: 创建时间。
        :type create_time: str (optional)

        :param update_time: 更新时间。
        :type update_time: str (optional)

        :param app_status: app_status attribute
        :type app_status: str (optional)

        :param app_id_short: 只读实例短ID。
        :type app_id_short: str (optional)
        """
        super().__init__()
        self.app_id = app_id
        self.app_name = app_name
        self.weight = weight
        self.ro_group_id = ro_group_id
        self.source_app_id = source_app_id
        self.status = status
        self.create_time = create_time
        self.update_time = update_time
        self.app_status = app_status
        self.app_id_short = app_id_short

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
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.weight is not None:
            result['weight'] = self.weight
        if self.ro_group_id is not None:
            result['roGroupId'] = self.ro_group_id
        if self.source_app_id is not None:
            result['sourceAppId'] = self.source_app_id
        if self.status is not None:
            result['status'] = self.status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.app_status is not None:
            result['appStatus'] = self.app_status
        if self.app_id_short is not None:
            result['appIdShort'] = self.app_id_short
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppList

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        if m.get('roGroupId') is not None:
            self.ro_group_id = m.get('roGroupId')
        if m.get('sourceAppId') is not None:
            self.source_app_id = m.get('sourceAppId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('appStatus') is not None:
            self.app_status = m.get('appStatus')
        if m.get('appIdShort') is not None:
            self.app_id_short = m.get('appIdShort')
        return self
