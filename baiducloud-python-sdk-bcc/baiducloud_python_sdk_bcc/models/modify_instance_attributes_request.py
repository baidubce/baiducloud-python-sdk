"""
Request entity for ModifyInstanceAttributesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyInstanceAttributesRequest(AbstractModel):
    """
    Request entity for ModifyInstanceAttributesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, name=None, enable_jumbo_frame=None, net_eth_queue_count=None):
        """
        Initialize ModifyInstanceAttributesRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param name: 实例名称，支持大小写字母、数字以及-_ /.特殊字符，必须以字母开头，长度1-65个字符。
        :type name: str (optional)

        :param enable_jumbo_frame: 是否开启Jumbo帧，开启:true，关闭:false。注意:只有支持Jumbo帧的套餐才能开启
        :type enable_jumbo_frame: bool (optional)

        :param net_eth_queue_count: 修改后的网卡队列数
        :type net_eth_queue_count: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.name = name
        self.enable_jumbo_frame = enable_jumbo_frame
        self.net_eth_queue_count = net_eth_queue_count

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.enable_jumbo_frame is not None:
            result['enableJumboFrame'] = self.enable_jumbo_frame
        if self.net_eth_queue_count is not None:
            result['netEthQueueCount'] = self.net_eth_queue_count
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyInstanceAttributesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('enableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('enableJumboFrame')
        if m.get('netEthQueueCount') is not None:
            self.net_eth_queue_count = m.get('netEthQueueCount')
        return self
