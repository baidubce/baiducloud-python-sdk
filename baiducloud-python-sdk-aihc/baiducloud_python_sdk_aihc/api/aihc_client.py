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
from baiducloud_python_sdk_aihc.models.create_a_dataset_v2_response import CreateADatasetV2Response
from baiducloud_python_sdk_aihc.models.create_a_model_v2_response import CreateAModelV2Response
from baiducloud_python_sdk_aihc.models.create_dataset_version_v2_response import CreateDatasetVersionV2Response
from baiducloud_python_sdk_aihc.models.get_a_list_of_model_versions_v2_response import (
    GetAListOfModelVersionsV2Response,
)
from baiducloud_python_sdk_aihc.models.get_dataset_details_v2_response import GetDatasetDetailsV2Response
from baiducloud_python_sdk_aihc.models.get_dataset_version_details_v2_response import (
    GetDatasetVersionDetailsV2Response,
)
from baiducloud_python_sdk_aihc.models.get_model_details_v2_response import GetModelDetailsV2Response
from baiducloud_python_sdk_aihc.models.get_model_list_v2_response import GetModelListV2Response
from baiducloud_python_sdk_aihc.models.get_model_version_details_v2_response import GetModelVersionDetailsV2Response
from baiducloud_python_sdk_aihc.models.new_model_version_v2_response import NewModelVersionV2Response
from baiducloud_python_sdk_aihc.models.retrieve_the_dataset_list_v2_response import RetrieveTheDatasetListV2Response
from baiducloud_python_sdk_aihc.models.retrieve_the_dataset_version_list_v2_response import (
    RetrieveTheDatasetVersionListV2Response,
)

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

    def create_a_dataset_v2(self, request, config=None):
        """
        create_a_dataset_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateADatasetV2Response data
        :rtype: CreateADatasetV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'CreateDataset'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateADatasetV2Response,
        )

    def create_a_model_v2(self, request, config=None):
        """
        create_a_model_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateAModelV2Response data
        :rtype: CreateAModelV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'CreateModel'
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateAModelV2Response,
        )

    def create_dataset_version_v2(self, request, config=None):
        """
        create_dataset_version_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CreateDatasetVersionV2Response data
        :rtype: CreateDatasetVersionV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'CreateDatasetVersion'
        params['datasetId'] = 'xxx'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CreateDatasetVersionV2Response,
        )

    def delete_dataset_v2(self, request, config=None):
        """
        delete_dataset_v2

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
        headers = None
        params = {}
        params['action'] = 'DeleteDataset'
        params['datasetId'] = 'xxx'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def delete_dataset_version_v2(self, request, config=None):
        """
        delete_dataset_version_v2

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
        headers = None
        params = {}
        params['action'] = 'DeleteDatasetVersion'
        params['datasetId'] = 'xxx'
        params['versionId'] = 'xxx'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        if request.version_id is not None:
            params['versionId'] = request.version_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def delete_model_v2(self, request, config=None):
        """
        delete_model_v2

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
        headers = None
        params = {}
        params['action'] = 'DeleteModel'
        params['modelId'] = 'xxx'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def delete_model_version_v2(self, request, config=None):
        """
        delete_model_version_v2

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
        headers = None
        params = {}
        params['action'] = 'DeleteModelVersion'
        params['modelId'] = 'xxx'
        params['versionId'] = 'xxx'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        if request.version_id is not None:
            params['versionId'] = request.version_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(http_methods.POST, path=path, params=params, config=merged_config)

    def get_a_list_of_model_versions_v2(self, request, config=None):
        """
        get_a_list_of_model_versions_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetAListOfModelVersionsV2Response data
        :rtype: GetAListOfModelVersionsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'DescribeModelVersions'
        params['modelId'] = 'xxx'
        params['pageNumber'] = 'xxx'
        params['pageSize'] = 'xxx'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        if request.page_number is not None:
            params['pageNumber'] = request.page_number
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetAListOfModelVersionsV2Response
        )

    def get_dataset_details_v2(self, request, config=None):
        """
        get_dataset_details_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetDatasetDetailsV2Response data
        :rtype: GetDatasetDetailsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'DescribeDataset'
        params['datasetId'] = 'xxx'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetDatasetDetailsV2Response
        )

    def get_dataset_version_details_v2(self, request, config=None):
        """
        get_dataset_version_details_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetDatasetVersionDetailsV2Response data
        :rtype: GetDatasetVersionDetailsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'DescribeDatasetVersion'
        params['datasetId'] = 'xxx'
        params['versionId'] = 'xxx'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        if request.version_id is not None:
            params['versionId'] = request.version_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetDatasetVersionDetailsV2Response
        )

    def get_model_details_v2(self, request, config=None):
        """
        get_model_details_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetModelDetailsV2Response data
        :rtype: GetModelDetailsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'DescribeModel'
        params['modelId'] = 'xxx'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetModelDetailsV2Response
        )

    def get_model_list_v2(self, request, config=None):
        """
        get_model_list_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetModelListV2Response data
        :rtype: GetModelListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'DescribeModels'
        params['keyword'] = 'xxx'
        params['pageNumber'] = 'xxx'
        params['pageSize'] = 'xxx'
        if request.page_number is not None:
            params['pageNumber'] = request.page_number
        if request.page_size is not None:
            params['pageSize'] = request.page_size
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetModelListV2Response
        )

    def get_model_version_details_v2(self, request, config=None):
        """
        get_model_version_details_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing GetModelVersionDetailsV2Response data
        :rtype: GetModelVersionDetailsV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'DescribeModelVersion'
        params['modelId'] = 'xxx'
        params['versionId'] = 'xxx'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        if request.version_id is not None:
            params['versionId'] = request.version_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.GET, path=path, params=params, config=merged_config, model=GetModelVersionDetailsV2Response
        )

    def modify_dataset_v2(self, request, config=None):
        """
        modify_dataset_v2

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
        headers = None
        params = {}
        params['action'] = 'ModifyDataset'
        params['datasetId'] = 'xxx'
        if request.dataset_id is not None:
            params['datasetId'] = request.dataset_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def modify_the_model_v2(self, request, config=None):
        """
        modify_the_model_v2

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
        headers = None
        params = {}
        params['action'] = 'ModifyModel'
        params['modelId'] = 'xxx'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST, path=path, body=request.to_json_string(), params=params, config=merged_config
        )

    def new_model_version_v2(self, request, config=None):
        """
        new_model_version_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing NewModelVersionV2Response data
        :rtype: NewModelVersionV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'CreateModelVersion'
        params['modelId'] = 'xxx'
        if request.model_id is not None:
            params['modelId'] = request.model_id
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=NewModelVersionV2Response,
        )

    def retrieve_the_dataset_list_v2(self, request, config=None):
        """
        retrieve_the_dataset_list_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RetrieveTheDatasetListV2Response data
        :rtype: RetrieveTheDatasetListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'DescribeDatasets'
        params['keyword'] = 'xxx'
        params['storageType'] = 'xxx'
        params['storageInstances'] = 'xxx'
        params['importFormat'] = 'xxx'
        params['pageNumber'] = 'xxx'
        params['pageSize'] = 'xxx'
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
            http_methods.GET, path=path, params=params, config=merged_config, model=RetrieveTheDatasetListV2Response
        )

    def retrieve_the_dataset_version_list_v2(self, request, config=None):
        """
        retrieve_the_dataset_version_list_v2

        :param request: Request entity containing all parameters
        :type request: AihcClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing RetrieveTheDatasetVersionListV2Response data
        :rtype: RetrieveTheDatasetVersionListV2Response

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = b'/'
        headers = None
        params = {}
        params['action'] = 'DescribeDatasetVersions'
        params['datasetId'] = 'xxx'
        params['pageNumber'] = 'xxx'
        params['pageSize'] = 'xxx'
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
            params=params,
            config=merged_config,
            model=RetrieveTheDatasetVersionListV2Response,
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
