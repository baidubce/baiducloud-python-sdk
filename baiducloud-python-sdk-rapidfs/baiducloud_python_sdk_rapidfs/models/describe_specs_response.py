"""
Request entity for DescribeSpecsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.instance_spec_info import InstanceSpecInfo


class DescribeSpecsResponse(BceResponse):
    """
    DescribeSpecsResponse
    """

    def __init__(self, instance_spec_infos=None):
        """
        Initialize DescribeSpecsResponse response.

        :param instance_spec_infos: RapidFS 缓存实例规格信息，见附录 InstanceSpecInfo
        :type instance_spec_infos: List[InstanceSpecInfo] (optional)
        """
        super().__init__()
        self.instance_spec_infos = instance_spec_infos

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.instance_spec_infos is not None:
            result['instanceSpecInfos'] = [i.to_dict() for i in self.instance_spec_infos]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeSpecsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceSpecInfos') is not None:
            self.instance_spec_infos = [InstanceSpecInfo().from_dict(i) for i in m.get('instanceSpecInfos')]
        return self
