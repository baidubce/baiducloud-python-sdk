"""
Request entity for CreateInstanceBySpecResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreateInstanceBySpecResponse(BceResponse):
    """
    CreateInstanceBySpecResponse
    """

    def __init__(self, order_id=None, instance_ids=None, warning_list=None):
        """
        Initialize CreateInstanceBySpecResponse response.

        :param order_id: 订单ID
        :type order_id: str (optional)

        :param instance_ids: instance_ids field
        :type instance_ids: List[str] (optional)

        :param warning_list: 创建虚机产生的warning信息
        :type warning_list: List[str] (optional)
        """
        super().__init__()
        self.order_id = order_id
        self.instance_ids = instance_ids
        self.warning_list = warning_list

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
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.warning_list is not None:
            result['warningList'] = self.warning_list
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateInstanceBySpecResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('warningList') is not None:
            self.warning_list = m.get('warningList')
        return self
