"""
Example for ocr client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_ocr.models.account_opening_response import AccountOpeningResponse
from baiducloud_python_sdk_ocr.models.accurate_response import AccurateResponse
from baiducloud_python_sdk_ocr.models.accurate_basic_response import AccurateBasicResponse
from baiducloud_python_sdk_ocr.models.air_ticket_response import AirTicketResponse
from baiducloud_python_sdk_ocr.models.bank_receipt_new_response import BankReceiptNewResponse
from baiducloud_python_sdk_ocr.models.bankcard_response import BankcardResponse
from baiducloud_python_sdk_ocr.models.birth_certificate_response import BirthCertificateResponse
from baiducloud_python_sdk_ocr.models.bus_ticket_response import BusTicketResponse
from baiducloud_python_sdk_ocr.models.business_license_response import BusinessLicenseResponse
from baiducloud_python_sdk_ocr.models.businesslicense_detailed_response import BusinesslicenseDetailedResponse
from baiducloud_python_sdk_ocr.models.businesslicense_standard_response import BusinesslicenseStandardResponse
from baiducloud_python_sdk_ocr.models.businesslicense_verification_detailed_response import (
    BusinesslicenseVerificationDetailedResponse,
)
from baiducloud_python_sdk_ocr.models.businesslicense_verification_standard_response import (
    BusinesslicenseVerificationStandardResponse,
)
from baiducloud_python_sdk_ocr.models.correct_edu_create_task_response import CorrectEduCreateTaskResponse
from baiducloud_python_sdk_ocr.models.correct_edu_get_result_response import CorrectEduGetResultResponse
from baiducloud_python_sdk_ocr.models.divorce_certificate_response import DivorceCertificateResponse
from baiducloud_python_sdk_ocr.models.doc_analysis_response import DocAnalysisResponse
from baiducloud_python_sdk_ocr.models.doc_analysis_office_response import DocAnalysisOfficeResponse
from baiducloud_python_sdk_ocr.models.doc_classify_response import DocClassifyResponse
from baiducloud_python_sdk_ocr.models.doc_crop_enhance_response import DocCropEnhanceResponse
from baiducloud_python_sdk_ocr.models.driving_license_response import DrivingLicenseResponse
from baiducloud_python_sdk_ocr.models.facade_response import FacadeResponse
from baiducloud_python_sdk_ocr.models.ferry_ticket_response import FerryTicketResponse
from baiducloud_python_sdk_ocr.models.foreign_resident_id_card_response import ForeignResidentIdCardResponse
from baiducloud_python_sdk_ocr.models.forgery_detection_response import ForgeryDetectionResponse
from baiducloud_python_sdk_ocr.models.four_factors_verification_response import FourFactorsVerificationResponse
from baiducloud_python_sdk_ocr.models.general_response import GeneralResponse
from baiducloud_python_sdk_ocr.models.general_basic_response import GeneralBasicResponse
from baiducloud_python_sdk_ocr.models.handwriting_response import HandwritingResponse
from baiducloud_python_sdk_ocr.models.handwriting_composition_create_task_response import (
    HandwritingCompositionCreateTaskResponse,
)
from baiducloud_python_sdk_ocr.models.handwriting_composition_get_result_response import (
    HandwritingCompositionGetResultResponse,
)
from baiducloud_python_sdk_ocr.models.health_report_response import HealthReportResponse
from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_response import (
    HkMacauTaiwanExitentrypermitResponse,
)
from baiducloud_python_sdk_ocr.models.hk_macau_taiwanpermit_response import HkMacauTaiwanpermitResponse
from baiducloud_python_sdk_ocr.models.household_register_response import HouseholdRegisterResponse
from baiducloud_python_sdk_ocr.models.idcard_response import IdcardResponse
from baiducloud_python_sdk_ocr.models.invoice_response import InvoiceResponse
from baiducloud_python_sdk_ocr.models.license_plate_response import LicensePlateResponse
from baiducloud_python_sdk_ocr.models.marriage_certificate_response import MarriageCertificateResponse
from baiducloud_python_sdk_ocr.models.medical_detail_response import MedicalDetailResponse
from baiducloud_python_sdk_ocr.models.medical_invoice_response import MedicalInvoiceResponse
from baiducloud_python_sdk_ocr.models.medical_prescription_response import MedicalPrescriptionResponse
from baiducloud_python_sdk_ocr.models.medical_record_response import MedicalRecordResponse
from baiducloud_python_sdk_ocr.models.medical_report_detection_response import MedicalReportDetectionResponse
from baiducloud_python_sdk_ocr.models.medical_statement_response import MedicalStatementResponse
from baiducloud_python_sdk_ocr.models.medical_summary_response import MedicalSummaryResponse
from baiducloud_python_sdk_ocr.models.meter_response import MeterResponse
from baiducloud_python_sdk_ocr.models.mixed_multi_vehicle_response import MixedMultiVehicleResponse
from baiducloud_python_sdk_ocr.models.multi_idcard_response import MultiIdcardResponse
from baiducloud_python_sdk_ocr.models.multiple_invoice_response import MultipleInvoiceResponse
from baiducloud_python_sdk_ocr.models.numbers_response import NumbersResponse
from baiducloud_python_sdk_ocr.models.online_taxi_itinerary_response import OnlineTaxiItineraryResponse
from baiducloud_python_sdk_ocr.models.overseas_passport_response import OverseasPassportResponse
from baiducloud_python_sdk_ocr.models.paddle_vl_parser_task_response import PaddleVlParserTaskResponse
from baiducloud_python_sdk_ocr.models.paddle_vl_parser_task_query_response import PaddleVlParserTaskQueryResponse
from baiducloud_python_sdk_ocr.models.paper_cut_edu_response import PaperCutEduResponse
from baiducloud_python_sdk_ocr.models.paper_cut_edu_vlm_create_task_response import PaperCutEduVlmCreateTaskResponse
from baiducloud_python_sdk_ocr.models.paper_cut_edu_vlm_get_result_response import PaperCutEduVlmGetResultResponse
from baiducloud_python_sdk_ocr.models.parser_task_response import ParserTaskResponse
from baiducloud_python_sdk_ocr.models.parser_task_query_response import ParserTaskQueryResponse
from baiducloud_python_sdk_ocr.models.passport_response import PassportResponse
from baiducloud_python_sdk_ocr.models.qrcode_response import QrcodeResponse
from baiducloud_python_sdk_ocr.models.quota_invoice_response import QuotaInvoiceResponse
from baiducloud_python_sdk_ocr.models.real_estate_certificate_response import RealEstateCertificateResponse
from baiducloud_python_sdk_ocr.models.remove_handwriting_response import RemoveHandwritingResponse
from baiducloud_python_sdk_ocr.models.road_transport_certificate_response import RoadTransportCertificateResponse
from baiducloud_python_sdk_ocr.models.seal_response import SealResponse
from baiducloud_python_sdk_ocr.models.shopping_receipt_response import ShoppingReceiptResponse
from baiducloud_python_sdk_ocr.models.smart_struct_response import SmartStructResponse
from baiducloud_python_sdk_ocr.models.social_security_card_response import SocialSecurityCardResponse
from baiducloud_python_sdk_ocr.models.table_response import TableResponse
from baiducloud_python_sdk_ocr.models.taxi_receipt_response import TaxiReceiptResponse
from baiducloud_python_sdk_ocr.models.three_factors_verification_response import ThreeFactorsVerificationResponse
from baiducloud_python_sdk_ocr.models.toll_invoice_response import TollInvoiceResponse
from baiducloud_python_sdk_ocr.models.train_ticket_response import TrainTicketResponse
from baiducloud_python_sdk_ocr.models.two_factors_verification_response import TwoFactorsVerificationResponse
from baiducloud_python_sdk_ocr.models.used_vehicle_invoice_response import UsedVehicleInvoiceResponse
from baiducloud_python_sdk_ocr.models.vat_invoice_response import VatInvoiceResponse
from baiducloud_python_sdk_ocr.models.vehicle_certificate_response import VehicleCertificateResponse
from baiducloud_python_sdk_ocr.models.vehicle_invoice_response import VehicleInvoiceResponse
from baiducloud_python_sdk_ocr.models.vehicle_license_response import VehicleLicenseResponse
from baiducloud_python_sdk_ocr.models.vehicle_reg_certificate_response import VehicleRegCertificateResponse
from baiducloud_python_sdk_ocr.models.vehicle_registration_certificate_response import (
    VehicleRegistrationCertificateResponse,
)
from baiducloud_python_sdk_ocr.models.vin_code_response import VinCodeResponse
from baiducloud_python_sdk_ocr.models.waybill_response import WaybillResponse
from baiducloud_python_sdk_ocr.models.web_image_response import WebImageResponse
from baiducloud_python_sdk_ocr.models.web_image_loc_response import WebImageLocResponse
from baiducloud_python_sdk_ocr.models.weight_note_response import WeightNoteResponse

_logger = logging.getLogger(__name__)


class OcrClient(BceBaseClient):
    """
    ocr base sdk client
    """

    CONSTANT_REST = b'rest'

    CONSTANT_2_0 = b'2.0'

    CONSTANT_OCR = b'ocr'

    CONSTANT_V1 = b'v1'

    CONSTANT_BUSINESS_LICENSE = b'business_license'

    CONSTANT_BRAIN = b'brain'

    CONSTANT_ONLINE = b'online'

    CONSTANT_V2 = b'v2'

    CONSTANT_PADDLE_VL_PARSER = b'paddle-vl-parser'

    CONSTANT_TASK = b'task'

    CONSTANT_QUERY = b'query'

    CONSTANT_ACCURATE = b'accurate'

    CONSTANT_NUMBERS = b'numbers'

    CONSTANT_FACADE = b'facade'

    CONSTANT_FORGERY_DETECTION = b'forgery_detection'

    CONSTANT_CORRECT_EDU = b'correct_edu'

    CONSTANT_CREATE_TASK = b'create_task'

    CONSTANT_ONLINE_TAXI_ITINERARY = b'online_taxi_itinerary'

    CONSTANT_VEHICLE_REGISTRATION_CERTIFICATE = b'vehicle_registration_certificate'

    CONSTANT_LICENSE_PLATE = b'license_plate'

    CONSTANT_THREE_FACTORS_VERIFICATION = b'three_factors_verification'

    CONSTANT_WAYBILL = b'waybill'

    CONSTANT_PASSPORT = b'passport'

    CONSTANT_WEBIMAGE = b'webimage'

    CONSTANT_GET_RESULT = b'get_result'

    CONSTANT_TOLL_INVOICE = b'toll_invoice'

    CONSTANT_DOC_CLASSIFY = b'doc_classify'

    CONSTANT_VAT_INVOICE = b'vat_invoice'

    CONSTANT_DOC_ANALYSIS_OFFICE = b'doc_analysis_office'

    CONSTANT_TAXI_RECEIPT = b'taxi_receipt'

    CONSTANT_VEHICLE_CERTIFICATE = b'vehicle_certificate'

    CONSTANT_METER = b'meter'

    CONSTANT_HANDWRITING_COMPOSITION = b'handwriting_composition'

    CONSTANT_HANDWRITING = b'handwriting'

    CONSTANT_DOC_CROP_ENHANCE = b'doc_crop_enhance'

    CONSTANT_MEDICAL_RECORD = b'medical_record'

    CONSTANT_BUSINESSLICENSE_VERIFICATION_DETAILED = b'businesslicense_verification_detailed'

    CONSTANT_WEIGHT_NOTE = b'weight_note'

    CONSTANT_SOCIAL_SECURITY_CARD = b'social_security_card'

    CONSTANT_SHOPPING_RECEIPT = b'shopping_receipt'

    CONSTANT_MEDICAL_REPORT_DETECTION = b'medical_report_detection'

    CONSTANT_FERRY_TICKET = b'ferry_ticket'

    CONSTANT_BUSINESSLICENSE_VERIFICATION_STANDARD = b'businesslicense_verification_standard'

    CONSTANT_BIRTH_CERTIFICATE = b'birth_certificate'

    CONSTANT_REAL_ESTATE_CERTIFICATE = b'real_estate_certificate'

    CONSTANT_REMOVE_HANDWRITING = b'remove_handwriting'

    CONSTANT_ACCURATE_BASIC = b'accurate_basic'

    CONSTANT_HOUSEHOLD_REGISTER = b'household_register'

    CONSTANT_OVERSEAS_PASSPORT = b'overseas_passport'

    CONSTANT_SMART_STRUCT = b'smart_struct'

    CONSTANT_QUOTA_INVOICE = b'quota_invoice'

    CONSTANT_MULTIPLE_INVOICE = b'multiple_invoice'

    CONSTANT_WEBIMAGE_LOC = b'webimage_loc'

    CONSTANT_ROAD_TRANSPORT_CERTIFICATE = b'road_transport_certificate'

    CONSTANT_MULTI_IDCARD = b'multi_idcard'

    CONSTANT_QRCODE = b'qrcode'

    CONSTANT_GENERAL_BASIC = b'general_basic'

    CONSTANT_SEAL = b'seal'

    CONSTANT_TWO_FACTORS_VERIFICATION = b'two_factors_verification'

    CONSTANT_FOUR_FACTORS_VERIFICATION = b'four_factors_verification'

    CONSTANT_MEDICAL_DETAIL = b'medical_detail'

    CONSTANT_PARSER = b'parser'

    CONSTANT_PAPER_CUT_EDU_VLM = b'paper_cut_edu_vlm'

    CONSTANT_GENERAL = b'general'

    CONSTANT_BANK_RECEIPT_NEW = b'bank_receipt_new'

    CONSTANT_VIN_CODE = b'vin_code'

    CONSTANT_MEDICAL_STATEMENT = b'medical_statement'

    CONSTANT_FOREIGN_RESIDENT_ID_CARD = b'foreign_resident_id_card'

    CONSTANT_MIXED_MULTI_VEHICLE = b'mixed_multi_vehicle'

    CONSTANT_HK_MACAU_TAIWAN_EXITENTRYPERMIT = b'hk_macau_taiwan_exitentrypermit'

    CONSTANT_DOC_ANALYSIS = b'doc_analysis'

    CONSTANT_TABLE = b'table'

    CONSTANT_VEHICLE_LICENSE = b'vehicle_license'

    CONSTANT_MEDICAL_PRESCRIPTION = b'medical_prescription'

    CONSTANT_MARRIAGE_CERTIFICATE = b'marriage_certificate'

    CONSTANT_MEDICAL_INVOICE = b'medical_invoice'

    CONSTANT_USED_VEHICLE_INVOICE = b'used_vehicle_invoice'

    CONSTANT_HEALTH_REPORT = b'health_report'

    CONSTANT_PAPER_CUT_EDU = b'paper_cut_edu'

    CONSTANT_ACCOUNT_OPENING = b'account_opening'

    CONSTANT_AIR_TICKET = b'air_ticket'

    CONSTANT_TRAIN_TICKET = b'train_ticket'

    CONSTANT_MEDICAL_SUMMARY = b'medical_summary'

    CONSTANT_VEHICLE_INVOICE = b'vehicle_invoice'

    CONSTANT_DRIVING_LICENSE = b'driving_license'

    CONSTANT_DIVORCE_CERTIFICATE = b'divorce_certificate'

    CONSTANT_IDCARD = b'idcard'

    CONSTANT_BUS_TICKET = b'bus_ticket'

    CONSTANT_INVOICE = b'invoice'

    CONSTANT_BANKCARD = b'bankcard'

    def __init__(self, config=None):
        """
        Initialize the ocr client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def account_opening(self, request, config=None):
        """
        account_opening

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AccountOpeningResponse data
        :rtype: AccountOpeningResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_ACCOUNT_OPENING,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=AccountOpeningResponse,
        )

    def accurate(self, request, config=None):
        """
        accurate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AccurateResponse data
        :rtype: AccurateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_ACCURATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=AccurateResponse
        )

    def accurate_basic(self, request, config=None):
        """
        accurate_basic

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AccurateBasicResponse data
        :rtype: AccurateBasicResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_ACCURATE_BASIC,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=AccurateBasicResponse,
        )

    def air_ticket(self, request, config=None):
        """
        air_ticket

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AirTicketResponse data
        :rtype: AirTicketResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_AIR_TICKET,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=AirTicketResponse,
        )

    def bank_receipt_new(self, request, config=None):
        """
        bank_receipt_new

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BankReceiptNewResponse data
        :rtype: BankReceiptNewResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_BANK_RECEIPT_NEW,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=BankReceiptNewResponse,
        )

    def bankcard(self, request, config=None):
        """
        bankcard

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BankcardResponse data
        :rtype: BankcardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_BANKCARD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=BankcardResponse
        )

    def birth_certificate(self, request, config=None):
        """
        birth_certificate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BirthCertificateResponse data
        :rtype: BirthCertificateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_BIRTH_CERTIFICATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=BirthCertificateResponse,
        )

    def bus_ticket(self, request, config=None):
        """
        bus_ticket

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BusTicketResponse data
        :rtype: BusTicketResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_BUS_TICKET,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=BusTicketResponse,
        )

    def business_license(self, request, config=None):
        """
        business_license

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BusinessLicenseResponse data
        :rtype: BusinessLicenseResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_BUSINESS_LICENSE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=BusinessLicenseResponse,
        )

    def businesslicense_detailed(self, request, config=None):
        """
        businesslicense_detailed

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BusinesslicenseDetailedResponse data
        :rtype: BusinesslicenseDetailedResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_BUSINESSLICENSE_VERIFICATION_DETAILED,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=BusinesslicenseDetailedResponse,
        )

    def businesslicense_standard(self, request, config=None):
        """
        businesslicense_standard

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BusinesslicenseStandardResponse data
        :rtype: BusinesslicenseStandardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_BUSINESSLICENSE_VERIFICATION_STANDARD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=BusinesslicenseStandardResponse,
        )

    def businesslicense_verification_detailed(self, request, config=None):
        """
        businesslicense_verification_detailed

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BusinesslicenseVerificationDetailedResponse data
        :rtype: BusinesslicenseVerificationDetailedResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_BUSINESSLICENSE_VERIFICATION_DETAILED,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=BusinesslicenseVerificationDetailedResponse,
        )

    def businesslicense_verification_standard(self, request, config=None):
        """
        businesslicense_verification_standard

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing BusinesslicenseVerificationStandardResponse data
        :rtype: BusinesslicenseVerificationStandardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_BUSINESSLICENSE_VERIFICATION_STANDARD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=BusinesslicenseVerificationStandardResponse,
        )

    def correct_edu_create_task(self, request, config=None):
        """
        correct_edu_create_task

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CorrectEduCreateTaskResponse data
        :rtype: CorrectEduCreateTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_CORRECT_EDU,
            OcrClient.CONSTANT_CREATE_TASK,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CorrectEduCreateTaskResponse,
        )

    def correct_edu_get_result(self, request, config=None):
        """
        correct_edu_get_result

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CorrectEduGetResultResponse data
        :rtype: CorrectEduGetResultResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_CORRECT_EDU,
            OcrClient.CONSTANT_GET_RESULT,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=CorrectEduGetResultResponse,
        )

    def divorce_certificate(self, request, config=None):
        """
        divorce_certificate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DivorceCertificateResponse data
        :rtype: DivorceCertificateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_DIVORCE_CERTIFICATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=DivorceCertificateResponse,
        )

    def doc_analysis(self, request, config=None):
        """
        doc_analysis

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DocAnalysisResponse data
        :rtype: DocAnalysisResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_DOC_ANALYSIS,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=DocAnalysisResponse,
        )

    def doc_analysis_office(self, request, config=None):
        """
        doc_analysis_office

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DocAnalysisOfficeResponse data
        :rtype: DocAnalysisOfficeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_DOC_ANALYSIS_OFFICE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=DocAnalysisOfficeResponse,
        )

    def doc_classify(self, request, config=None):
        """
        doc_classify

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DocClassifyResponse data
        :rtype: DocClassifyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_DOC_CLASSIFY,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=DocClassifyResponse,
        )

    def doc_crop_enhance(self, request, config=None):
        """
        doc_crop_enhance

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DocCropEnhanceResponse data
        :rtype: DocCropEnhanceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_DOC_CROP_ENHANCE,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=DocCropEnhanceResponse,
        )

    def driving_license(self, request, config=None):
        """
        driving_license

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DrivingLicenseResponse data
        :rtype: DrivingLicenseResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_DRIVING_LICENSE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=DrivingLicenseResponse,
        )

    def facade(self, request, config=None):
        """
        facade

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FacadeResponse data
        :rtype: FacadeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_FACADE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=FacadeResponse
        )

    def ferry_ticket(self, request, config=None):
        """
        ferry_ticket

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FerryTicketResponse data
        :rtype: FerryTicketResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_FERRY_TICKET,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=FerryTicketResponse,
        )

    def foreign_resident_id_card(self, request, config=None):
        """
        foreign_resident_id_card

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ForeignResidentIdCardResponse data
        :rtype: ForeignResidentIdCardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_FOREIGN_RESIDENT_ID_CARD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ForeignResidentIdCardResponse,
        )

    def forgery_detection(self, request, config=None):
        """
        forgery_detection

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ForgeryDetectionResponse data
        :rtype: ForgeryDetectionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_FORGERY_DETECTION,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ForgeryDetectionResponse,
        )

    def four_factors_verification(self, request, config=None):
        """
        four_factors_verification

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing FourFactorsVerificationResponse data
        :rtype: FourFactorsVerificationResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_FOUR_FACTORS_VERIFICATION,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=FourFactorsVerificationResponse,
        )

    def general(self, request, config=None):
        """
        general

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GeneralResponse data
        :rtype: GeneralResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_GENERAL,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=GeneralResponse
        )

    def general_basic(self, request, config=None):
        """
        general_basic

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GeneralBasicResponse data
        :rtype: GeneralBasicResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_GENERAL_BASIC,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=GeneralBasicResponse,
        )

    def handwriting(self, request, config=None):
        """
        handwriting

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing HandwritingResponse data
        :rtype: HandwritingResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_HANDWRITING,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=HandwritingResponse,
        )

    def handwriting_composition_create_task(self, request, config=None):
        """
        handwriting_composition_create_task

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing HandwritingCompositionCreateTaskResponse data
        :rtype: HandwritingCompositionCreateTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_HANDWRITING_COMPOSITION,
            OcrClient.CONSTANT_CREATE_TASK,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=HandwritingCompositionCreateTaskResponse,
        )

    def handwriting_composition_get_result(self, request, config=None):
        """
        handwriting_composition_get_result

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing HandwritingCompositionGetResultResponse data
        :rtype: HandwritingCompositionGetResultResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_HANDWRITING_COMPOSITION,
            OcrClient.CONSTANT_GET_RESULT,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=HandwritingCompositionGetResultResponse,
        )

    def health_report(self, request, config=None):
        """
        health_report

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing HealthReportResponse data
        :rtype: HealthReportResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_HEALTH_REPORT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=HealthReportResponse,
        )

    def hk_macau_taiwan_exitentrypermit(self, request, config=None):
        """
        hk_macau_taiwan_exitentrypermit

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing HkMacauTaiwanExitentrypermitResponse data
        :rtype: HkMacauTaiwanExitentrypermitResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_HK_MACAU_TAIWAN_EXITENTRYPERMIT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=HkMacauTaiwanExitentrypermitResponse,
        )

    def hk_macau_taiwanpermit(self, request, config=None):
        """
        hk_macau_taiwanpermit

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing HkMacauTaiwanpermitResponse data
        :rtype: HkMacauTaiwanpermitResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_HK_MACAU_TAIWAN_EXITENTRYPERMIT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=HkMacauTaiwanpermitResponse,
        )

    def household_register(self, request, config=None):
        """
        household_register

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing HouseholdRegisterResponse data
        :rtype: HouseholdRegisterResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_HOUSEHOLD_REGISTER,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=HouseholdRegisterResponse,
        )

    def idcard(self, request, config=None):
        """
        idcard

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing IdcardResponse data
        :rtype: IdcardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_IDCARD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=IdcardResponse
        )

    def invoice(self, request, config=None):
        """
        invoice

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing InvoiceResponse data
        :rtype: InvoiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_INVOICE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=InvoiceResponse
        )

    def license_plate(self, request, config=None):
        """
        license_plate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing LicensePlateResponse data
        :rtype: LicensePlateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_LICENSE_PLATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=LicensePlateResponse,
        )

    def marriage_certificate(self, request, config=None):
        """
        marriage_certificate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MarriageCertificateResponse data
        :rtype: MarriageCertificateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MARRIAGE_CERTIFICATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MarriageCertificateResponse,
        )

    def medical_detail(self, request, config=None):
        """
        medical_detail

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MedicalDetailResponse data
        :rtype: MedicalDetailResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MEDICAL_DETAIL,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MedicalDetailResponse,
        )

    def medical_invoice(self, request, config=None):
        """
        medical_invoice

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MedicalInvoiceResponse data
        :rtype: MedicalInvoiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MEDICAL_INVOICE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MedicalInvoiceResponse,
        )

    def medical_prescription(self, request, config=None):
        """
        medical_prescription

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MedicalPrescriptionResponse data
        :rtype: MedicalPrescriptionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MEDICAL_PRESCRIPTION,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MedicalPrescriptionResponse,
        )

    def medical_record(self, request, config=None):
        """
        medical_record

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MedicalRecordResponse data
        :rtype: MedicalRecordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MEDICAL_RECORD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MedicalRecordResponse,
        )

    def medical_report_detection(self, request, config=None):
        """
        medical_report_detection

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MedicalReportDetectionResponse data
        :rtype: MedicalReportDetectionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MEDICAL_REPORT_DETECTION,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MedicalReportDetectionResponse,
        )

    def medical_statement(self, request, config=None):
        """
        medical_statement

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MedicalStatementResponse data
        :rtype: MedicalStatementResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MEDICAL_STATEMENT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MedicalStatementResponse,
        )

    def medical_summary(self, request, config=None):
        """
        medical_summary

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MedicalSummaryResponse data
        :rtype: MedicalSummaryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MEDICAL_SUMMARY,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MedicalSummaryResponse,
        )

    def meter(self, request, config=None):
        """
        meter

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MeterResponse data
        :rtype: MeterResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_METER,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=MeterResponse
        )

    def mixed_multi_vehicle(self, request, config=None):
        """
        mixed_multi_vehicle

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MixedMultiVehicleResponse data
        :rtype: MixedMultiVehicleResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MIXED_MULTI_VEHICLE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MixedMultiVehicleResponse,
        )

    def multi_idcard(self, request, config=None):
        """
        multi_idcard

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MultiIdcardResponse data
        :rtype: MultiIdcardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MULTI_IDCARD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MultiIdcardResponse,
        )

    def multiple_invoice(self, request, config=None):
        """
        multiple_invoice

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing MultipleInvoiceResponse data
        :rtype: MultipleInvoiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_MULTIPLE_INVOICE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=MultipleInvoiceResponse,
        )

    def numbers(self, request, config=None):
        """
        numbers

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing NumbersResponse data
        :rtype: NumbersResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_NUMBERS,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=NumbersResponse
        )

    def online_taxi_itinerary(self, request, config=None):
        """
        online_taxi_itinerary

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing OnlineTaxiItineraryResponse data
        :rtype: OnlineTaxiItineraryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_ONLINE_TAXI_ITINERARY,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=OnlineTaxiItineraryResponse,
        )

    def overseas_passport(self, request, config=None):
        """
        overseas_passport

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing OverseasPassportResponse data
        :rtype: OverseasPassportResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_OVERSEAS_PASSPORT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=OverseasPassportResponse,
        )

    def paddle_vl_parser_task(self, request, config=None):
        """
        paddle_vl_parser_task

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PaddleVlParserTaskResponse data
        :rtype: PaddleVlParserTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_BRAIN,
            OcrClient.CONSTANT_ONLINE,
            OcrClient.CONSTANT_V2,
            OcrClient.CONSTANT_PADDLE_VL_PARSER,
            OcrClient.CONSTANT_TASK,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=PaddleVlParserTaskResponse,
        )

    def paddle_vl_parser_task_query(self, request, config=None):
        """
        paddle_vl_parser_task_query

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PaddleVlParserTaskQueryResponse data
        :rtype: PaddleVlParserTaskQueryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_BRAIN,
            OcrClient.CONSTANT_ONLINE,
            OcrClient.CONSTANT_V2,
            OcrClient.CONSTANT_PADDLE_VL_PARSER,
            OcrClient.CONSTANT_TASK,
            OcrClient.CONSTANT_QUERY,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=PaddleVlParserTaskQueryResponse,
        )

    def paper_cut_edu(self, request, config=None):
        """
        paper_cut_edu

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PaperCutEduResponse data
        :rtype: PaperCutEduResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_PAPER_CUT_EDU,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=PaperCutEduResponse,
        )

    def paper_cut_edu_vlm_create_task(self, request, config=None):
        """
        paper_cut_edu_vlm_create_task

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PaperCutEduVlmCreateTaskResponse data
        :rtype: PaperCutEduVlmCreateTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_PAPER_CUT_EDU_VLM,
            OcrClient.CONSTANT_CREATE_TASK,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=PaperCutEduVlmCreateTaskResponse,
        )

    def paper_cut_edu_vlm_get_result(self, request, config=None):
        """
        paper_cut_edu_vlm_get_result

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PaperCutEduVlmGetResultResponse data
        :rtype: PaperCutEduVlmGetResultResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_PAPER_CUT_EDU_VLM,
            OcrClient.CONSTANT_GET_RESULT,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=PaperCutEduVlmGetResultResponse,
        )

    def parser_task(self, request, config=None):
        """
        parser_task

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ParserTaskResponse data
        :rtype: ParserTaskResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_BRAIN,
            OcrClient.CONSTANT_ONLINE,
            OcrClient.CONSTANT_V2,
            OcrClient.CONSTANT_PARSER,
            OcrClient.CONSTANT_TASK,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ParserTaskResponse,
        )

    def parser_task_query(self, request, config=None):
        """
        parser_task_query

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ParserTaskQueryResponse data
        :rtype: ParserTaskQueryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_BRAIN,
            OcrClient.CONSTANT_ONLINE,
            OcrClient.CONSTANT_V2,
            OcrClient.CONSTANT_PARSER,
            OcrClient.CONSTANT_TASK,
            OcrClient.CONSTANT_QUERY,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ParserTaskQueryResponse,
        )

    def passport(self, request, config=None):
        """
        passport

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing PassportResponse data
        :rtype: PassportResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_PASSPORT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=PassportResponse
        )

    def qrcode(self, request, config=None):
        """
        qrcode

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QrcodeResponse data
        :rtype: QrcodeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_QRCODE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=QrcodeResponse
        )

    def quota_invoice(self, request, config=None):
        """
        quota_invoice

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing QuotaInvoiceResponse data
        :rtype: QuotaInvoiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_QUOTA_INVOICE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=QuotaInvoiceResponse,
        )

    def real_estate_certificate(self, request, config=None):
        """
        real_estate_certificate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RealEstateCertificateResponse data
        :rtype: RealEstateCertificateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_REAL_ESTATE_CERTIFICATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=RealEstateCertificateResponse,
        )

    def remove_handwriting(self, request, config=None):
        """
        remove_handwriting

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RemoveHandwritingResponse data
        :rtype: RemoveHandwritingResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_REMOVE_HANDWRITING,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=RemoveHandwritingResponse,
        )

    def road_transport_certificate(self, request, config=None):
        """
        road_transport_certificate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RoadTransportCertificateResponse data
        :rtype: RoadTransportCertificateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_ROAD_TRANSPORT_CERTIFICATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=RoadTransportCertificateResponse,
        )

    def seal(self, request, config=None):
        """
        seal

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SealResponse data
        :rtype: SealResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_SEAL,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=SealResponse
        )

    def shopping_receipt(self, request, config=None):
        """
        shopping_receipt

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ShoppingReceiptResponse data
        :rtype: ShoppingReceiptResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_SHOPPING_RECEIPT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ShoppingReceiptResponse,
        )

    def smart_struct(self, request, config=None):
        """
        smart_struct

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SmartStructResponse data
        :rtype: SmartStructResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_SMART_STRUCT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SmartStructResponse,
        )

    def social_security_card(self, request, config=None):
        """
        social_security_card

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SocialSecurityCardResponse data
        :rtype: SocialSecurityCardResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_SOCIAL_SECURITY_CARD,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=SocialSecurityCardResponse,
        )

    def table(self, request, config=None):
        """
        table

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TableResponse data
        :rtype: TableResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_TABLE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=TableResponse
        )

    def taxi_receipt(self, request, config=None):
        """
        taxi_receipt

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TaxiReceiptResponse data
        :rtype: TaxiReceiptResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_TAXI_RECEIPT,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=TaxiReceiptResponse,
        )

    def three_factors_verification(self, request, config=None):
        """
        three_factors_verification

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing ThreeFactorsVerificationResponse data
        :rtype: ThreeFactorsVerificationResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_THREE_FACTORS_VERIFICATION,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=ThreeFactorsVerificationResponse,
        )

    def toll_invoice(self, request, config=None):
        """
        toll_invoice

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TollInvoiceResponse data
        :rtype: TollInvoiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_TOLL_INVOICE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=TollInvoiceResponse,
        )

    def train_ticket(self, request, config=None):
        """
        train_ticket

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TrainTicketResponse data
        :rtype: TrainTicketResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_TRAIN_TICKET,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=TrainTicketResponse,
        )

    def two_factors_verification(self, request, config=None):
        """
        two_factors_verification

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TwoFactorsVerificationResponse data
        :rtype: TwoFactorsVerificationResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_TWO_FACTORS_VERIFICATION,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=TwoFactorsVerificationResponse,
        )

    def used_vehicle_invoice(self, request, config=None):
        """
        used_vehicle_invoice

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing UsedVehicleInvoiceResponse data
        :rtype: UsedVehicleInvoiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_USED_VEHICLE_INVOICE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=UsedVehicleInvoiceResponse,
        )

    def vat_invoice(self, request, config=None):
        """
        vat_invoice

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing VatInvoiceResponse data
        :rtype: VatInvoiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_VAT_INVOICE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=VatInvoiceResponse,
        )

    def vehicle_certificate(self, request, config=None):
        """
        vehicle_certificate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing VehicleCertificateResponse data
        :rtype: VehicleCertificateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_VEHICLE_CERTIFICATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=VehicleCertificateResponse,
        )

    def vehicle_invoice(self, request, config=None):
        """
        vehicle_invoice

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing VehicleInvoiceResponse data
        :rtype: VehicleInvoiceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_VEHICLE_INVOICE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=VehicleInvoiceResponse,
        )

    def vehicle_license(self, request, config=None):
        """
        vehicle_license

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing VehicleLicenseResponse data
        :rtype: VehicleLicenseResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_VEHICLE_LICENSE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=VehicleLicenseResponse,
        )

    def vehicle_reg_certificate(self, request, config=None):
        """
        vehicle_reg_certificate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing VehicleRegCertificateResponse data
        :rtype: VehicleRegCertificateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_VEHICLE_REGISTRATION_CERTIFICATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=VehicleRegCertificateResponse,
        )

    def vehicle_registration_certificate(self, request, config=None):
        """
        vehicle_registration_certificate

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing VehicleRegistrationCertificateResponse data
        :rtype: VehicleRegistrationCertificateResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_VEHICLE_REGISTRATION_CERTIFICATE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=VehicleRegistrationCertificateResponse,
        )

    def vin_code(self, request, config=None):
        """
        vin_code

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing VinCodeResponse data
        :rtype: VinCodeResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_VIN_CODE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=VinCodeResponse
        )

    def waybill(self, request, config=None):
        """
        waybill

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing WaybillResponse data
        :rtype: WaybillResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_WAYBILL,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=WaybillResponse
        )

    def web_image(self, request, config=None):
        """
        web_image

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing WebImageResponse data
        :rtype: WebImageResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_WEBIMAGE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=form_body, headers=headers, config=merged_config, model=WebImageResponse
        )

    def web_image_loc(self, request, config=None):
        """
        web_image_loc

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing WebImageLocResponse data
        :rtype: WebImageLocResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_WEBIMAGE_LOC,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=WebImageLocResponse,
        )

    def weight_note(self, request, config=None):
        """
        weight_note

        :param request: Request entity containing all parameters
        :type request: OcrClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing WeightNoteResponse data
        :rtype: WeightNoteResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            OcrClient.CONSTANT_REST,
            OcrClient.CONSTANT_2_0,
            OcrClient.CONSTANT_OCR,
            OcrClient.CONSTANT_V1,
            OcrClient.CONSTANT_WEIGHT_NOTE,
        )
        headers = {}
        headers[b'Content-Type'] = b'application/x-www-form-urlencoded'
        form_body, _, _ = request_body_utils.fill_payload_as_form(request)
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=form_body,
            headers=headers,
            config=merged_config,
            model=WeightNoteResponse,
        )

    def _merge_config(self, config=None):
        """
        :param config:
        :type config: baiducloud_python_sdk_core.BceClientConfiguration
        """
        if config is None:
            return self.config
        else:
            new_config = copy.copy(self.config)
            new_config.merge_non_none_values(config)
            return new_config

    def _send_request(
        self, http_method, path, body=None, headers=None, params=None, config=None, body_parser=None, model=None
    ):
        """
        Send an HTTP request to the service endpoint.

        :param http_method: HTTP method (GET, POST, PUT, DELETE, etc.)
        :type http_method: bytes
        :param path: Request path
        :type path: bytes
        :param body: Optional request body
        :type body: str or bytes
        :param headers: Optional HTTP headers
        :type headers: dict
        :param params: Optional query parameters
        :type params: dict
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration
        :param body_parser: Optional custom body parser function
        :type body_parser: callable
        :param model: Optional response model class for deserialization
        :type model: class

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network connection failure, SSL errors, etc.)
        :raises BceServerError: Server returned error response
        """
        config = self._merge_config(config)
        if body_parser is None:
            body_parser = handler.parse_json
        if headers is None:
            headers = {b'Accept': b'*/*', b'Content-Type': b'application/json;charset=utf-8'}
        sign_fn, params = self._choose_signer(config, params)
        return bce_http_client.send_request(
            config, sign_fn, [handler.parse_error, body_parser], http_method, path, body, headers, params, model=model
        )
