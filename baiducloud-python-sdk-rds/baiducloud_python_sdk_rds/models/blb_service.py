"""
BlbService information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BlbService(AbstractModel):
    """
    BlbService
    """

    def __init__(self, status=None, service=None):
        """
        Initialize BlbService instance.

        :param status: status attribute
        :type status: str (optional)

        :param service: 服务的域名。
        :type service: str (optional)
        """
        super().__init__()
        self.status = status
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
        if self.status is not None:
            result['status'] = self.status
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
        :rtype: BlbService

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('service') is not None:
            self.service = m.get('service')
        return self
