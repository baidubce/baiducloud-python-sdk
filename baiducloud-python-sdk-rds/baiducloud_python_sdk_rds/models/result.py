"""
Result information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.para import Para


class Result(AbstractModel):
    """
    Result
    """

    def __init__(
        self,
        id=None,
        name=None,
        db_type=None,
        db_version=None,
        count=None,
        desc=None,
        dynamic=None,
        create_time=None,
        update_time=None,
        id_show=None,
        para=None,
        type=None,
        rds_property=None,
    ):
        """
        Initialize Result instance.

        :param id: 见示例
        :type id: str (optional)

        :param name: 模板名称。
        :type name: str (optional)

        :param db_type: 数据库类型。
        :type db_type: str (optional)

        :param db_version: 数据库版本。
        :type db_version: str (optional)

        :param count: 见示例
        :type count: int (optional)

        :param desc: 备注。
        :type desc: str (optional)

        :param dynamic: 见示例
        :type dynamic: bool (optional)

        :param create_time: 创建时间。
        :type create_time: str (optional)

        :param update_time: 更新时间。
        :type update_time: str (optional)

        :param id_show: 见示例
        :type id_show: str (optional)

        :param para: 参数列表。
        :type para: List[Para] (optional)

        :param type: 模板类型。
        :type type: str (optional)

        :param rds_property: 见示例
        :type rds_property: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.db_type = db_type
        self.db_version = db_version
        self.count = count
        self.desc = desc
        self.dynamic = dynamic
        self.create_time = create_time
        self.update_time = update_time
        self.id_show = id_show
        self.para = para
        self.type = type
        self.rds_property = rds_property

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.db_type is not None:
            result['dbType'] = self.db_type
        if self.db_version is not None:
            result['dbVersion'] = self.db_version
        if self.count is not None:
            result['count'] = self.count
        if self.desc is not None:
            result['desc'] = self.desc
        if self.dynamic is not None:
            result['dynamic'] = self.dynamic
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.id_show is not None:
            result['idShow'] = self.id_show
        if self.para is not None:
            result['para'] = [i.to_dict() for i in self.para]
        if self.type is not None:
            result['type'] = self.type
        if self.rds_property is not None:
            result['property'] = self.rds_property
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Result

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('dbType') is not None:
            self.db_type = m.get('dbType')
        if m.get('dbVersion') is not None:
            self.db_version = m.get('dbVersion')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('dynamic') is not None:
            self.dynamic = m.get('dynamic')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('idShow') is not None:
            self.id_show = m.get('idShow')
        if m.get('para') is not None:
            self.para = [Para().from_dict(i) for i in m.get('para')]
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('property') is not None:
            self.rds_property = m.get('property')
        return self
