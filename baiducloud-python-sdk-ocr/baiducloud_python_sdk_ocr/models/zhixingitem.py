"""
Zhixingitem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Zhixingitem(AbstractModel):
    """
    Zhixingitem
    """

    def __init__(
        self,
        casestate=None,
        partycardnum=None,
        zxid=None,
        pname=None,
        casecreatetime=None,
        casecode=None,
        execcourtname=None,
        execmoney=None,
    ):
        """
        Initialize Zhixingitem instance.

        :param casestate: 状态
        :type casestate: str (optional)

        :param partycardnum: 身份证号码/组织机构代码
        :type partycardnum: str (optional)

        :param zxid: 官网系统ID
        :type zxid: str (optional)

        :param pname: 名称
        :type pname: str (optional)

        :param casecreatetime: 立案时间
        :type casecreatetime: str (optional)

        :param casecode: 立案号
        :type casecode: str (optional)

        :param execcourtname: 执行法院
        :type execcourtname: str (optional)

        :param execmoney: 标的
        :type execmoney: str (optional)
        """
        super().__init__()
        self.casestate = casestate
        self.partycardnum = partycardnum
        self.zxid = zxid
        self.pname = pname
        self.casecreatetime = casecreatetime
        self.casecode = casecode
        self.execcourtname = execcourtname
        self.execmoney = execmoney

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
        if self.casestate is not None:
            result['casestate'] = self.casestate
        if self.partycardnum is not None:
            result['partycardnum'] = self.partycardnum
        if self.zxid is not None:
            result['zxid'] = self.zxid
        if self.pname is not None:
            result['pname'] = self.pname
        if self.casecreatetime is not None:
            result['casecreatetime'] = self.casecreatetime
        if self.casecode is not None:
            result['casecode'] = self.casecode
        if self.execcourtname is not None:
            result['execcourtname'] = self.execcourtname
        if self.execmoney is not None:
            result['execmoney'] = self.execmoney
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Zhixingitem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('casestate') is not None:
            self.casestate = m.get('casestate')
        if m.get('partycardnum') is not None:
            self.partycardnum = m.get('partycardnum')
        if m.get('zxid') is not None:
            self.zxid = m.get('zxid')
        if m.get('pname') is not None:
            self.pname = m.get('pname')
        if m.get('casecreatetime') is not None:
            self.casecreatetime = m.get('casecreatetime')
        if m.get('casecode') is not None:
            self.casecode = m.get('casecode')
        if m.get('execcourtname') is not None:
            self.execcourtname = m.get('execcourtname')
        if m.get('execmoney') is not None:
            self.execmoney = m.get('execmoney')
        return self
