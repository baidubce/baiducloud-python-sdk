"""
Example for nlp client.
"""

import copy
import logging

from baiducloud_python_sdk_core import utils, bce_base_client
from baiducloud_python_sdk_core.bce_base_client import BceBaseClient
from baiducloud_python_sdk_core.http import bce_http_client
from baiducloud_python_sdk_core.http import handler
from baiducloud_python_sdk_core.http import http_methods
from baiducloud_python_sdk_core.util import request_body_utils
from baiducloud_python_sdk_nlp.models.address_response import AddressResponse
from baiducloud_python_sdk_nlp.models.comment_tag_response import CommentTagResponse
from baiducloud_python_sdk_nlp.models.ecnet_response import EcnetResponse
from baiducloud_python_sdk_nlp.models.emotion_response import EmotionResponse
from baiducloud_python_sdk_nlp.models.entity_analysis_response import EntityAnalysisResponse
from baiducloud_python_sdk_nlp.models.keyword_response import KeywordResponse
from baiducloud_python_sdk_nlp.models.lexer_response import LexerResponse
from baiducloud_python_sdk_nlp.models.news_summary_response import NewsSummaryResponse
from baiducloud_python_sdk_nlp.models.sentiment_classify_response import SentimentClassifyResponse
from baiducloud_python_sdk_nlp.models.simnet_response import SimnetResponse
from baiducloud_python_sdk_nlp.models.text_correction_response import TextCorrectionResponse
from baiducloud_python_sdk_nlp.models.topic_response import TopicResponse
from baiducloud_python_sdk_nlp.models.txt_keywords_extraction_response import TxtKeywordsExtractionResponse
from baiducloud_python_sdk_nlp.models.txt_monet_response import TxtMonetResponse

_logger = logging.getLogger(__name__)


class NlpClient(BceBaseClient):
    """
    nlp base sdk client
    """

    CONSTANT_RPC = b'rpc'

    CONSTANT_2_0 = b'2.0'

    CONSTANT_NLP = b'nlp'

    CONSTANT_V2 = b'v2'

    CONSTANT_TEXT_CORRECTION = b'text_correction'

    CONSTANT_V1 = b'v1'

    CONSTANT_ECNET = b'ecnet'

    CONSTANT_ADDRESS = b'address'

    CONSTANT_NEWS_SUMMARY = b'news_summary'

    CONSTANT_COMMENT_TAG = b'comment_tag'

    CONSTANT_LEXER = b'lexer'

    CONSTANT_EMOTION = b'emotion'

    CONSTANT_TXT_KEYWORDS_EXTRACTION = b'txt_keywords_extraction'

    CONSTANT_TOPIC = b'topic'

    CONSTANT_TXT_MONET = b'txt_monet'

    CONSTANT_ENTITY_ANALYSIS = b'entity_analysis'

    CONSTANT_SENTIMENT_CLASSIFY = b'sentiment_classify'

    CONSTANT_KEYWORD = b'keyword'

    CONSTANT_SIMNET = b'simnet'

    def __init__(self, config=None):
        """
        Initialize the nlp client.

        :param config: Client configuration
        :type config: baidubce.BceClientConfiguration
        """
        bce_base_client.BceBaseClient.__init__(self, config)

    def address(self, request, config=None):
        """
        address

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing AddressResponse data
        :rtype: AddressResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_ADDRESS,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=AddressResponse,
        )

    def comment_tag(self, request, config=None):
        """
        comment_tag

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing CommentTagResponse data
        :rtype: CommentTagResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V2,
            NlpClient.CONSTANT_COMMENT_TAG,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=CommentTagResponse,
        )

    def ecnet(self, request, config=None):
        """
        ecnet

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing EcnetResponse data
        :rtype: EcnetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_ECNET,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=EcnetResponse,
        )

    def emotion(self, request, config=None):
        """
        emotion

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing EmotionResponse data
        :rtype: EmotionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_EMOTION,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=EmotionResponse,
        )

    def entity_analysis(self, request, config=None):
        """
        entity_analysis

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing EntityAnalysisResponse data
        :rtype: EntityAnalysisResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_ENTITY_ANALYSIS,
        )
        headers = None
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            config=merged_config,
            model=EntityAnalysisResponse,
        )

    def keyword(self, request, config=None):
        """
        keyword

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing KeywordResponse data
        :rtype: KeywordResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_KEYWORD,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=KeywordResponse,
        )

    def lexer(self, request, config=None):
        """
        lexer

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing LexerResponse data
        :rtype: LexerResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_LEXER,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=LexerResponse,
        )

    def news_summary(self, request, config=None):
        """
        news_summary

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing NewsSummaryResponse data
        :rtype: NewsSummaryResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_NEWS_SUMMARY,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=NewsSummaryResponse,
        )

    def sentiment_classify(self, request, config=None):
        """
        sentiment_classify

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SentimentClassifyResponse data
        :rtype: SentimentClassifyResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_SENTIMENT_CLASSIFY,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=SentimentClassifyResponse,
        )

    def simnet(self, request, config=None):
        """
        simnet

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing SimnetResponse data
        :rtype: SimnetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V2,
            NlpClient.CONSTANT_SIMNET,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=SimnetResponse,
        )

    def text_correction(self, request, config=None):
        """
        text_correction

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TextCorrectionResponse data
        :rtype: TextCorrectionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V2,
            NlpClient.CONSTANT_TEXT_CORRECTION,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=TextCorrectionResponse,
        )

    def topic(self, request, config=None):
        """
        topic

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TopicResponse data
        :rtype: TopicResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_TOPIC,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=TopicResponse,
        )

    def txt_keywords_extraction(self, request, config=None):
        """
        txt_keywords_extraction

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TxtKeywordsExtractionResponse data
        :rtype: TxtKeywordsExtractionResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_TXT_KEYWORDS_EXTRACTION,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=TxtKeywordsExtractionResponse,
        )

    def txt_monet(self, request, config=None):
        """
        txt_monet

        :param request: Request entity containing all parameters
        :type request: NlpClientRequest
        :param config: Optional request configuration override
        :type config: baiducloud_python_sdk_core.BceClientConfiguration

        :return: API response containing TxtMonetResponse data
        :rtype: TxtMonetResponse

        :raises BceClientError: Client error (network failure, invalid parameters, etc.)
        :raises BceServerError: Server error (4xx/5xx HTTP status codes)
        """
        path = utils.append_uri(
            b'/',
            NlpClient.CONSTANT_RPC,
            NlpClient.CONSTANT_2_0,
            NlpClient.CONSTANT_NLP,
            NlpClient.CONSTANT_V1,
            NlpClient.CONSTANT_TXT_MONET,
        )
        headers = None
        params = {}
        if request.charset is not None:
            params['charset'] = request.charset
        merged_config = self._create_request_with_host(request, config)
        return self._send_request(
            http_methods.POST,
            path=path,
            body=request.to_json_string(),
            params=params,
            config=merged_config,
            model=TxtMonetResponse,
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
