import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.auth.api_key_credentials import ApiKeyCredentials
from baiducloud_python_sdk_core.auth.access_token_credentials import AccessTokenCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_ocr.api.ocr_client import OcrClient
from baiducloud_python_sdk_ocr import models as ocr_models


class OcrClientTest(unittest.TestCase):
    """OcrClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        API_KEY = ''
        SECRET_KEY = ''

        # ==== AK/SK 鉴权 ====
        # config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

        # ==== AccessToken 鉴权（API Key / Secret Key 换取 AccessToken）====
        # config = BceClientConfiguration(credentials=AccessTokenCredentials(API_KEY, SECRET_KEY), endpoint=HOST)

        # ==== API Key 鉴权 ====
        config = BceClientConfiguration(credentials=ApiKeyCredentials(API_KEY), endpoint=HOST)

        self.client = OcrClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_account_opening(self):
        self.client.account_opening(ocr_models.AccountOpeningRequest())

    def test_accurate(self):
        self.client.accurate(ocr_models.AccurateRequest())

    def test_accurate_basic(self):
        self.client.accurate_basic(ocr_models.AccurateBasicRequest())

    def test_air_ticket(self):
        self.client.air_ticket(ocr_models.AirTicketRequest())

    def test_bank_receipt_new(self):
        self.client.bank_receipt_new(ocr_models.BankReceiptNewRequest())

    def test_bankcard(self):
        self.client.bankcard(ocr_models.BankcardRequest())

    def test_birth_certificate(self):
        self.client.birth_certificate(ocr_models.BirthCertificateRequest())

    def test_bus_ticket(self):
        self.client.bus_ticket(ocr_models.BusTicketRequest())

    def test_business_license(self):
        self.client.business_license(ocr_models.BusinessLicenseRequest())

    def test_businesslicense_detailed(self):
        self.client.businesslicense_detailed(ocr_models.BusinesslicenseDetailedRequest())

    def test_businesslicense_standard(self):
        self.client.businesslicense_standard(ocr_models.BusinesslicenseStandardRequest())

    def test_businesslicense_verification_detailed(self):
        self.client.businesslicense_verification_detailed(ocr_models.BusinesslicenseVerificationDetailedRequest())

    def test_businesslicense_verification_standard(self):
        self.client.businesslicense_verification_standard(ocr_models.BusinesslicenseVerificationStandardRequest())

    def test_correct_edu_create_task(self):
        self.client.correct_edu_create_task(ocr_models.CorrectEduCreateTaskRequest())

    def test_correct_edu_get_result(self):
        self.client.correct_edu_get_result(ocr_models.CorrectEduGetResultRequest())

    def test_divorce_certificate(self):
        self.client.divorce_certificate(ocr_models.DivorceCertificateRequest())

    def test_doc_analysis(self):
        self.client.doc_analysis(ocr_models.DocAnalysisRequest())

    def test_doc_analysis_office(self):
        self.client.doc_analysis_office(ocr_models.DocAnalysisOfficeRequest())

    def test_doc_classify(self):
        self.client.doc_classify(ocr_models.DocClassifyRequest())

    def test_doc_crop_enhance(self):
        self.client.doc_crop_enhance(ocr_models.DocCropEnhanceRequest())

    def test_driving_license(self):
        self.client.driving_license(ocr_models.DrivingLicenseRequest())

    def test_facade(self):
        self.client.facade(ocr_models.FacadeRequest())

    def test_ferry_ticket(self):
        self.client.ferry_ticket(ocr_models.FerryTicketRequest())

    def test_foreign_resident_id_card(self):
        self.client.foreign_resident_id_card(ocr_models.ForeignResidentIdCardRequest())

    def test_forgery_detection(self):
        self.client.forgery_detection(ocr_models.ForgeryDetectionRequest())

    def test_four_factors_verification(self):
        self.client.four_factors_verification(ocr_models.FourFactorsVerificationRequest())

    def test_general(self):
        self.client.general(ocr_models.GeneralRequest())

    def test_general_basic(self):
        self.client.general_basic(ocr_models.GeneralBasicRequest())

    def test_handwriting(self):
        self.client.handwriting(ocr_models.HandwritingRequest())

    def test_handwriting_composition_create_task(self):
        self.client.handwriting_composition_create_task(ocr_models.HandwritingCompositionCreateTaskRequest())

    def test_handwriting_composition_get_result(self):
        self.client.handwriting_composition_get_result(ocr_models.HandwritingCompositionGetResultRequest())

    def test_health_report(self):
        self.client.health_report(ocr_models.HealthReportRequest())

    def test_hk_macau_taiwan_exitentrypermit(self):
        self.client.hk_macau_taiwan_exitentrypermit(ocr_models.HkMacauTaiwanExitentrypermitRequest())

    def test_hk_macau_taiwanpermit(self):
        self.client.hk_macau_taiwanpermit(ocr_models.HkMacauTaiwanpermitRequest())

    def test_household_register(self):
        self.client.household_register(ocr_models.HouseholdRegisterRequest())

    def test_idcard(self):
        self.client.idcard(ocr_models.IdcardRequest())

    def test_invoice(self):
        self.client.invoice(ocr_models.InvoiceRequest())

    def test_license_plate(self):
        self.client.license_plate(ocr_models.LicensePlateRequest())

    def test_marriage_certificate(self):
        self.client.marriage_certificate(ocr_models.MarriageCertificateRequest())

    def test_medical_detail(self):
        self.client.medical_detail(ocr_models.MedicalDetailRequest())

    def test_medical_invoice(self):
        self.client.medical_invoice(ocr_models.MedicalInvoiceRequest())

    def test_medical_prescription(self):
        self.client.medical_prescription(ocr_models.MedicalPrescriptionRequest())

    def test_medical_record(self):
        self.client.medical_record(ocr_models.MedicalRecordRequest())

    def test_medical_report_detection(self):
        self.client.medical_report_detection(ocr_models.MedicalReportDetectionRequest())

    def test_medical_statement(self):
        self.client.medical_statement(ocr_models.MedicalStatementRequest())

    def test_medical_summary(self):
        self.client.medical_summary(ocr_models.MedicalSummaryRequest())

    def test_meter(self):
        self.client.meter(ocr_models.MeterRequest())

    def test_mixed_multi_vehicle(self):
        self.client.mixed_multi_vehicle(ocr_models.MixedMultiVehicleRequest())

    def test_multi_idcard(self):
        self.client.multi_idcard(ocr_models.MultiIdcardRequest())

    def test_multiple_invoice(self):
        self.client.multiple_invoice(ocr_models.MultipleInvoiceRequest())

    def test_numbers(self):
        self.client.numbers(ocr_models.NumbersRequest())

    def test_online_taxi_itinerary(self):
        self.client.online_taxi_itinerary(ocr_models.OnlineTaxiItineraryRequest())

    def test_overseas_passport(self):
        self.client.overseas_passport(ocr_models.OverseasPassportRequest())

    def test_paddle_vl_parser_task(self):
        self.client.paddle_vl_parser_task(ocr_models.PaddleVlParserTaskRequest())

    def test_paddle_vl_parser_task_query(self):
        self.client.paddle_vl_parser_task_query(ocr_models.PaddleVlParserTaskQueryRequest())

    def test_paper_cut_edu(self):
        self.client.paper_cut_edu(ocr_models.PaperCutEduRequest())

    def test_paper_cut_edu_vlm_create_task(self):
        self.client.paper_cut_edu_vlm_create_task(ocr_models.PaperCutEduVlmCreateTaskRequest())

    def test_paper_cut_edu_vlm_get_result(self):
        self.client.paper_cut_edu_vlm_get_result(ocr_models.PaperCutEduVlmGetResultRequest())

    def test_parser_task(self):
        self.client.parser_task(ocr_models.ParserTaskRequest())

    def test_parser_task_query(self):
        self.client.parser_task_query(ocr_models.ParserTaskQueryRequest())

    def test_passport(self):
        self.client.passport(ocr_models.PassportRequest())

    def test_qrcode(self):
        self.client.qrcode(ocr_models.QrcodeRequest())

    def test_quota_invoice(self):
        self.client.quota_invoice(ocr_models.QuotaInvoiceRequest())

    def test_real_estate_certificate(self):
        self.client.real_estate_certificate(ocr_models.RealEstateCertificateRequest())

    def test_remove_handwriting(self):
        self.client.remove_handwriting(ocr_models.RemoveHandwritingRequest())

    def test_road_transport_certificate(self):
        self.client.road_transport_certificate(ocr_models.RoadTransportCertificateRequest())

    def test_seal(self):
        self.client.seal(ocr_models.SealRequest())

    def test_shopping_receipt(self):
        self.client.shopping_receipt(ocr_models.ShoppingReceiptRequest())

    def test_smart_struct(self):
        self.client.smart_struct(ocr_models.SmartStructRequest())

    def test_social_security_card(self):
        self.client.social_security_card(ocr_models.SocialSecurityCardRequest())

    def test_table(self):
        self.client.table(ocr_models.TableRequest())

    def test_taxi_receipt(self):
        self.client.taxi_receipt(ocr_models.TaxiReceiptRequest())

    def test_three_factors_verification(self):
        self.client.three_factors_verification(ocr_models.ThreeFactorsVerificationRequest())

    def test_toll_invoice(self):
        self.client.toll_invoice(ocr_models.TollInvoiceRequest())

    def test_train_ticket(self):
        self.client.train_ticket(ocr_models.TrainTicketRequest())

    def test_two_factors_verification(self):
        self.client.two_factors_verification(ocr_models.TwoFactorsVerificationRequest())

    def test_used_vehicle_invoice(self):
        self.client.used_vehicle_invoice(ocr_models.UsedVehicleInvoiceRequest())

    def test_vat_invoice(self):
        self.client.vat_invoice(ocr_models.VatInvoiceRequest())

    def test_vehicle_certificate(self):
        self.client.vehicle_certificate(ocr_models.VehicleCertificateRequest())

    def test_vehicle_invoice(self):
        self.client.vehicle_invoice(ocr_models.VehicleInvoiceRequest())

    def test_vehicle_license(self):
        self.client.vehicle_license(ocr_models.VehicleLicenseRequest())

    def test_vehicle_reg_certificate(self):
        self.client.vehicle_reg_certificate(ocr_models.VehicleRegCertificateRequest())

    def test_vehicle_registration_certificate(self):
        self.client.vehicle_registration_certificate(ocr_models.VehicleRegistrationCertificateRequest())

    def test_vin_code(self):
        self.client.vin_code(ocr_models.VinCodeRequest())

    def test_waybill(self):
        self.client.waybill(ocr_models.WaybillRequest())

    def test_web_image(self):
        self.client.web_image(ocr_models.WebImageRequest())

    def test_web_image_loc(self):
        self.client.web_image_loc(ocr_models.WebImageLocRequest())

    def test_weight_note(self):
        self.client.weight_note(ocr_models.WeightNoteRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(OcrClientTest("test_account_opening"))
    suite.addTest(OcrClientTest("test_accurate"))
    suite.addTest(OcrClientTest("test_accurate_basic"))
    suite.addTest(OcrClientTest("test_air_ticket"))
    suite.addTest(OcrClientTest("test_bank_receipt_new"))
    suite.addTest(OcrClientTest("test_bankcard"))
    suite.addTest(OcrClientTest("test_birth_certificate"))
    suite.addTest(OcrClientTest("test_bus_ticket"))
    suite.addTest(OcrClientTest("test_business_license"))
    suite.addTest(OcrClientTest("test_businesslicense_detailed"))
    suite.addTest(OcrClientTest("test_businesslicense_standard"))
    suite.addTest(OcrClientTest("test_businesslicense_verification_detailed"))
    suite.addTest(OcrClientTest("test_businesslicense_verification_standard"))
    suite.addTest(OcrClientTest("test_correct_edu_create_task"))
    suite.addTest(OcrClientTest("test_correct_edu_get_result"))
    suite.addTest(OcrClientTest("test_divorce_certificate"))
    suite.addTest(OcrClientTest("test_doc_analysis"))
    suite.addTest(OcrClientTest("test_doc_analysis_office"))
    suite.addTest(OcrClientTest("test_doc_classify"))
    suite.addTest(OcrClientTest("test_doc_crop_enhance"))
    suite.addTest(OcrClientTest("test_driving_license"))
    suite.addTest(OcrClientTest("test_facade"))
    suite.addTest(OcrClientTest("test_ferry_ticket"))
    suite.addTest(OcrClientTest("test_foreign_resident_id_card"))
    suite.addTest(OcrClientTest("test_forgery_detection"))
    suite.addTest(OcrClientTest("test_four_factors_verification"))
    suite.addTest(OcrClientTest("test_general"))
    suite.addTest(OcrClientTest("test_general_basic"))
    suite.addTest(OcrClientTest("test_handwriting"))
    suite.addTest(OcrClientTest("test_handwriting_composition_create_task"))
    suite.addTest(OcrClientTest("test_handwriting_composition_get_result"))
    suite.addTest(OcrClientTest("test_health_report"))
    suite.addTest(OcrClientTest("test_hk_macau_taiwan_exitentrypermit"))
    suite.addTest(OcrClientTest("test_hk_macau_taiwanpermit"))
    suite.addTest(OcrClientTest("test_household_register"))
    suite.addTest(OcrClientTest("test_idcard"))
    suite.addTest(OcrClientTest("test_invoice"))
    suite.addTest(OcrClientTest("test_license_plate"))
    suite.addTest(OcrClientTest("test_marriage_certificate"))
    suite.addTest(OcrClientTest("test_medical_detail"))
    suite.addTest(OcrClientTest("test_medical_invoice"))
    suite.addTest(OcrClientTest("test_medical_prescription"))
    suite.addTest(OcrClientTest("test_medical_record"))
    suite.addTest(OcrClientTest("test_medical_report_detection"))
    suite.addTest(OcrClientTest("test_medical_statement"))
    suite.addTest(OcrClientTest("test_medical_summary"))
    suite.addTest(OcrClientTest("test_meter"))
    suite.addTest(OcrClientTest("test_mixed_multi_vehicle"))
    suite.addTest(OcrClientTest("test_multi_idcard"))
    suite.addTest(OcrClientTest("test_multiple_invoice"))
    suite.addTest(OcrClientTest("test_numbers"))
    suite.addTest(OcrClientTest("test_online_taxi_itinerary"))
    suite.addTest(OcrClientTest("test_overseas_passport"))
    suite.addTest(OcrClientTest("test_paddle_vl_parser_task"))
    suite.addTest(OcrClientTest("test_paddle_vl_parser_task_query"))
    suite.addTest(OcrClientTest("test_paper_cut_edu"))
    suite.addTest(OcrClientTest("test_paper_cut_edu_vlm_create_task"))
    suite.addTest(OcrClientTest("test_paper_cut_edu_vlm_get_result"))
    suite.addTest(OcrClientTest("test_parser_task"))
    suite.addTest(OcrClientTest("test_parser_task_query"))
    suite.addTest(OcrClientTest("test_passport"))
    suite.addTest(OcrClientTest("test_qrcode"))
    suite.addTest(OcrClientTest("test_quota_invoice"))
    suite.addTest(OcrClientTest("test_real_estate_certificate"))
    suite.addTest(OcrClientTest("test_remove_handwriting"))
    suite.addTest(OcrClientTest("test_road_transport_certificate"))
    suite.addTest(OcrClientTest("test_seal"))
    suite.addTest(OcrClientTest("test_shopping_receipt"))
    suite.addTest(OcrClientTest("test_smart_struct"))
    suite.addTest(OcrClientTest("test_social_security_card"))
    suite.addTest(OcrClientTest("test_table"))
    suite.addTest(OcrClientTest("test_taxi_receipt"))
    suite.addTest(OcrClientTest("test_three_factors_verification"))
    suite.addTest(OcrClientTest("test_toll_invoice"))
    suite.addTest(OcrClientTest("test_train_ticket"))
    suite.addTest(OcrClientTest("test_two_factors_verification"))
    suite.addTest(OcrClientTest("test_used_vehicle_invoice"))
    suite.addTest(OcrClientTest("test_vat_invoice"))
    suite.addTest(OcrClientTest("test_vehicle_certificate"))
    suite.addTest(OcrClientTest("test_vehicle_invoice"))
    suite.addTest(OcrClientTest("test_vehicle_license"))
    suite.addTest(OcrClientTest("test_vehicle_reg_certificate"))
    suite.addTest(OcrClientTest("test_vehicle_registration_certificate"))
    suite.addTest(OcrClientTest("test_vin_code"))
    suite.addTest(OcrClientTest("test_waybill"))
    suite.addTest(OcrClientTest("test_web_image"))
    suite.addTest(OcrClientTest("test_web_image_loc"))
    suite.addTest(OcrClientTest("test_weight_note"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
