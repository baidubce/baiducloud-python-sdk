"""
BusinesslicenseVerificationStandardResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BusinesslicenseVerificationStandardResult(AbstractModel):
    """
    BusinesslicenseVerificationStandardResult
    """

    def __init__(
        self,
        companyname=None,
        companytype=None,
        legalperson=None,
        capital=None,
        companycode=None,
        companyaddress=None,
        businessscope=None,
        authority=None,
        companystatus=None,
        establishdate=None,
        creditno=None,
        operationstartdate=None,
        operationenddate=None,
        issuedate=None,
        province=None,
        provincecode=None,
        city=None,
        citycode=None,
        district=None,
        districtcode=None,
        regcapcur=None,
        orgcode=None,
        licensedbusinessscope=None,
        companyenglishname=None,
        onceusedname=None,
        orgcompanycode=None,
        paidincapital=None,
        revokedate=None,
        logoffdate=None,
    ):
        """
        Initialize BusinesslicenseVerificationStandardResult instance.

        :param companyname: 企业名称
        :type companyname: str (optional)

        :param companytype: 企业类型
        :type companytype: str (optional)

        :param legalperson: 法定代表人
        :type legalperson: str (optional)

        :param capital: 注册资本
        :type capital: str (optional)

        :param companycode: 注册码
        :type companycode: str (optional)

        :param companyaddress: 企业地址
        :type companyaddress: str (optional)

        :param businessscope: 经营范围
        :type businessscope: str (optional)

        :param authority: 登记机关
        :type authority: str (optional)

        :param companystatus: 登记状态
        :type companystatus: str (optional)

        :param establishdate: 成立时间
        :type establishdate: str (optional)

        :param creditno: 统一社会信用代码
        :type creditno: str (optional)

        :param operationstartdate: 营业日期
        :type operationstartdate: str (optional)

        :param operationenddate: 截止日期
        :type operationenddate: str (optional)

        :param issuedate: 核准时间
        :type issuedate: str (optional)

        :param province: 所在省份
        :type province: str (optional)

        :param provincecode: 所在省份-行政区号
        :type provincecode: str (optional)

        :param city: 所在市
        :type city: str (optional)

        :param citycode: 所在市-行政区号
        :type citycode: str (optional)

        :param district: 所在地区
        :type district: str (optional)

        :param districtcode: 所在地区-行政区号
        :type districtcode: str (optional)

        :param regcapcur: 注册资本币种
        :type regcapcur: str (optional)

        :param orgcode: 组织机构代码
        :type orgcode: str (optional)

        :param licensedbusinessscope: 许可经营范围
        :type licensedbusinessscope: str (optional)

        :param companyenglishname: 企业英文名称
        :type companyenglishname: str (optional)

        :param onceusedname: 企业曾用名
        :type onceusedname: List[str] (optional)

        :param orgcompanycode: 原注册号
        :type orgcompanycode: str (optional)

        :param paidincapital: 实收资本
        :type paidincapital: str (optional)

        :param revokedate: 吊销日期
        :type revokedate: str (optional)

        :param logoffdate: 注销日期
        :type logoffdate: str (optional)
        """
        super().__init__()
        self.companyname = companyname
        self.companytype = companytype
        self.legalperson = legalperson
        self.capital = capital
        self.companycode = companycode
        self.companyaddress = companyaddress
        self.businessscope = businessscope
        self.authority = authority
        self.companystatus = companystatus
        self.establishdate = establishdate
        self.creditno = creditno
        self.operationstartdate = operationstartdate
        self.operationenddate = operationenddate
        self.issuedate = issuedate
        self.province = province
        self.provincecode = provincecode
        self.city = city
        self.citycode = citycode
        self.district = district
        self.districtcode = districtcode
        self.regcapcur = regcapcur
        self.orgcode = orgcode
        self.licensedbusinessscope = licensedbusinessscope
        self.companyenglishname = companyenglishname
        self.onceusedname = onceusedname
        self.orgcompanycode = orgcompanycode
        self.paidincapital = paidincapital
        self.revokedate = revokedate
        self.logoffdate = logoffdate

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
        if self.companyname is not None:
            result['companyname'] = self.companyname
        if self.companytype is not None:
            result['companytype'] = self.companytype
        if self.legalperson is not None:
            result['legalperson'] = self.legalperson
        if self.capital is not None:
            result['capital'] = self.capital
        if self.companycode is not None:
            result['companycode'] = self.companycode
        if self.companyaddress is not None:
            result['companyaddress'] = self.companyaddress
        if self.businessscope is not None:
            result['businessscope'] = self.businessscope
        if self.authority is not None:
            result['authority'] = self.authority
        if self.companystatus is not None:
            result['companystatus'] = self.companystatus
        if self.establishdate is not None:
            result['establishdate'] = self.establishdate
        if self.creditno is not None:
            result['creditno'] = self.creditno
        if self.operationstartdate is not None:
            result['operationstartdate'] = self.operationstartdate
        if self.operationenddate is not None:
            result['operationenddate'] = self.operationenddate
        if self.issuedate is not None:
            result['issuedate'] = self.issuedate
        if self.province is not None:
            result['province'] = self.province
        if self.provincecode is not None:
            result['provincecode'] = self.provincecode
        if self.city is not None:
            result['city'] = self.city
        if self.citycode is not None:
            result['citycode'] = self.citycode
        if self.district is not None:
            result['district'] = self.district
        if self.districtcode is not None:
            result['districtcode'] = self.districtcode
        if self.regcapcur is not None:
            result['regcapcur'] = self.regcapcur
        if self.orgcode is not None:
            result['orgcode'] = self.orgcode
        if self.licensedbusinessscope is not None:
            result['licensedbusinessscope'] = self.licensedbusinessscope
        if self.companyenglishname is not None:
            result['companyenglishname'] = self.companyenglishname
        if self.onceusedname is not None:
            result['onceusedname'] = self.onceusedname
        if self.orgcompanycode is not None:
            result['orgcompanycode'] = self.orgcompanycode
        if self.paidincapital is not None:
            result['paidincapital'] = self.paidincapital
        if self.revokedate is not None:
            result['revokedate'] = self.revokedate
        if self.logoffdate is not None:
            result['logoffdate'] = self.logoffdate
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BusinesslicenseVerificationStandardResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('companyname') is not None:
            self.companyname = m.get('companyname')
        if m.get('companytype') is not None:
            self.companytype = m.get('companytype')
        if m.get('legalperson') is not None:
            self.legalperson = m.get('legalperson')
        if m.get('capital') is not None:
            self.capital = m.get('capital')
        if m.get('companycode') is not None:
            self.companycode = m.get('companycode')
        if m.get('companyaddress') is not None:
            self.companyaddress = m.get('companyaddress')
        if m.get('businessscope') is not None:
            self.businessscope = m.get('businessscope')
        if m.get('authority') is not None:
            self.authority = m.get('authority')
        if m.get('companystatus') is not None:
            self.companystatus = m.get('companystatus')
        if m.get('establishdate') is not None:
            self.establishdate = m.get('establishdate')
        if m.get('creditno') is not None:
            self.creditno = m.get('creditno')
        if m.get('operationstartdate') is not None:
            self.operationstartdate = m.get('operationstartdate')
        if m.get('operationenddate') is not None:
            self.operationenddate = m.get('operationenddate')
        if m.get('issuedate') is not None:
            self.issuedate = m.get('issuedate')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('provincecode') is not None:
            self.provincecode = m.get('provincecode')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('citycode') is not None:
            self.citycode = m.get('citycode')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('districtcode') is not None:
            self.districtcode = m.get('districtcode')
        if m.get('regcapcur') is not None:
            self.regcapcur = m.get('regcapcur')
        if m.get('orgcode') is not None:
            self.orgcode = m.get('orgcode')
        if m.get('licensedbusinessscope') is not None:
            self.licensedbusinessscope = m.get('licensedbusinessscope')
        if m.get('companyenglishname') is not None:
            self.companyenglishname = m.get('companyenglishname')
        if m.get('onceusedname') is not None:
            self.onceusedname = m.get('onceusedname')
        if m.get('orgcompanycode') is not None:
            self.orgcompanycode = m.get('orgcompanycode')
        if m.get('paidincapital') is not None:
            self.paidincapital = m.get('paidincapital')
        if m.get('revokedate') is not None:
            self.revokedate = m.get('revokedate')
        if m.get('logoffdate') is not None:
            self.logoffdate = m.get('logoffdate')
        return self
