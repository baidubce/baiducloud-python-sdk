"""
ExceptionDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ExceptionDetail(AbstractModel):
    """
    ExceptionDetail
    """

    def __init__(self, id=None, stacktrace=None, service=None):
        """
        Initialize ExceptionDetail instance.

        :param id: 异常ID
        :type id: str (optional)

        :param stacktrace: 异常堆栈
        :type stacktrace: str (optional)

        :param service: 异常所属服务
        :type service: str (optional)
        """
        super().__init__()
        self.id = id
        self.stacktrace = stacktrace
        self.service = service

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
        if self.id is not None:
            result['id'] = self.id
        if self.stacktrace is not None:
            result['stacktrace'] = self.stacktrace
        if self.service is not None:
            result['service'] = self.service
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ExceptionDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('stacktrace') is not None:
            self.stacktrace = m.get('stacktrace')
        if m.get('service') is not None:
            self.service = m.get('service')
        return self
