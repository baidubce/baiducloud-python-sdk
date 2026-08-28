"""
BusinesslicenseVerificationDetailedResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.base import Base

from baiducloud_python_sdk_ocr.models.branch import Branch

from baiducloud_python_sdk_ocr.models.change import Change

from baiducloud_python_sdk_ocr.models.taxcredititem import Taxcredititem

from baiducloud_python_sdk_ocr.models.contactinfo import Contactinfo

from baiducloud_python_sdk_ocr.models.employee import Employee

from baiducloud_python_sdk_ocr.models.exception_info import ExceptionInfo

from baiducloud_python_sdk_ocr.models.industry import Industry

from baiducloud_python_sdk_ocr.models.liquidation import Liquidation

from baiducloud_python_sdk_ocr.models.mpledge import Mpledge

from baiducloud_python_sdk_ocr.models.originalname import Originalname

from baiducloud_python_sdk_ocr.models.partner import Partner

from baiducloud_python_sdk_ocr.models.penalty import Penalty

from baiducloud_python_sdk_ocr.models.permission import Permission

from baiducloud_python_sdk_ocr.models.pledge import Pledge

from baiducloud_python_sdk_ocr.models.spotcheck import Spotcheck

from baiducloud_python_sdk_ocr.models.shixinitem import Shixinitem

from baiducloud_python_sdk_ocr.models.zhixingitem import Zhixingitem


class BusinesslicenseVerificationDetailedResult(AbstractModel):
    """
    BusinesslicenseVerificationDetailedResult
    """

    def __init__(
        self,
        base=None,
        branches=None,
        changes=None,
        taxcredititems=None,
        contactinfo=None,
        employees=None,
        exceptions=None,
        industry=None,
        liquidation=None,
        mpledges=None,
        originalname=None,
        partners=None,
        penalties=None,
        permissions=None,
        pledges=None,
        spotchecks=None,
        shixinitems=None,
        zhixingitems=None,
    ):
        """
        Initialize BusinesslicenseVerificationDetailedResult instance.

        :param base: base attribute
        :type base: Base (optional)

        :param branches: 分支机构，每个数组可能包含多个object
        :type branches: List[Branch] (optional)

        :param changes: 企业变更
        :type changes: List[Change] (optional)

        :param taxcredititems: 纳税信息
        :type taxcredititems: List[Taxcredititem] (optional)

        :param contactinfo: contactinfo attribute
        :type contactinfo: Contactinfo (optional)

        :param employees: 企业高管，每个数组可能包含多个object
        :type employees: List[Employee] (optional)

        :param exceptions: 经营异常
        :type exceptions: List[ExceptionInfo] (optional)

        :param industry: 行业信息
        :type industry: List[Industry] (optional)

        :param liquidation: liquidation attribute
        :type liquidation: Liquidation (optional)

        :param mpledges: 动产抵押，每个数组可能包含多个object
        :type mpledges: List[Mpledge] (optional)

        :param originalname: 曾用名，每个数组可能包含多个object
        :type originalname: List[Originalname] (optional)

        :param partners: 股东信息，每个数组可能包含多个object
        :type partners: List[Partner] (optional)

        :param penalties: 行政处罚，每个数组可能包含多个object
        :type penalties: List[Penalty] (optional)

        :param permissions: 行政许可，每个数组可能包含多个object
        :type permissions: List[Permission] (optional)

        :param pledges: 股权出质，每个数组可能包含多个object
        :type pledges: List[Pledge] (optional)

        :param spotchecks: 企业抽查检查，每个数组可能包含多个object
        :type spotchecks: List[Spotcheck] (optional)

        :param shixinitems: 失信，每个数组可能包含多个object
        :type shixinitems: List[Shixinitem] (optional)

        :param zhixingitems: 被执行，每个数组可能包含多个object
        :type zhixingitems: List[Zhixingitem] (optional)
        """
        super().__init__()
        self.base = base
        self.branches = branches
        self.changes = changes
        self.taxcredititems = taxcredititems
        self.contactinfo = contactinfo
        self.employees = employees
        self.exceptions = exceptions
        self.industry = industry
        self.liquidation = liquidation
        self.mpledges = mpledges
        self.originalname = originalname
        self.partners = partners
        self.penalties = penalties
        self.permissions = permissions
        self.pledges = pledges
        self.spotchecks = spotchecks
        self.shixinitems = shixinitems
        self.zhixingitems = zhixingitems

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
        if self.base is not None:
            result['base'] = self.base.to_dict()
        if self.branches is not None:
            result['branches'] = [i.to_dict() for i in self.branches]
        if self.changes is not None:
            result['changes'] = [i.to_dict() for i in self.changes]
        if self.taxcredititems is not None:
            result['taxcredititems'] = [i.to_dict() for i in self.taxcredititems]
        if self.contactinfo is not None:
            result['contactinfo'] = self.contactinfo.to_dict()
        if self.employees is not None:
            result['employees'] = [i.to_dict() for i in self.employees]
        if self.exceptions is not None:
            result['exceptions'] = [i.to_dict() for i in self.exceptions]
        if self.industry is not None:
            result['industry'] = [i.to_dict() for i in self.industry]
        if self.liquidation is not None:
            result['liquidation'] = self.liquidation.to_dict()
        if self.mpledges is not None:
            result['mpledges'] = [i.to_dict() for i in self.mpledges]
        if self.originalname is not None:
            result['originalname'] = [i.to_dict() for i in self.originalname]
        if self.partners is not None:
            result['partners'] = [i.to_dict() for i in self.partners]
        if self.penalties is not None:
            result['penalties'] = [i.to_dict() for i in self.penalties]
        if self.permissions is not None:
            result['permissions'] = [i.to_dict() for i in self.permissions]
        if self.pledges is not None:
            result['pledges'] = [i.to_dict() for i in self.pledges]
        if self.spotchecks is not None:
            result['spotchecks'] = [i.to_dict() for i in self.spotchecks]
        if self.shixinitems is not None:
            result['shixinitems'] = [i.to_dict() for i in self.shixinitems]
        if self.zhixingitems is not None:
            result['zhixingitems'] = [i.to_dict() for i in self.zhixingitems]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BusinesslicenseVerificationDetailedResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('base') is not None:
            self.base = Base().from_dict(m.get('base'))
        if m.get('branches') is not None:
            self.branches = [Branch().from_dict(i) for i in m.get('branches')]
        if m.get('changes') is not None:
            self.changes = [Change().from_dict(i) for i in m.get('changes')]
        if m.get('taxcredititems') is not None:
            self.taxcredititems = [Taxcredititem().from_dict(i) for i in m.get('taxcredititems')]
        if m.get('contactinfo') is not None:
            self.contactinfo = Contactinfo().from_dict(m.get('contactinfo'))
        if m.get('employees') is not None:
            self.employees = [Employee().from_dict(i) for i in m.get('employees')]
        if m.get('exceptions') is not None:
            self.exceptions = [ExceptionInfo().from_dict(i) for i in m.get('exceptions')]
        if m.get('industry') is not None:
            self.industry = [Industry().from_dict(i) for i in m.get('industry')]
        if m.get('liquidation') is not None:
            self.liquidation = Liquidation().from_dict(m.get('liquidation'))
        if m.get('mpledges') is not None:
            self.mpledges = [Mpledge().from_dict(i) for i in m.get('mpledges')]
        if m.get('originalname') is not None:
            self.originalname = [Originalname().from_dict(i) for i in m.get('originalname')]
        if m.get('partners') is not None:
            self.partners = [Partner().from_dict(i) for i in m.get('partners')]
        if m.get('penalties') is not None:
            self.penalties = [Penalty().from_dict(i) for i in m.get('penalties')]
        if m.get('permissions') is not None:
            self.permissions = [Permission().from_dict(i) for i in m.get('permissions')]
        if m.get('pledges') is not None:
            self.pledges = [Pledge().from_dict(i) for i in m.get('pledges')]
        if m.get('spotchecks') is not None:
            self.spotchecks = [Spotcheck().from_dict(i) for i in m.get('spotchecks')]
        if m.get('shixinitems') is not None:
            self.shixinitems = [Shixinitem().from_dict(i) for i in m.get('shixinitems')]
        if m.get('zhixingitems') is not None:
            self.zhixingitems = [Zhixingitem().from_dict(i) for i in m.get('zhixingitems')]
        return self
