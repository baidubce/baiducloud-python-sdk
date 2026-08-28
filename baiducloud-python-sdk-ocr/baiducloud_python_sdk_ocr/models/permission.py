"""
Permission information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Permission(AbstractModel):
    """
    Permission
    """

    def __init__(self, name=None, province=None, liandate=None, caseno=None):
        """
        Initialize Permission instance.

        :param name: 项目名称
        :type name: str (optional)

        :param province: 地域
        :type province: str (optional)

        :param liandate: 决定日期
        :type liandate: str (optional)

        :param caseno: 决定文书号
        :type caseno: str (optional)
        """
        super().__init__()
        self.name = name
        self.province = province
        self.liandate = liandate
        self.caseno = caseno

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
        if self.name is not None:
            result['name'] = self.name
        if self.province is not None:
            result['province'] = self.province
        if self.liandate is not None:
            result['liandate'] = self.liandate
        if self.caseno is not None:
            result['caseno'] = self.caseno
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Permission

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('liandate') is not None:
            self.liandate = m.get('liandate')
        if m.get('caseno') is not None:
            self.caseno = m.get('caseno')
        return self
