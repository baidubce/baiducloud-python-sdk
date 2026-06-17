"""
Request entity for InstanceBatchResizeBySpecRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceBatchResizeBySpecRequest(AbstractModel):
    """
    Request entity for InstanceBatchResizeBySpecRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, spec, instance_id_list, enable_jumbo_frame=None, subnet_id=None, logical_zone=None):
        """
        Initialize InstanceBatchResizeBySpecRequest request entity.

        :param spec: 批量变配的实例规格
        :type spec: str (required)

        :param instance_id_list: 实例id组成的集合，最多30个
        :type instance_id_list: List[str] (required)

        :param enable_jumbo_frame: enable_jumbo_frame parameter
        :type enable_jumbo_frame: bool (optional)

        :param subnet_id: 子网id
        :type subnet_id: str (optional)

        :param logical_zone: 逻辑可用区标识
        :type logical_zone: str (optional)
        """
        super().__init__()
        self.spec = spec
        self.instance_id_list = instance_id_list
        self.enable_jumbo_frame = enable_jumbo_frame
        self.subnet_id = subnet_id
        self.logical_zone = logical_zone

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.spec is not None:
            result['spec'] = self.spec
        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list
        if self.enable_jumbo_frame is not None:
            result['enableJumboFrame'] = self.enable_jumbo_frame
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.logical_zone is not None:
            result['logicalZone'] = self.logical_zone
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceBatchResizeBySpecRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')
        if m.get('enableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('enableJumboFrame')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('logicalZone') is not None:
            self.logical_zone = m.get('logicalZone')
        return self
