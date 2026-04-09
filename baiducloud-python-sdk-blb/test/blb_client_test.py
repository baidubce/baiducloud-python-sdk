import unittest

from baiducloud_python_sdk_core.auth.bce_credentials import BceCredentials
from baiducloud_python_sdk_core.bce_client_configuration import BceClientConfiguration
from baiducloud_python_sdk_blb.api.blb_client import BlbClient
from baiducloud_python_sdk_blb.models.billing import Billing
from baiducloud_python_sdk_blb.models.blb_inquiry_request import BlbInquiryRequest
from baiducloud_python_sdk_blb.models.reservation import Reservation


class BlbClientTest(unittest.TestCase):
    """BlbClient unit test stubs"""

    def setUp(self):
        """
        set up
        """
        HOST = b''
        AK = b''
        SK = b''
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = BlbClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_billing_change_cancel_to_post_blb(self):
        self.client.billing_change_cancel_to_post_blb(None)

    def test_billing_change_post_to_pre_blb(self):
        self.client.billing_change_post_to_pre_blb(None)

    def test_billing_change_pre_to_post_blb(self):
        self.client.billing_change_pre_to_post_blb(None)

    def test_blb_inquiry(self):
        request = BlbInquiryRequest(
            blb_type='ipv6Application',
            performance_level='small1',
            count=1,
            billing=Billing(
                payment_timing='Prepaid',
                reservation=Reservation(reservation_length=1),
            ),
        )
        response = self.client.blb_inquiry(request)
        print('metadata:', response.metadata)
        print('prices:', response.prices)
        if response.prices:
            for p in response.prices:
                print(' -', p.to_dict())

    def test_refund_blb(self):
        self.client.refund_blb(None)

    def test_resize_blb(self):
        self.client.resize_blb(None)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(BlbClientTest("test_billing_change_cancel_to_post_blb"))
    suite.addTest(BlbClientTest("test_billing_change_post_to_pre_blb"))
    suite.addTest(BlbClientTest("test_billing_change_pre_to_post_blb"))
    suite.addTest(BlbClientTest("test_blb_inquiry"))
    suite.addTest(BlbClientTest("test_refund_blb"))
    suite.addTest(BlbClientTest("test_resize_blb"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
