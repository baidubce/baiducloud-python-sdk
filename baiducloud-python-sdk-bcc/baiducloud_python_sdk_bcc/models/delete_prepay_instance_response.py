"""
Request entity for DeletePrepayInstanceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.instance_delete_result_model import InstanceDeleteResultModel
from baiducloud_python_sdk_bcc.models.instance_delete_result_model import InstanceDeleteResultModel


class DeletePrepayInstanceResponse(BceResponse):
    """
    DeletePrepayInstanceResponse
    """

    def __init__(self, success_resources=None, fail_resources=None, instance_refund_flag=None):
        """
        Initialize DeletePrepayInstanceResponse response.

        :param success_resources: success_resources field
        :type success_resources: InstanceDeleteResultModel (optional)

        :param fail_resources: fail_resources field
        :type fail_resources: InstanceDeleteResultModel (optional)

        :param instance_refund_flag: 实例是否成功释放
        :type instance_refund_flag: bool (optional)
        """
        super().__init__()
        self.success_resources = success_resources
        self.fail_resources = fail_resources
        self.instance_refund_flag = instance_refund_flag

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.success_resources is not None:
            result['successResources'] = self.success_resources.to_dict()
        if self.fail_resources is not None:
            result['failResources'] = self.fail_resources.to_dict()
        if self.instance_refund_flag is not None:
            result['instanceRefundFlag'] = self.instance_refund_flag
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeletePrepayInstanceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('successResources') is not None:
            self.success_resources = InstanceDeleteResultModel().from_dict(m.get('successResources'))
        if m.get('failResources') is not None:
            self.fail_resources = InstanceDeleteResultModel().from_dict(m.get('failResources'))
        if m.get('instanceRefundFlag') is not None:
            self.instance_refund_flag = m.get('instanceRefundFlag')
        return self
