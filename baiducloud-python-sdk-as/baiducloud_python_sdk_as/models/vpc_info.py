"""
VpcInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VpcInfo(AbstractModel):
    """
    VpcInfo
    """

    def __init__(self, vpc_name=None, vpc_id=None, vpc_uuid=None):
        """
        Initialize VpcInfo instance.

        :param vpc_name: 子网名称
        :type vpc_name: str (optional)

        :param vpc_id: 子网id
        :type vpc_id: str (optional)

        :param vpc_uuid: 子网uuid
        :type vpc_uuid: str (optional)
        """
        super().__init__()
        self.vpc_name = vpc_name
        self.vpc_id = vpc_id
        self.vpc_uuid = vpc_uuid

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
        if self.vpc_name is not None:
            result['vpcName'] = self.vpc_name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_uuid is not None:
            result['vpcUuid'] = self.vpc_uuid
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VpcInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcName') is not None:
            self.vpc_name = m.get('vpcName')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcUuid') is not None:
            self.vpc_uuid = m.get('vpcUuid')
        return self
