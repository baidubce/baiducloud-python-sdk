"""
Change information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Change(AbstractModel):
    """
    Change
    """

    def __init__(self, changefield=None, changebefore=None, changeafter=None, changedate=None):
        """
        Initialize Change instance.

        :param changefield: 变更事项
        :type changefield: str (optional)

        :param changebefore: 变更前内容
        :type changebefore: str (optional)

        :param changeafter: 变更后内容
        :type changeafter: str (optional)

        :param changedate: 变更日期
        :type changedate: str (optional)
        """
        super().__init__()
        self.changefield = changefield
        self.changebefore = changebefore
        self.changeafter = changeafter
        self.changedate = changedate

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
        if self.changefield is not None:
            result['changefield'] = self.changefield
        if self.changebefore is not None:
            result['changebefore'] = self.changebefore
        if self.changeafter is not None:
            result['changeafter'] = self.changeafter
        if self.changedate is not None:
            result['changedate'] = self.changedate
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Change

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('changefield') is not None:
            self.changefield = m.get('changefield')
        if m.get('changebefore') is not None:
            self.changebefore = m.get('changebefore')
        if m.get('changeafter') is not None:
            self.changeafter = m.get('changeafter')
        if m.get('changedate') is not None:
            self.changedate = m.get('changedate')
        return self
