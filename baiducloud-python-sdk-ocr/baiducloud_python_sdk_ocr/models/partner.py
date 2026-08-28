"""
Partner information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Partner(AbstractModel):
    """
    Partner
    """

    def __init__(
        self,
        stockname=None,
        stocktype=None,
        stockpercent=None,
        stockcapital=None,
        shouddate=None,
        investtype=None,
        stockrealcapital=None,
        capidate=None,
        investname=None,
        concur=None,
    ):
        """
        Initialize Partner instance.

        :param stockname: 股东
        :type stockname: str (optional)

        :param stocktype: 股东类型
        :type stocktype: str (optional)

        :param stockpercent: 出资比例
        :type stockpercent: str (optional)

        :param stockcapital: 认缴出资额
        :type stockcapital: str (optional)

        :param shouddate: 认缴出资时间
        :type shouddate: str (optional)

        :param investtype: 认缴出资方式
        :type investtype: str (optional)

        :param stockrealcapital: 实缴出资额
        :type stockrealcapital: str (optional)

        :param capidate: 实缴时间
        :type capidate: str (optional)

        :param investname: 实际出资方式
        :type investname: str (optional)

        :param concur: 出资币种
        :type concur: str (optional)
        """
        super().__init__()
        self.stockname = stockname
        self.stocktype = stocktype
        self.stockpercent = stockpercent
        self.stockcapital = stockcapital
        self.shouddate = shouddate
        self.investtype = investtype
        self.stockrealcapital = stockrealcapital
        self.capidate = capidate
        self.investname = investname
        self.concur = concur

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
        if self.stockname is not None:
            result['stockname'] = self.stockname
        if self.stocktype is not None:
            result['stocktype'] = self.stocktype
        if self.stockpercent is not None:
            result['stockpercent'] = self.stockpercent
        if self.stockcapital is not None:
            result['stockcapital'] = self.stockcapital
        if self.shouddate is not None:
            result['shouddate'] = self.shouddate
        if self.investtype is not None:
            result['investtype'] = self.investtype
        if self.stockrealcapital is not None:
            result['stockrealcapital'] = self.stockrealcapital
        if self.capidate is not None:
            result['capidate'] = self.capidate
        if self.investname is not None:
            result['investname'] = self.investname
        if self.concur is not None:
            result['concur'] = self.concur
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Partner

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('stockname') is not None:
            self.stockname = m.get('stockname')
        if m.get('stocktype') is not None:
            self.stocktype = m.get('stocktype')
        if m.get('stockpercent') is not None:
            self.stockpercent = m.get('stockpercent')
        if m.get('stockcapital') is not None:
            self.stockcapital = m.get('stockcapital')
        if m.get('shouddate') is not None:
            self.shouddate = m.get('shouddate')
        if m.get('investtype') is not None:
            self.investtype = m.get('investtype')
        if m.get('stockrealcapital') is not None:
            self.stockrealcapital = m.get('stockrealcapital')
        if m.get('capidate') is not None:
            self.capidate = m.get('capidate')
        if m.get('investname') is not None:
            self.investname = m.get('investname')
        if m.get('concur') is not None:
            self.concur = m.get('concur')
        return self
