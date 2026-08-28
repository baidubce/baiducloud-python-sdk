"""
Branch information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Branch(AbstractModel):
    """
    Branch
    """

    def __init__(self, companycode=None, companyname=None, authority=None, creditno=None, legalperson=None):
        """
        Initialize Branch instance.

        :param companycode: 注册号
        :type companycode: str (optional)

        :param companyname: 名称
        :type companyname: str (optional)

        :param authority: 登记机关
        :type authority: str (optional)

        :param creditno: 统一社会信用代码
        :type creditno: str (optional)

        :param legalperson: 法人姓名
        :type legalperson: str (optional)
        """
        super().__init__()
        self.companycode = companycode
        self.companyname = companyname
        self.authority = authority
        self.creditno = creditno
        self.legalperson = legalperson

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
        if self.companycode is not None:
            result['companycode'] = self.companycode
        if self.companyname is not None:
            result['companyname'] = self.companyname
        if self.authority is not None:
            result['authority'] = self.authority
        if self.creditno is not None:
            result['creditno'] = self.creditno
        if self.legalperson is not None:
            result['legalperson'] = self.legalperson
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Branch

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('companycode') is not None:
            self.companycode = m.get('companycode')
        if m.get('companyname') is not None:
            self.companyname = m.get('companyname')
        if m.get('authority') is not None:
            self.authority = m.get('authority')
        if m.get('creditno') is not None:
            self.creditno = m.get('creditno')
        if m.get('legalperson') is not None:
            self.legalperson = m.get('legalperson')
        return self
