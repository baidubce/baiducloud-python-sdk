"""
Request entity for GetPackageListV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GetPackageListV2Request(AbstractModel):
    """
    Request entity for GetPackageListV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, type=None, machine_spec_list=None):
        """
        Initialize GetPackageListV2Request request entity.

        :param type: type parameter
        :type type: str (optional)

        :param machine_spec_list: 查询指定套餐
        :type machine_spec_list: List[str] (optional)
        """
        super().__init__()
        self.type = type
        self.machine_spec_list = machine_spec_list

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
        if self.machine_spec_list is not None:
            result['machineSpecList'] = self.machine_spec_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetPackageListV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('machineSpecList') is not None:
            self.machine_spec_list = m.get('machineSpecList')
        return self
