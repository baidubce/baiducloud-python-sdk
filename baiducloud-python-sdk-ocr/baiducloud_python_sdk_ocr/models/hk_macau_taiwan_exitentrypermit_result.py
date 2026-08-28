"""
HkMacauTaiwanExitentrypermitResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_field import HkMacauTaiwanExitentrypermitField


class HkMacauTaiwanExitentrypermitResult(AbstractModel):
    """
    HkMacauTaiwanExitentrypermitResult
    """

    def __init__(
        self,
        card_number=None,
        name_chn=None,
        name_eng=None,
        birthday=None,
        sex=None,
        valid_date=None,
        issue_authority=None,
        issue_place=None,
        mrz_code=None,
        hk_type=None,
        hk_valid_date=None,
        hk_remarks=None,
        hk_round_trip_number=None,
        mc_type=None,
        mc_valid_date=None,
        mc_remarks=None,
        mc_round_trip_number=None,
        type=None,
        remarks=None,
        round_trip_number=None,
        issue_times=None,
        idcard_name=None,
        idcard_number=None,
        mrz_code1=None,
        mrz_code2=None,
    ):
        """
        Initialize HkMacauTaiwanExitentrypermitResult instance.

        :param card_number: 证件号码
        :type card_number: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param name_chn: 姓名
        :type name_chn: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param name_eng: 姓名（英文）
        :type name_eng: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param birthday: 出生日期
        :type birthday: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param sex: 性别
        :type sex: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param valid_date: 有效期限
        :type valid_date: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param issue_authority: 签发机关
        :type issue_authority: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param issue_place: 签发地点
        :type issue_place: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param mrz_code: 证件下方第一行
        :type mrz_code: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param hk_type: 来往香港签注-种类
        :type hk_type: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param hk_valid_date: 来往香港签注-有效期
        :type hk_valid_date: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param hk_remarks: 来往香港签注-备注
        :type hk_remarks: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param hk_round_trip_number: 来往香港签注-往返有效
        :type hk_round_trip_number: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param mc_type: 来往澳门签注-种类
        :type mc_type: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param mc_valid_date: 来往澳门签注-有效期
        :type mc_valid_date: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param mc_remarks: 来往澳门签注-备注
        :type mc_remarks: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param mc_round_trip_number: 来往澳门签注-往返有效
        :type mc_round_trip_number: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param type: 种类
        :type type: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param remarks: 备注
        :type remarks: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param round_trip_number: 往返有效
        :type round_trip_number: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param issue_times: 签发次数
        :type issue_times: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param idcard_name: 身份证姓名
        :type idcard_name: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param idcard_number: 身份证号码
        :type idcard_number: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param mrz_code1: 证件下方第一行
        :type mrz_code1: List[HkMacauTaiwanExitentrypermitField] (optional)

        :param mrz_code2: 证件下方第二行
        :type mrz_code2: List[HkMacauTaiwanExitentrypermitField] (optional)
        """
        super().__init__()
        self.card_number = card_number
        self.name_chn = name_chn
        self.name_eng = name_eng
        self.birthday = birthday
        self.sex = sex
        self.valid_date = valid_date
        self.issue_authority = issue_authority
        self.issue_place = issue_place
        self.mrz_code = mrz_code
        self.hk_type = hk_type
        self.hk_valid_date = hk_valid_date
        self.hk_remarks = hk_remarks
        self.hk_round_trip_number = hk_round_trip_number
        self.mc_type = mc_type
        self.mc_valid_date = mc_valid_date
        self.mc_remarks = mc_remarks
        self.mc_round_trip_number = mc_round_trip_number
        self.type = type
        self.remarks = remarks
        self.round_trip_number = round_trip_number
        self.issue_times = issue_times
        self.idcard_name = idcard_name
        self.idcard_number = idcard_number
        self.mrz_code1 = mrz_code1
        self.mrz_code2 = mrz_code2

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
        if self.card_number is not None:
            result['card_number'] = [i.to_dict() for i in self.card_number]
        if self.name_chn is not None:
            result['name_chn'] = [i.to_dict() for i in self.name_chn]
        if self.name_eng is not None:
            result['name_eng'] = [i.to_dict() for i in self.name_eng]
        if self.birthday is not None:
            result['birthday'] = [i.to_dict() for i in self.birthday]
        if self.sex is not None:
            result['sex'] = [i.to_dict() for i in self.sex]
        if self.valid_date is not None:
            result['valid_date'] = [i.to_dict() for i in self.valid_date]
        if self.issue_authority is not None:
            result['issue_authority'] = [i.to_dict() for i in self.issue_authority]
        if self.issue_place is not None:
            result['issue_place'] = [i.to_dict() for i in self.issue_place]
        if self.mrz_code is not None:
            result['MRZCode'] = [i.to_dict() for i in self.mrz_code]
        if self.hk_type is not None:
            result['hk_type'] = [i.to_dict() for i in self.hk_type]
        if self.hk_valid_date is not None:
            result['hk_valid_date'] = [i.to_dict() for i in self.hk_valid_date]
        if self.hk_remarks is not None:
            result['hk_remarks'] = [i.to_dict() for i in self.hk_remarks]
        if self.hk_round_trip_number is not None:
            result['hk_round_trip_number'] = [i.to_dict() for i in self.hk_round_trip_number]
        if self.mc_type is not None:
            result['mc_type'] = [i.to_dict() for i in self.mc_type]
        if self.mc_valid_date is not None:
            result['mc_valid_date'] = [i.to_dict() for i in self.mc_valid_date]
        if self.mc_remarks is not None:
            result['mc_remarks'] = [i.to_dict() for i in self.mc_remarks]
        if self.mc_round_trip_number is not None:
            result['mc_round_trip_number'] = [i.to_dict() for i in self.mc_round_trip_number]
        if self.type is not None:
            result['type'] = [i.to_dict() for i in self.type]
        if self.remarks is not None:
            result['remarks'] = [i.to_dict() for i in self.remarks]
        if self.round_trip_number is not None:
            result['round_trip_number'] = [i.to_dict() for i in self.round_trip_number]
        if self.issue_times is not None:
            result['issue_times'] = [i.to_dict() for i in self.issue_times]
        if self.idcard_name is not None:
            result['idcard_name'] = [i.to_dict() for i in self.idcard_name]
        if self.idcard_number is not None:
            result['idcard_number'] = [i.to_dict() for i in self.idcard_number]
        if self.mrz_code1 is not None:
            result['MRZCode1'] = [i.to_dict() for i in self.mrz_code1]
        if self.mrz_code2 is not None:
            result['MRZCode2'] = [i.to_dict() for i in self.mrz_code2]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HkMacauTaiwanExitentrypermitResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('card_number') is not None:
            self.card_number = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('card_number')]
        if m.get('name_chn') is not None:
            self.name_chn = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('name_chn')]
        if m.get('name_eng') is not None:
            self.name_eng = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('name_eng')]
        if m.get('birthday') is not None:
            self.birthday = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('birthday')]
        if m.get('sex') is not None:
            self.sex = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('sex')]
        if m.get('valid_date') is not None:
            self.valid_date = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('valid_date')]
        if m.get('issue_authority') is not None:
            self.issue_authority = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('issue_authority')]
        if m.get('issue_place') is not None:
            self.issue_place = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('issue_place')]
        if m.get('MRZCode') is not None:
            self.mrz_code = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('MRZCode')]
        if m.get('hk_type') is not None:
            self.hk_type = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('hk_type')]
        if m.get('hk_valid_date') is not None:
            self.hk_valid_date = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('hk_valid_date')]
        if m.get('hk_remarks') is not None:
            self.hk_remarks = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('hk_remarks')]
        if m.get('hk_round_trip_number') is not None:
            self.hk_round_trip_number = [
                HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('hk_round_trip_number')
            ]
        if m.get('mc_type') is not None:
            self.mc_type = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('mc_type')]
        if m.get('mc_valid_date') is not None:
            self.mc_valid_date = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('mc_valid_date')]
        if m.get('mc_remarks') is not None:
            self.mc_remarks = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('mc_remarks')]
        if m.get('mc_round_trip_number') is not None:
            self.mc_round_trip_number = [
                HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('mc_round_trip_number')
            ]
        if m.get('type') is not None:
            self.type = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('type')]
        if m.get('remarks') is not None:
            self.remarks = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('remarks')]
        if m.get('round_trip_number') is not None:
            self.round_trip_number = [
                HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('round_trip_number')
            ]
        if m.get('issue_times') is not None:
            self.issue_times = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('issue_times')]
        if m.get('idcard_name') is not None:
            self.idcard_name = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('idcard_name')]
        if m.get('idcard_number') is not None:
            self.idcard_number = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('idcard_number')]
        if m.get('MRZCode1') is not None:
            self.mrz_code1 = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('MRZCode1')]
        if m.get('MRZCode2') is not None:
            self.mrz_code2 = [HkMacauTaiwanExitentrypermitField().from_dict(i) for i in m.get('MRZCode2')]
        return self
