"""
Receiver information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Receiver(AbstractModel):
    """
    Receiver
    """

    def __init__(
        self,
        receivers_id=None,
        receivers_domain_id=None,
        receivers_name=None,
        receivers_email=None,
        receivers_phone=None,
    ):
        """
        Initialize Receiver instance.

        :param receivers_id: 用户/用户组ID
        :type receivers_id: str (optional)

        :param receivers_domain_id: 主账户对应的domainId
        :type receivers_domain_id: str (optional)

        :param receivers_name: 用户/用户组名称
        :type receivers_name: str (optional)

        :param receivers_email: 用户配置的邮箱
        :type receivers_email: str (optional)

        :param receivers_phone: 用户配置的电话号码
        :type receivers_phone: str (optional)
        """
        super().__init__()
        self.receivers_id = receivers_id
        self.receivers_domain_id = receivers_domain_id
        self.receivers_name = receivers_name
        self.receivers_email = receivers_email
        self.receivers_phone = receivers_phone

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
        if self.receivers_id is not None:
            result['receivers.id'] = self.receivers_id
        if self.receivers_domain_id is not None:
            result['receivers.domainId'] = self.receivers_domain_id
        if self.receivers_name is not None:
            result['receivers.name'] = self.receivers_name
        if self.receivers_email is not None:
            result['receivers.email'] = self.receivers_email
        if self.receivers_phone is not None:
            result['receivers.phone'] = self.receivers_phone
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Receiver

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('receivers.id') is not None:
            self.receivers_id = m.get('receivers.id')
        if m.get('receivers.domainId') is not None:
            self.receivers_domain_id = m.get('receivers.domainId')
        if m.get('receivers.name') is not None:
            self.receivers_name = m.get('receivers.name')
        if m.get('receivers.email') is not None:
            self.receivers_email = m.get('receivers.email')
        if m.get('receivers.phone') is not None:
            self.receivers_phone = m.get('receivers.phone')
        return self
