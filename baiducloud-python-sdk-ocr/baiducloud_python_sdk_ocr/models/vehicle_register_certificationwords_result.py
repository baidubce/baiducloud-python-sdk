"""
VehicleRegisterCertificationwordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)

from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_words_item import (
    VehicleRegistrationCertificateWordsItem,
)


class VehicleRegisterCertificationwordsResult(AbstractModel):
    """
    VehicleRegisterCertificationwordsResult
    """

    def __init__(
        self,
        number=None,
        name_idcard_no=None,
        registration_authority=None,
        registration_date=None,
        registration_num=None,
        vehicle_model=None,
        vehicle_type=None,
        vin=None,
        engine_num=None,
        seating_capacity=None,
        body_color=None,
        nature_of_use=None,
        date_of_production=None,
        date_of_issue=None,
        seal_of_issue_authority=None,
    ):
        """
        Initialize VehicleRegisterCertificationwordsResult instance.

        :param number: number attribute
        :type number: VehicleRegistrationCertificateWordsItem (optional)

        :param name_idcard_no: name_idcard_no attribute
        :type name_idcard_no: VehicleRegistrationCertificateWordsItem (optional)

        :param registration_authority: registration_authority attribute
        :type registration_authority: VehicleRegistrationCertificateWordsItem (optional)

        :param registration_date: registration_date attribute
        :type registration_date: VehicleRegistrationCertificateWordsItem (optional)

        :param registration_num: registration_num attribute
        :type registration_num: VehicleRegistrationCertificateWordsItem (optional)

        :param vehicle_model: vehicle_model attribute
        :type vehicle_model: VehicleRegistrationCertificateWordsItem (optional)

        :param vehicle_type: vehicle_type attribute
        :type vehicle_type: VehicleRegistrationCertificateWordsItem (optional)

        :param vin: vin attribute
        :type vin: VehicleRegistrationCertificateWordsItem (optional)

        :param engine_num: engine_num attribute
        :type engine_num: VehicleRegistrationCertificateWordsItem (optional)

        :param seating_capacity: seating_capacity attribute
        :type seating_capacity: VehicleRegistrationCertificateWordsItem (optional)

        :param body_color: body_color attribute
        :type body_color: VehicleRegistrationCertificateWordsItem (optional)

        :param nature_of_use: nature_of_use attribute
        :type nature_of_use: VehicleRegistrationCertificateWordsItem (optional)

        :param date_of_production: date_of_production attribute
        :type date_of_production: VehicleRegistrationCertificateWordsItem (optional)

        :param date_of_issue: date_of_issue attribute
        :type date_of_issue: VehicleRegistrationCertificateWordsItem (optional)

        :param seal_of_issue_authority: seal_of_issue_authority attribute
        :type seal_of_issue_authority: VehicleRegistrationCertificateWordsItem (optional)
        """
        super().__init__()
        self.number = number
        self.name_idcard_no = name_idcard_no
        self.registration_authority = registration_authority
        self.registration_date = registration_date
        self.registration_num = registration_num
        self.vehicle_model = vehicle_model
        self.vehicle_type = vehicle_type
        self.vin = vin
        self.engine_num = engine_num
        self.seating_capacity = seating_capacity
        self.body_color = body_color
        self.nature_of_use = nature_of_use
        self.date_of_production = date_of_production
        self.date_of_issue = date_of_issue
        self.seal_of_issue_authority = seal_of_issue_authority

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
        if self.number is not None:
            result['number'] = self.number.to_dict()
        if self.name_idcard_no is not None:
            result['name_idcard_no'] = self.name_idcard_no.to_dict()
        if self.registration_authority is not None:
            result['registration_authority'] = self.registration_authority.to_dict()
        if self.registration_date is not None:
            result['registration_date'] = self.registration_date.to_dict()
        if self.registration_num is not None:
            result['registration_num'] = self.registration_num.to_dict()
        if self.vehicle_model is not None:
            result['vehicle_model'] = self.vehicle_model.to_dict()
        if self.vehicle_type is not None:
            result['vehicle_type'] = self.vehicle_type.to_dict()
        if self.vin is not None:
            result['vin'] = self.vin.to_dict()
        if self.engine_num is not None:
            result['engine_num'] = self.engine_num.to_dict()
        if self.seating_capacity is not None:
            result['seating_capacity'] = self.seating_capacity.to_dict()
        if self.body_color is not None:
            result['body_color'] = self.body_color.to_dict()
        if self.nature_of_use is not None:
            result['nature_of_use'] = self.nature_of_use.to_dict()
        if self.date_of_production is not None:
            result['date_of_production'] = self.date_of_production.to_dict()
        if self.date_of_issue is not None:
            result['date_of_issue'] = self.date_of_issue.to_dict()
        if self.seal_of_issue_authority is not None:
            result['seal_of_issue_authority'] = self.seal_of_issue_authority.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VehicleRegisterCertificationwordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('number') is not None:
            self.number = VehicleRegistrationCertificateWordsItem().from_dict(m.get('number'))
        if m.get('name_idcard_no') is not None:
            self.name_idcard_no = VehicleRegistrationCertificateWordsItem().from_dict(m.get('name_idcard_no'))
        if m.get('registration_authority') is not None:
            self.registration_authority = VehicleRegistrationCertificateWordsItem().from_dict(
                m.get('registration_authority')
            )
        if m.get('registration_date') is not None:
            self.registration_date = VehicleRegistrationCertificateWordsItem().from_dict(m.get('registration_date'))
        if m.get('registration_num') is not None:
            self.registration_num = VehicleRegistrationCertificateWordsItem().from_dict(m.get('registration_num'))
        if m.get('vehicle_model') is not None:
            self.vehicle_model = VehicleRegistrationCertificateWordsItem().from_dict(m.get('vehicle_model'))
        if m.get('vehicle_type') is not None:
            self.vehicle_type = VehicleRegistrationCertificateWordsItem().from_dict(m.get('vehicle_type'))
        if m.get('vin') is not None:
            self.vin = VehicleRegistrationCertificateWordsItem().from_dict(m.get('vin'))
        if m.get('engine_num') is not None:
            self.engine_num = VehicleRegistrationCertificateWordsItem().from_dict(m.get('engine_num'))
        if m.get('seating_capacity') is not None:
            self.seating_capacity = VehicleRegistrationCertificateWordsItem().from_dict(m.get('seating_capacity'))
        if m.get('body_color') is not None:
            self.body_color = VehicleRegistrationCertificateWordsItem().from_dict(m.get('body_color'))
        if m.get('nature_of_use') is not None:
            self.nature_of_use = VehicleRegistrationCertificateWordsItem().from_dict(m.get('nature_of_use'))
        if m.get('date_of_production') is not None:
            self.date_of_production = VehicleRegistrationCertificateWordsItem().from_dict(m.get('date_of_production'))
        if m.get('date_of_issue') is not None:
            self.date_of_issue = VehicleRegistrationCertificateWordsItem().from_dict(m.get('date_of_issue'))
        if m.get('seal_of_issue_authority') is not None:
            self.seal_of_issue_authority = VehicleRegistrationCertificateWordsItem().from_dict(
                m.get('seal_of_issue_authority')
            )
        return self
