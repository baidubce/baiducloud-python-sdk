"""
ReleaseResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReleaseResult(AbstractModel):
    """
    ReleaseResult
    """

    def __init__(self, sandbox_id=None, success=None, error=None):
        """
        Initialize ReleaseResult instance.

        :param sandbox_id: 沙箱实例 ID。
        :type sandbox_id: str (optional)

        :param success: 是否释放成功。
        :type success: bool (optional)

        :param error: 失败原因。
        :type error: str (optional)
        """
        super().__init__()
        self.sandbox_id = sandbox_id
        self.success = success
        self.error = error

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
        if self.sandbox_id is not None:
            result['sandboxId'] = self.sandbox_id
        if self.success is not None:
            result['success'] = self.success
        if self.error is not None:
            result['error'] = self.error
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReleaseResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sandboxId') is not None:
            self.sandbox_id = m.get('sandboxId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('error') is not None:
            self.error = m.get('error')
        return self
