"""
Employee information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Employee(AbstractModel):
    """
    Employee
    """

    def __init__(self, employeename=None, position=None):
        """
        Initialize Employee instance.

        :param employeename: 姓名
        :type employeename: str (optional)

        :param position: 职位
        :type position: str (optional)
        """
        super().__init__()
        self.employeename = employeename
        self.position = position

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
        if self.employeename is not None:
            result['employeename'] = self.employeename
        if self.position is not None:
            result['position'] = self.position
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Employee

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('employeename') is not None:
            self.employeename = m.get('employeename')
        if m.get('position') is not None:
            self.position = m.get('position')
        return self
