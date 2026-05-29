"""
Project information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Project(AbstractModel):
    """
    Project
    """

    def __init__(
        self,
        uuid=None,
        name=None,
        description=None,
        top=None,
        log_store_count=None,
        created_time=None,
        updated_time=None,
    ):
        """
        Initialize Project instance.

        :param uuid: 日志组UUID
        :type uuid: str (optional)

        :param name: 日志组名称
        :type name: str (optional)

        :param description: 日志组描述
        :type description: str (optional)

        :param top: 日志组是否置顶
        :type top: bool (optional)

        :param log_store_count: 日志组中日志集的个数
        :type log_store_count: int (optional)

        :param created_time: 日志组创建的日期时间
        :type created_time: datetime (optional)

        :param updated_time: 日志组最后修改的日期时间
        :type updated_time: datetime (optional)
        """
        super().__init__()
        self.uuid = uuid
        self.name = name
        self.description = description
        self.top = top
        self.log_store_count = log_store_count
        self.created_time = created_time
        self.updated_time = updated_time

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
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.top is not None:
            result['top'] = self.top
        if self.log_store_count is not None:
            result['logStoreCount'] = self.log_store_count
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Project

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('logStoreCount') is not None:
            self.log_store_count = m.get('logStoreCount')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self
