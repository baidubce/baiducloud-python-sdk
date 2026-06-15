"""
Example for aihc client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.auth import bce_v1_signer
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_aihc.models.create_dataset_response import CreateDatasetResponse
from baiducloud_python_sdk_aihc.models.create_dataset_version_response import CreateDatasetVersionResponse
from baiducloud_python_sdk_aihc.models.create_model_response import CreateModelResponse
from baiducloud_python_sdk_aihc.models.create_model_version_response import CreateModelVersionResponse
from baiducloud_python_sdk_aihc.models.describe_dataset_response import DescribeDatasetResponse
from baiducloud_python_sdk_aihc.models.describe_dataset_version_response import DescribeDatasetVersionResponse
from baiducloud_python_sdk_aihc.models.describe_dataset_versions_response import DescribeDatasetVersionsResponse
from baiducloud_python_sdk_aihc.models.describe_datasets_response import DescribeDatasetsResponse
from baiducloud_python_sdk_aihc.models.describe_model_response import DescribeModelResponse
from baiducloud_python_sdk_aihc.models.describe_model_version_response import DescribeModelVersionResponse
from baiducloud_python_sdk_aihc.models.describe_model_versions_response import DescribeModelVersionsResponse
from baiducloud_python_sdk_aihc.models.describe_models_response import DescribeModelsResponse

_logger = logging.getLogger(__name__)


class AihcClient(BceBaseClient):
    """
    aihc base sdk client
    """

    def __init__(self, config=None):
        """
        Initialize the aihc client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def create_dataset(self, request, config=None):
        """
        create_dataset

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDatasetResponse data
        :rtype: CreateDatasetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'CreateDataset'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=CreateDatasetResponse,
        )

    def create_dataset_version(self, request, config=None):
        """
        create_dataset_version

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDatasetVersionResponse data
        :rtype: CreateDatasetVersionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'CreateDatasetVersion'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=CreateDatasetVersionResponse,
        )

    def create_model(self, request, config=None):
        """
        create_model

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateModelResponse data
        :rtype: CreateModelResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'CreateModel'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=CreateModelResponse,
        )

    def create_model_version(self, request, config=None):
        """
        create_model_version

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateModelVersionResponse data
        :rtype: CreateModelVersionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'CreateModelVersion'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
            model=CreateModelVersionResponse,
        )

    def delete_dataset(self, request, config=None):
        """
        delete_dataset

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DeleteDataset'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, headers=headers, params=params, config=merged_config)

    def delete_dataset_version(self, request, config=None):
        """
        delete_dataset_version

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DeleteDatasetVersion'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        if request.version_id is not None:
            params['versionId'] = request.version_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, headers=headers, params=params, config=merged_config)

    def delete_model(self, request, config=None):
        """
        delete_model

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DeleteModel'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, headers=headers, params=params, config=merged_config)

    def delete_model_version(self, request, config=None):
        """
        delete_model_version

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DeleteModelVersion'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        if request.version_id is not None:
            params['versionId'] = request.version_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, headers=headers, params=params, config=merged_config)

    def describe_dataset(self, request, config=None):
        """
        describe_dataset

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDatasetResponse data
        :rtype: DescribeDatasetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DescribeDataset'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            headers=headers,
            params=params,
            config=merged_config,
            model=DescribeDatasetResponse,
        )

    def describe_dataset_version(self, request, config=None):
        """
        describe_dataset_version

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDatasetVersionResponse data
        :rtype: DescribeDatasetVersionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DescribeDatasetVersion'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        if request.version_id is not None:
            params['versionId'] = request.version_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            headers=headers,
            params=params,
            config=merged_config,
            model=DescribeDatasetVersionResponse,
        )

    def describe_dataset_versions(self, request, config=None):
        """
        describe_dataset_versions

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDatasetVersionsResponse data
        :rtype: DescribeDatasetVersionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DescribeDatasetVersions'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        if request.page_number is not None:
            params['pageNumber'] = request.page_number
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            headers=headers,
            params=params,
            config=merged_config,
            model=DescribeDatasetVersionsResponse,
        )

    def describe_datasets(self, request, config=None):
        """
        describe_datasets

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeDatasetsResponse data
        :rtype: DescribeDatasetsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DescribeDatasets'
        if request.keyword is not None:
            params['keyword'] = request.keyword
        if request.storage_type is not None:
            params['storageType'] = request.storage_type
        if request.storage_instances is not None:
            params['storageInstances'] = request.storage_instances
        if request.import_format is not None:
            params['importFormat'] = request.import_format
        if request.page_number is not None:
            params['pageNumber'] = request.page_number
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            headers=headers,
            params=params,
            config=merged_config,
            model=DescribeDatasetsResponse,
        )

    def describe_model(self, request, config=None):
        """
        describe_model

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeModelResponse data
        :rtype: DescribeModelResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DescribeModel'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            headers=headers,
            params=params,
            config=merged_config,
            model=DescribeModelResponse,
        )

    def describe_model_version(self, request, config=None):
        """
        describe_model_version

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeModelVersionResponse data
        :rtype: DescribeModelVersionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DescribeModelVersion'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        if request.version_id is not None:
            params['versionId'] = request.version_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            headers=headers,
            params=params,
            config=merged_config,
            model=DescribeModelVersionResponse,
        )

    def describe_model_versions(self, request, config=None):
        """
        describe_model_versions

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeModelVersionsResponse data
        :rtype: DescribeModelVersionsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DescribeModelVersions'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        if request.page_number is not None:
            params['pageNumber'] = request.page_number
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            headers=headers,
            params=params,
            config=merged_config,
            model=DescribeModelVersionsResponse,
        )

    def describe_models(self, request, config=None):
        """
        describe_models

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing DescribeModelsResponse data
        :rtype: DescribeModelsResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'DescribeModels'
        if request.keyword is not None:
            params['keyword'] = request.keyword
        if request.page_number is not None:
            params['pageNumber'] = request.page_number
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET,
            path=path,
            headers=headers,
            params=params,
            config=merged_config,
            model=DescribeModelsResponse,
        )

    def modify_dataset(self, request, config=None):
        """
        modify_dataset

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'ModifyDataset'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
        )

    def modify_model(self, request, config=None):
        """
        modify_model

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response
        :rtype: baiducloud_python_sdk_core.bce_response.BceResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = {}
        headers[b'Version'] = b'v2'
        params = {}
        params['action'] = 'ModifyModel'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            headers=headers,
            params=params,
            config=merged_config,
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
        return bce_http_client.send_request(
            config,
            bce_v1_signer.sign,
            [handler.parse_error, body_parser],
            http_method,
            path,
            body,
            headers,
            params,
            model=model,
        )
