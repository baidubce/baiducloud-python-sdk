"""
Shixinitem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Shixinitem(AbstractModel):
    """
    Shixinitem
    """

    def __init__(
        self,
        iname=None,
        regdate=None,
        casecode=None,
        cardnum=None,
        gistcid=None,
        publishdate=None,
        performance=None,
        disreputtypename=None,
        courtname=None,
    ):
        """
        Initialize Shixinitem instance.

        :param iname: 公司名称
        :type iname: str (optional)

        :param regdate: 立案日期
        :type regdate: str (optional)

        :param casecode: 立案文书号
        :type casecode: str (optional)

        :param cardnum: 组织机构代码
        :type cardnum: str (optional)

        :param gistcid: 执行依据文号
        :type gistcid: str (optional)

        :param publishdate: 发布时间
        :type publishdate: str (optional)

        :param performance: 被执行人的履约情况
        :type performance: str (optional)

        :param disreputtypename: 行为备注
        :type disreputtypename: str (optional)

        :param courtname: 执行法院
        :type courtname: str (optional)
        """
        super().__init__()
        self.iname = iname
        self.regdate = regdate
        self.casecode = casecode
        self.cardnum = cardnum
        self.gistcid = gistcid
        self.publishdate = publishdate
        self.performance = performance
        self.disreputtypename = disreputtypename
        self.courtname = courtname

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
        if self.iname is not None:
            result['iname'] = self.iname
        if self.regdate is not None:
            result['regdate'] = self.regdate
        if self.casecode is not None:
            result['casecode'] = self.casecode
        if self.cardnum is not None:
            result['cardnum'] = self.cardnum
        if self.gistcid is not None:
            result['gistcid'] = self.gistcid
        if self.publishdate is not None:
            result['publishdate'] = self.publishdate
        if self.performance is not None:
            result['performance'] = self.performance
        if self.disreputtypename is not None:
            result['disreputtypename'] = self.disreputtypename
        if self.courtname is not None:
            result['courtname'] = self.courtname
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Shixinitem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('iname') is not None:
            self.iname = m.get('iname')
        if m.get('regdate') is not None:
            self.regdate = m.get('regdate')
        if m.get('casecode') is not None:
            self.casecode = m.get('casecode')
        if m.get('cardnum') is not None:
            self.cardnum = m.get('cardnum')
        if m.get('gistcid') is not None:
            self.gistcid = m.get('gistcid')
        if m.get('publishdate') is not None:
            self.publishdate = m.get('publishdate')
        if m.get('performance') is not None:
            self.performance = m.get('performance')
        if m.get('disreputtypename') is not None:
            self.disreputtypename = m.get('disreputtypename')
        if m.get('courtname') is not None:
            self.courtname = m.get('courtname')
        return self
