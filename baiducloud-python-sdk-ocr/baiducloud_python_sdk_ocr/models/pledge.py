"""
Pledge information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Pledge(AbstractModel):
    """
    Pledge
    """

    def __init__(
        self,
        registno=None,
        pledgor=None,
        pledgorno=None,
        pledgee=None,
        pledgeeno=None,
        pledgedamount=None,
        regdate=None,
        publicdate=None,
        status=None,
    ):
        """
        Initialize Pledge instance.

        :param registno: 质权登记编号
        :type registno: str (optional)

        :param pledgor: 出质人
        :type pledgor: str (optional)

        :param pledgorno: 出质人证照编号
        :type pledgorno: str (optional)

        :param pledgee: 质权人
        :type pledgee: str (optional)

        :param pledgeeno: 质权人证照编号
        :type pledgeeno: str (optional)

        :param pledgedamount: 出质股权数额
        :type pledgedamount: str (optional)

        :param regdate: 股权出质设立登记日期
        :type regdate: str (optional)

        :param publicdate: 公示时间
        :type publicdate: str (optional)

        :param status: 出质状态
        :type status: str (optional)
        """
        super().__init__()
        self.registno = registno
        self.pledgor = pledgor
        self.pledgorno = pledgorno
        self.pledgee = pledgee
        self.pledgeeno = pledgeeno
        self.pledgedamount = pledgedamount
        self.regdate = regdate
        self.publicdate = publicdate
        self.status = status

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
        if self.registno is not None:
            result['registno'] = self.registno
        if self.pledgor is not None:
            result['pledgor'] = self.pledgor
        if self.pledgorno is not None:
            result['pledgorno'] = self.pledgorno
        if self.pledgee is not None:
            result['pledgee'] = self.pledgee
        if self.pledgeeno is not None:
            result['pledgeeno'] = self.pledgeeno
        if self.pledgedamount is not None:
            result['pledgedamount'] = self.pledgedamount
        if self.regdate is not None:
            result['regdate'] = self.regdate
        if self.publicdate is not None:
            result['publicdate'] = self.publicdate
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Pledge

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('registno') is not None:
            self.registno = m.get('registno')
        if m.get('pledgor') is not None:
            self.pledgor = m.get('pledgor')
        if m.get('pledgorno') is not None:
            self.pledgorno = m.get('pledgorno')
        if m.get('pledgee') is not None:
            self.pledgee = m.get('pledgee')
        if m.get('pledgeeno') is not None:
            self.pledgeeno = m.get('pledgeeno')
        if m.get('pledgedamount') is not None:
            self.pledgedamount = m.get('pledgedamount')
        if m.get('regdate') is not None:
            self.regdate = m.get('regdate')
        if m.get('publicdate') is not None:
            self.publicdate = m.get('publicdate')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
