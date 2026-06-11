"""
RemoteCopyResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoteCopyResult(AbstractModel):
    """
    RemoteCopyResult
    """

    def __init__(self, region=None, image_id=None, code=None, err_msg=None):
        """
        Initialize RemoteCopyResult instance.

        :param region: 目标地域
        :type region: str (optional)

        :param image_id: 目标地域生成的镜像ID
        :type image_id: str (optional)

        :param code: 结果状态，success/failed
        :type code: str (optional)

        :param err_msg: 结果消息，成功为\"success\"，失败为错误信息
        :type err_msg: str (optional)
        """
        super().__init__()
        self.region = region
        self.image_id = image_id
        self.code = code
        self.err_msg = err_msg

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.code is not None:
            result['code'] = self.code
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoteCopyResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        return self
