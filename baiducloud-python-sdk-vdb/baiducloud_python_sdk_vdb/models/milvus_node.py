"""
MilvusNode information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MilvusNode(AbstractModel):
    """
    MilvusNode
    """

    def __init__(
        self,
        availability_zone=None,
        component_type=None,
        fixed_ip=None,
        floating_ip=None,
        node_id=None,
        port=None,
        status=None,
    ):
        """
        Initialize MilvusNode instance.

        :param availability_zone:
        :type availability_zone: str (optional)

        :param component_type:
        :type component_type: str (optional)

        :param fixed_ip:
        :type fixed_ip: str (optional)

        :param floating_ip:
        :type floating_ip: str (optional)

        :param node_id:
        :type node_id: str (optional)

        :param port:
        :type port: int (optional)

        :param status:
        :type status: str (optional)
        """
        super().__init__()
        self.availability_zone = availability_zone
        self.component_type = component_type
        self.fixed_ip = fixed_ip
        self.floating_ip = floating_ip
        self.node_id = node_id
        self.port = port
        self.status = status

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
        if self.availability_zone is not None:
            result['availabilityZone'] = self.availability_zone
        if self.component_type is not None:
            result['componentType'] = self.component_type
        if self.fixed_ip is not None:
            result['fixedIp'] = self.fixed_ip
        if self.floating_ip is not None:
            result['floatingIp'] = self.floating_ip
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.port is not None:
            result['port'] = self.port
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MilvusNode

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('availabilityZone') is not None:
            self.availability_zone = m.get('availabilityZone')
        if m.get('componentType') is not None:
            self.component_type = m.get('componentType')
        if m.get('fixedIp') is not None:
            self.fixed_ip = m.get('fixedIp')
        if m.get('floatingIp') is not None:
            self.floating_ip = m.get('floatingIp')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
