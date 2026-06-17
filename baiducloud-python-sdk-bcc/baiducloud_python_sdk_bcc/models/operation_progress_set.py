"""
OperationProgressSet information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OperationProgressSet(AbstractModel):
    """
    OperationProgressSet
    """

    def __init__(self, resource_id=None, operation_status=None, code=None, error_message=None):
        """
        Initialize OperationProgressSet instance.

        :param resource_id: 资源ID
        :type resource_id: str (optional)

        :param operation_status: 操作状态
        :type operation_status: str (optional)

        :param code: 响应码
        :type code: str (optional)

        :param error_message: 错误信息
        :type error_message: str (optional)
        """
        super().__init__()
        self.resource_id = resource_id
        self.operation_status = operation_status
        self.code = code
        self.error_message = error_message

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
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.operation_status is not None:
            result['operationStatus'] = self.operation_status
        if self.code is not None:
            result['code'] = self.code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OperationProgressSet

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('operationStatus') is not None:
            self.operation_status = m.get('operationStatus')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        return self
