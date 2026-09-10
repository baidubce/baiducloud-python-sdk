"""
Request entity for GetPackageListV2Response information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_cce.models.machine_spec_status import MachineSpecStatus


class GetPackageListV2Response(BceResponse):
    """
    GetPackageListV2Response
    """

    def __init__(self, machine_spec_list=None):
        """
        Initialize GetPackageListV2Response response.

        :param machine_spec_list: 套餐列表
        :type machine_spec_list: List[MachineSpecStatus] (optional)
        """
        super().__init__()
        self.machine_spec_list = machine_spec_list

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
        if self.machine_spec_list is not None:
            result['machineSpecList'] = [i.to_dict() for i in self.machine_spec_list]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPackageListV2Response

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('machineSpecList') is not None:
            self.machine_spec_list = [MachineSpecStatus().from_dict(i) for i in m.get('machineSpecList')]
        return self
