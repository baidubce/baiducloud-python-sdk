import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.auth.api_key_credentials import ApiKeyCredentials
from baiducloud_python_sdk_core.auth.access_token_credentials import AccessTokenCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_nlp.api.nlp_client import NlpClient
from baiducloud_python_sdk_nlp import models as nlp_models


class NlpClientTest(unittest.TestCase):
    """NlpClient unit test stubs"""

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

        self.client = NlpClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_address(self):
        self.client.address(nlp_models.AddressRequest())

    def test_comment_tag(self):
        self.client.comment_tag(nlp_models.CommentTagRequest())

    def test_ecnet(self):
        self.client.ecnet(nlp_models.EcnetRequest())

    def test_emotion(self):
        self.client.emotion(nlp_models.EmotionRequest())

    def test_entity_analysis(self):
        self.client.entity_analysis(nlp_models.EntityAnalysisRequest())

    def test_keyword(self):
        self.client.keyword(nlp_models.KeywordRequest())

    def test_lexer(self):
        self.client.lexer(nlp_models.LexerRequest())

    def test_news_summary(self):
        self.client.news_summary(nlp_models.NewsSummaryRequest())

    def test_sentiment_classify(self):
        self.client.sentiment_classify(nlp_models.SentimentClassifyRequest())

    def test_simnet(self):
        self.client.simnet(nlp_models.SimnetRequest())

    def test_text_correction(self):
        self.client.text_correction(nlp_models.TextCorrectionRequest())

    def test_topic(self):
        self.client.topic(nlp_models.TopicRequest())

    def test_txt_keywords_extraction(self):
        self.client.txt_keywords_extraction(nlp_models.TxtKeywordsExtractionRequest())

    def test_txt_monet(self):
        self.client.txt_monet(nlp_models.TxtMonetRequest())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(NlpClientTest("test_address"))
    suite.addTest(NlpClientTest("test_comment_tag"))
    suite.addTest(NlpClientTest("test_ecnet"))
    suite.addTest(NlpClientTest("test_emotion"))
    suite.addTest(NlpClientTest("test_entity_analysis"))
    suite.addTest(NlpClientTest("test_keyword"))
    suite.addTest(NlpClientTest("test_lexer"))
    suite.addTest(NlpClientTest("test_news_summary"))
    suite.addTest(NlpClientTest("test_sentiment_classify"))
    suite.addTest(NlpClientTest("test_simnet"))
    suite.addTest(NlpClientTest("test_text_correction"))
    suite.addTest(NlpClientTest("test_topic"))
    suite.addTest(NlpClientTest("test_txt_keywords_extraction"))
    suite.addTest(NlpClientTest("test_txt_monet"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
