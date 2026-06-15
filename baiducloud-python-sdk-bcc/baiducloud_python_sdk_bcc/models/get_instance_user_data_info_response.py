"""
Request entity for GetInstanceUserDataInfoResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetInstanceUserDataInfoResponse(BceResponse):
    """
    GetInstanceUserDataInfoResponse
    """

    def __init__(self, user_data=None, instance_id=None):
        """
        Initialize GetInstanceUserDataInfoResponse response.

        :param user_data: 最近一次自定义脚本内容（使用base64编码）
        :type user_data: str (optional)

        :param instance_id: 实例短ID
        :type instance_id: str (optional)
        """
        super().__init__()
        self.user_data = user_data
        self.instance_id = instance_id

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
        if self.user_data is not None:
            result['userData'] = self.user_data
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetInstanceUserDataInfoResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('userData') is not None:
            self.user_data = m.get('userData')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self
