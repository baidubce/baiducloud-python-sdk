"""
ACLEntry information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ACLEntry(AbstractModel):
    """
    ACLEntry
    """

    def __init__(self, service=None, region=None, resource=None, permission=None, effect=None):
        """
        Initialize ACLEntry instance.

        :param service: service attribute
        :type service: str (optional)

        :param region: 固定值， \"global\"
        :type region: str (optional)

        :param resource: 资源，具体格式看产品线
        :type resource: List[str] (optional)

        :param permission: 权限,具体格式看产品线
        :type permission: List[str] (optional)

        :param effect: 固定值，\"Allow\"
        :type effect: str (optional)
        """
        super().__init__()
        self.service = service
        self.region = region
        self.resource = resource
        self.permission = permission
        self.effect = effect

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
        if self.service is not None:
            result['service'] = self.service
        if self.region is not None:
            result['region'] = self.region
        if self.resource is not None:
            result['resource'] = self.resource
        if self.permission is not None:
            result['permission'] = self.permission
        if self.effect is not None:
            result['effect'] = self.effect
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ACLEntry

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        if m.get('permission') is not None:
            self.permission = m.get('permission')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        return self
