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

    def test_health_report(self):
        self.client.health_report(ocr_models.HealthReportRequest())

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


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(OcrClientTest("test_health_report"))
    suite.addTest(OcrClientTest("test_medical_detail"))
    suite.addTest(OcrClientTest("test_medical_invoice"))
    suite.addTest(OcrClientTest("test_medical_prescription"))
    suite.addTest(OcrClientTest("test_medical_record"))
    suite.addTest(OcrClientTest("test_medical_report_detection"))
    suite.addTest(OcrClientTest("test_medical_statement"))
    suite.addTest(OcrClientTest("test_medical_summary"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
