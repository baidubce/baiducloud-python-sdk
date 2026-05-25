"""
IpCollectionBindedInstance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IpCollectionBindedInstance(AbstractModel):
    """
    IpCollectionBindedInstance
    """

    def __init__(self, instance_id=None, instance_type=None):
        """
        Initialize IpCollectionBindedInstance instance.

        :param instance_id: 参数模板绑定的实例ID
        :type instance_id: str (optional)

        :param instance_type: 参数模板绑定的实例类型，目前暂时仅\"ESG\"，表示企业安全组
        :type instance_type: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.instance_type = instance_type

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
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IpCollectionBindedInstance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        return self
