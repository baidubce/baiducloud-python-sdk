"""
BccBidFlavors information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BccBidFlavors(AbstractModel):
    """
    BccBidFlavors
    """

    def __init__(self, spec_id=None, cpu_count=None, memory_capacity_in_gb=None, product_type=None, spec=None):
        """
        Initialize BccBidFlavors instance.

        :param spec_id: 规格族ID
        :type spec_id: str (optional)

        :param cpu_count: CPU核数
        :type cpu_count: int (optional)

        :param memory_capacity_in_gb: 内存容量，单位GB
        :type memory_capacity_in_gb: int (optional)

        :param product_type: 产品类型
        :type product_type: str (optional)

        :param spec: 实例规格
        :type spec: str (optional)
        """
        super().__init__()
        self.spec_id = spec_id
        self.cpu_count = cpu_count
        self.memory_capacity_in_gb = memory_capacity_in_gb
        self.product_type = product_type
        self.spec = spec

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
        if self.spec_id is not None:
            result['specId'] = self.spec_id
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count
        if self.memory_capacity_in_gb is not None:
            result['memoryCapacityInGB'] = self.memory_capacity_in_gb
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.spec is not None:
            result['spec'] = self.spec
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BccBidFlavors

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('specId') is not None:
            self.spec_id = m.get('specId')
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')
        if m.get('memoryCapacityInGB') is not None:
            self.memory_capacity_in_gb = m.get('memoryCapacityInGB')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        return self
