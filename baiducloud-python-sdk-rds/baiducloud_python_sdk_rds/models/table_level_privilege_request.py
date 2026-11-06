"""
TableLevelPrivilegeRequest information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.table_level_db_privilege import TableLevelDbPrivilege

from baiducloud_python_sdk_rds.models.table_level_tb_privilege import TableLevelTbPrivilege

from baiducloud_python_sdk_rds.models.proxy_wr_flag_info import ProxyWrFlagInfo


class TableLevelPrivilegeRequest(AbstractModel):
    """
    TableLevelPrivilegeRequest
    """

    def __init__(self, type=None, globals=None, databases=None, tables=None, proxys=None):
        """
        Initialize TableLevelPrivilegeRequest instance.

        :param type: 权限类型
        :type type: str (optional)

        :param globals: 全局权限项列表
        :type globals: List[str] (optional)

        :param databases: 库级权限列表，见下表
        :type databases: List[TableLevelDbPrivilege] (optional)

        :param tables: 表级权限列表，见下表
        :type tables: List[TableLevelTbPrivilege] (optional)

        :param proxys: Proxy 读写配置列表，见下表
        :type proxys: List[ProxyWrFlagInfo] (optional)
        """
        super().__init__()
        self.type = type
        self.globals = globals
        self.databases = databases
        self.tables = tables
        self.proxys = proxys

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
        if self.type is not None:
            result['type'] = self.type
        if self.globals is not None:
            result['globals'] = self.globals
        if self.databases is not None:
            result['databases'] = [i.to_dict() for i in self.databases]
        if self.tables is not None:
            result['tables'] = [i.to_dict() for i in self.tables]
        if self.proxys is not None:
            result['proxys'] = [i.to_dict() for i in self.proxys]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableLevelPrivilegeRequest

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('globals') is not None:
            self.globals = m.get('globals')
        if m.get('databases') is not None:
            self.databases = [TableLevelDbPrivilege().from_dict(i) for i in m.get('databases')]
        if m.get('tables') is not None:
            self.tables = [TableLevelTbPrivilege().from_dict(i) for i in m.get('tables')]
        if m.get('proxys') is not None:
            self.proxys = [ProxyWrFlagInfo().from_dict(i) for i in m.get('proxys')]
        return self
