"""
Request entity for ListAvailableResizeSpecRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ListAvailableResizeSpecRequest(AbstractModel):
    """
    Request entity for ListAvailableResizeSpecRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, spec=None, spec_id=None, zone=None, instance_id_list=None):
        """
        Initialize ListAvailableResizeSpecRequest request entity.

        :param spec: 实例规格。实例规格、规格族ID和实例ID有且只能传一个。
        :type spec: str (optional)

        :param spec_id: 规格族ID。实例规格、规格族ID和实例ID有且只能传一个。
        :type spec_id: str (optional)

        :param zone: zone parameter
        :type zone: str (optional)

        :param instance_id_list: 实例ID列表。实例规格、规格族ID和实例ID有且只能传一个。
        :type instance_id_list: List[str] (optional)
        """
        super().__init__()
        self.spec = spec
        self.spec_id = spec_id
        self.zone = zone
        self.instance_id_list = instance_id_list

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
        if self.spec_id is not None:
            result['specId'] = self.spec_id
        if self.zone is not None:
            result['zone'] = self.zone
        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListAvailableResizeSpecRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('specId') is not None:
            self.spec_id = m.get('specId')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')
        return self
