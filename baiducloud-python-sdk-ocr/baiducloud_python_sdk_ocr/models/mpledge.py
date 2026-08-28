"""
Mpledge information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Mpledge(AbstractModel):
    """
    Mpledge
    """

    def __init__(
        self,
        registerno=None,
        registerdate=None,
        publicdate=None,
        registeroffice=None,
        debtsecuredamount=None,
        status=None,
    ):
        """
        Initialize Mpledge instance.

        :param registerno: 登记编号
        :type registerno: str (optional)

        :param registerdate: 登记时间
        :type registerdate: str (optional)

        :param publicdate: 公示时间
        :type publicdate: str (optional)

        :param registeroffice: 登记机关
        :type registeroffice: str (optional)

        :param debtsecuredamount: 被担保债权数额
        :type debtsecuredamount: str (optional)

        :param status: 状态
        :type status: str (optional)
        """
        super().__init__()
        self.registerno = registerno
        self.registerdate = registerdate
        self.publicdate = publicdate
        self.registeroffice = registeroffice
        self.debtsecuredamount = debtsecuredamount
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
        if self.registerno is not None:
            result['registerno'] = self.registerno
        if self.registerdate is not None:
            result['registerdate'] = self.registerdate
        if self.publicdate is not None:
            result['publicdate'] = self.publicdate
        if self.registeroffice is not None:
            result['registeroffice'] = self.registeroffice
        if self.debtsecuredamount is not None:
            result['debtsecuredamount'] = self.debtsecuredamount
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
        :rtype: Mpledge

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('registerno') is not None:
            self.registerno = m.get('registerno')
        if m.get('registerdate') is not None:
            self.registerdate = m.get('registerdate')
        if m.get('publicdate') is not None:
            self.publicdate = m.get('publicdate')
        if m.get('registeroffice') is not None:
            self.registeroffice = m.get('registeroffice')
        if m.get('debtsecuredamount') is not None:
            self.debtsecuredamount = m.get('debtsecuredamount')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
