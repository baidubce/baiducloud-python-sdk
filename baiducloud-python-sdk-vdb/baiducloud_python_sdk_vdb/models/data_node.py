"""
DataNode information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DataNode(AbstractModel):
    """
    DataNode
    """

    def __init__(self, fixed_ip=None, flavor_in_gb=None, floating_ip=None, node_show_id=None, port=None):
        """
        Initialize DataNode instance.

        :param fixed_ip:
        :type fixed_ip: str (optional)

        :param flavor_in_gb:
        :type flavor_in_gb: float (optional)

        :param floating_ip:
        :type floating_ip: str (optional)

        :param node_show_id:
        :type node_show_id: str (optional)

        :param port:
        :type port: int (optional)
        """
        super().__init__()
        self.fixed_ip = fixed_ip
        self.flavor_in_gb = flavor_in_gb
        self.floating_ip = floating_ip
        self.node_show_id = node_show_id
        self.port = port

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
        if self.fixed_ip is not None:
            result['fixedIp'] = self.fixed_ip
        if self.flavor_in_gb is not None:
            result['flavorInGB'] = self.flavor_in_gb
        if self.floating_ip is not None:
            result['floatingIp'] = self.floating_ip
        if self.node_show_id is not None:
            result['nodeShowID'] = self.node_show_id
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DataNode

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fixedIp') is not None:
            self.fixed_ip = m.get('fixedIp')
        if m.get('flavorInGB') is not None:
            self.flavor_in_gb = m.get('flavorInGB')
        if m.get('floatingIp') is not None:
            self.floating_ip = m.get('floatingIp')
        if m.get('nodeShowID') is not None:
            self.node_show_id = m.get('nodeShowID')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self
