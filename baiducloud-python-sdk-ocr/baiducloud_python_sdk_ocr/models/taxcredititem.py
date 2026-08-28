"""
Taxcredititem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Taxcredititem(AbstractModel):
    """
    Taxcredititem
    """

    def __init__(self, taxpayerno=None, taxpayername=None, year=None, level=None):
        """
        Initialize Taxcredititem instance.

        :param taxpayerno: 纳税人识别号
        :type taxpayerno: str (optional)

        :param taxpayername: 纳税人名称
        :type taxpayername: str (optional)

        :param year: 评价年度
        :type year: str (optional)

        :param level: 信用等级
        :type level: str (optional)
        """
        super().__init__()
        self.taxpayerno = taxpayerno
        self.taxpayername = taxpayername
        self.year = year
        self.level = level

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
        if self.taxpayerno is not None:
            result['taxpayerno'] = self.taxpayerno
        if self.taxpayername is not None:
            result['taxpayername'] = self.taxpayername
        if self.year is not None:
            result['year'] = self.year
        if self.level is not None:
            result['level'] = self.level
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Taxcredititem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('taxpayerno') is not None:
            self.taxpayerno = m.get('taxpayerno')
        if m.get('taxpayername') is not None:
            self.taxpayername = m.get('taxpayername')
        if m.get('year') is not None:
            self.year = m.get('year')
        if m.get('level') is not None:
            self.level = m.get('level')
        return self
