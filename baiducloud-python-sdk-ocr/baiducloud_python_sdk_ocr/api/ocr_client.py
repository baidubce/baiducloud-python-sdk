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
from baiducloud_python_sdk_ocr.models.health_report_response import HealthReportResponse
from baiducloud_python_sdk_ocr.models.medical_detail_response import MedicalDetailResponse
from baiducloud_python_sdk_ocr.models.medical_invoice_response import MedicalInvoiceResponse
from baiducloud_python_sdk_ocr.models.medical_prescription_response import MedicalPrescriptionResponse
from baiducloud_python_sdk_ocr.models.medical_record_response import MedicalRecordResponse
from baiducloud_python_sdk_ocr.models.medical_report_detection_response import MedicalReportDetectionResponse
from baiducloud_python_sdk_ocr.models.medical_statement_response import MedicalStatementResponse
from baiducloud_python_sdk_ocr.models.medical_summary_response import MedicalSummaryResponse

_logger = logging.getLogger(__name__)


class OcrClient(BceBaseClient):
    """
    ocr base sdk client
    """

    CONSTANT_REST = b'rest'

    CONSTANT_2_0 = b'2.0'

    CONSTANT_OCR = b'ocr'

    CONSTANT_V1 = b'v1'

    CONSTANT_MEDICAL_SUMMARY = b'medical_summary'

    CONSTANT_MEDICAL_STATEMENT = b'medical_statement'

    CONSTANT_MEDICAL_PRESCRIPTION = b'medical_prescription'

    CONSTANT_MEDICAL_INVOICE = b'medical_invoice'

    CONSTANT_MEDICAL_RECORD = b'medical_record'

    CONSTANT_HEALTH_REPORT = b'health_report'

    CONSTANT_MEDICAL_DETAIL = b'medical_detail'

    CONSTANT_MEDICAL_REPORT_DETECTION = b'medical_report_detection'

    def __init__(self, config=None):
        """
        Initialize the ocr client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

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
