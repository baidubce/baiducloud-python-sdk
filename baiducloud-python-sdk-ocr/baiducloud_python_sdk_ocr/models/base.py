"""
Base information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Base(AbstractModel):
    """
    Base
    """

    def __init__(
        self,
        legalperson=None,
        establishdate=None,
        revokedate=None,
        companystatus=None,
        province=None,
        creditno=None,
        capital=None,
        companytype=None,
        companyaddress=None,
        businessscope=None,
        businessdatefrom=None,
        businessdateto=None,
        issuedate=None,
        orgcode=None,
        isonstock=None,
        stocknumber=None,
        stocktype=None,
        keyno=None,
        companyname=None,
        companycode=None,
        authority=None,
        regcapcur=None,
    ):
        """
        Initialize Base instance.

        :param legalperson: 法人名
        :type legalperson: str (optional)

        :param establishdate: 成立日期
        :type establishdate: str (optional)

        :param revokedate: 吊销日期
        :type revokedate: str (optional)

        :param companystatus: 企业状态
        :type companystatus: str (optional)

        :param province: 省份
        :type province: str (optional)

        :param creditno: 统一社会信用代码
        :type creditno: str (optional)

        :param capital: 注册资本
        :type capital: str (optional)

        :param companytype: 企业类型
        :type companytype: str (optional)

        :param companyaddress: 地址
        :type companyaddress: str (optional)

        :param businessscope: 经营范围
        :type businessscope: str (optional)

        :param businessdatefrom: 营业开始日期
        :type businessdatefrom: str (optional)

        :param businessdateto: 营业结束日期
        :type businessdateto: str (optional)

        :param issuedate: 发照日期
        :type issuedate: str (optional)

        :param orgcode: 组织机构代码
        :type orgcode: str (optional)

        :param isonstock: 是否上市 (0为未上市，1为上市）
        :type isonstock: str (optional)

        :param stocknumber: 上市公司代码
        :type stocknumber: str (optional)

        :param stocktype: 上市类型
        :type stocktype: str (optional)

        :param keyno: 内部keyno
        :type keyno: str (optional)

        :param companyname: 企业名称
        :type companyname: str (optional)

        :param companycode: 注册号
        :type companycode: str (optional)

        :param authority: 登记机关
        :type authority: str (optional)

        :param regcapcur: 注册资本币种
        :type regcapcur: str (optional)
        """
        super().__init__()
        self.legalperson = legalperson
        self.establishdate = establishdate
        self.revokedate = revokedate
        self.companystatus = companystatus
        self.province = province
        self.creditno = creditno
        self.capital = capital
        self.companytype = companytype
        self.companyaddress = companyaddress
        self.businessscope = businessscope
        self.businessdatefrom = businessdatefrom
        self.businessdateto = businessdateto
        self.issuedate = issuedate
        self.orgcode = orgcode
        self.isonstock = isonstock
        self.stocknumber = stocknumber
        self.stocktype = stocktype
        self.keyno = keyno
        self.companyname = companyname
        self.companycode = companycode
        self.authority = authority
        self.regcapcur = regcapcur

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
        if self.legalperson is not None:
            result['legalperson'] = self.legalperson
        if self.establishdate is not None:
            result['establishdate'] = self.establishdate
        if self.revokedate is not None:
            result['revokedate'] = self.revokedate
        if self.companystatus is not None:
            result['companystatus'] = self.companystatus
        if self.province is not None:
            result['province'] = self.province
        if self.creditno is not None:
            result['creditno'] = self.creditno
        if self.capital is not None:
            result['capital'] = self.capital
        if self.companytype is not None:
            result['companytype'] = self.companytype
        if self.companyaddress is not None:
            result['companyaddress'] = self.companyaddress
        if self.businessscope is not None:
            result['businessscope'] = self.businessscope
        if self.businessdatefrom is not None:
            result['businessdatefrom'] = self.businessdatefrom
        if self.businessdateto is not None:
            result['businessdateto'] = self.businessdateto
        if self.issuedate is not None:
            result['issuedate'] = self.issuedate
        if self.orgcode is not None:
            result['orgcode'] = self.orgcode
        if self.isonstock is not None:
            result['isonstock'] = self.isonstock
        if self.stocknumber is not None:
            result['stocknumber'] = self.stocknumber
        if self.stocktype is not None:
            result['stocktype'] = self.stocktype
        if self.keyno is not None:
            result['keyno'] = self.keyno
        if self.companyname is not None:
            result['companyname'] = self.companyname
        if self.companycode is not None:
            result['companycode'] = self.companycode
        if self.authority is not None:
            result['authority'] = self.authority
        if self.regcapcur is not None:
            result['regcapcur'] = self.regcapcur
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Base

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('legalperson') is not None:
            self.legalperson = m.get('legalperson')
        if m.get('establishdate') is not None:
            self.establishdate = m.get('establishdate')
        if m.get('revokedate') is not None:
            self.revokedate = m.get('revokedate')
        if m.get('companystatus') is not None:
            self.companystatus = m.get('companystatus')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('creditno') is not None:
            self.creditno = m.get('creditno')
        if m.get('capital') is not None:
            self.capital = m.get('capital')
        if m.get('companytype') is not None:
            self.companytype = m.get('companytype')
        if m.get('companyaddress') is not None:
            self.companyaddress = m.get('companyaddress')
        if m.get('businessscope') is not None:
            self.businessscope = m.get('businessscope')
        if m.get('businessdatefrom') is not None:
            self.businessdatefrom = m.get('businessdatefrom')
        if m.get('businessdateto') is not None:
            self.businessdateto = m.get('businessdateto')
        if m.get('issuedate') is not None:
            self.issuedate = m.get('issuedate')
        if m.get('orgcode') is not None:
            self.orgcode = m.get('orgcode')
        if m.get('isonstock') is not None:
            self.isonstock = m.get('isonstock')
        if m.get('stocknumber') is not None:
            self.stocknumber = m.get('stocknumber')
        if m.get('stocktype') is not None:
            self.stocktype = m.get('stocktype')
        if m.get('keyno') is not None:
            self.keyno = m.get('keyno')
        if m.get('companyname') is not None:
            self.companyname = m.get('companyname')
        if m.get('companycode') is not None:
            self.companycode = m.get('companycode')
        if m.get('authority') is not None:
            self.authority = m.get('authority')
        if m.get('regcapcur') is not None:
            self.regcapcur = m.get('regcapcur')
        return self
