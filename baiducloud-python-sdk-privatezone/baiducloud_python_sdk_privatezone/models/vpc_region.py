"""
VpcRegion information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VpcRegion(AbstractModel):
    """
    VpcRegion
    """

    def __init__(self, region=None, vpc_ids=None):
        """
        Initialize VpcRegion instance.

        :param region: VPC 所在的地区
        :type region: str (optional)

        :param vpc_ids: VPC 的 id 列表
        :type vpc_ids: List[str] (optional)
        """
        super().__init__()
        self.region = region
        self.vpc_ids = vpc_ids

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
        if self.vpc_ids is not None:
            result['vpcIds'] = self.vpc_ids
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VpcRegion

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('vpcIds') is not None:
            self.vpc_ids = m.get('vpcIds')
        return self
