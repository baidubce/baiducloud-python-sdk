"""
PostpayConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PostpayConfig(AbstractModel):
    """
    PostpayConfig
    """

    def __init__(self, instance_id=None, cds_list=None, effective_type=None):
        """
        Initialize PostpayConfig instance.

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param cds_list: cds_list attribute
        :type cds_list: List[str] (optional)

        :param effective_type: effective_type attribute
        :type effective_type: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.cds_list = cds_list
        self.effective_type = effective_type

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.cds_list is not None:
            result['cdsList'] = self.cds_list
        if self.effective_type is not None:
            result['effectiveType'] = self.effective_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PostpayConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('cdsList') is not None:
            self.cds_list = m.get('cdsList')
        if m.get('effectiveType') is not None:
            self.effective_type = m.get('effectiveType')
        return self
