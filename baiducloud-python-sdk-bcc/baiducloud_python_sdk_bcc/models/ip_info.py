"""
IpInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IpInfo(AbstractModel):
    """
    IpInfo
    """

    def __init__(
        self,
        private_ip=None,
        eip=None,
        primary=None,
        eip_id=None,
        eip_allocation_id=None,
        eip_size=None,
        eip_status=None,
        eip_group_id=None,
        eip_type=None,
    ):
        """
        Initialize IpInfo instance.

        :param private_ip: 内网IP地址
        :type private_ip: str (optional)

        :param eip: 公网IP地址
        :type eip: str (optional)

        :param primary: 是否为主IP
        :type primary: str (optional)

        :param eip_id: 绑定的eip 长ID
        :type eip_id: str (optional)

        :param eip_allocation_id: eip 短ID
        :type eip_allocation_id: str (optional)

        :param eip_size: eip带宽峰值
        :type eip_size: str (optional)

        :param eip_status: eip状态
        :type eip_status: str (optional)

        :param eip_group_id: 共享带宽组ID
        :type eip_group_id: str (optional)

        :param eip_type: eip类型，shared表示共享带宽，normal表示普通eip
        :type eip_type: str (optional)
        """
        super().__init__()
        self.private_ip = private_ip
        self.eip = eip
        self.primary = primary
        self.eip_id = eip_id
        self.eip_allocation_id = eip_allocation_id
        self.eip_size = eip_size
        self.eip_status = eip_status
        self.eip_group_id = eip_group_id
        self.eip_type = eip_type

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
        if self.private_ip is not None:
            result['privateIp'] = self.private_ip
        if self.eip is not None:
            result['eip'] = self.eip
        if self.primary is not None:
            result['primary'] = self.primary
        if self.eip_id is not None:
            result['eipId'] = self.eip_id
        if self.eip_allocation_id is not None:
            result['eipAllocationId'] = self.eip_allocation_id
        if self.eip_size is not None:
            result['eipSize'] = self.eip_size
        if self.eip_status is not None:
            result['eipStatus'] = self.eip_status
        if self.eip_group_id is not None:
            result['eipGroupId'] = self.eip_group_id
        if self.eip_type is not None:
            result['eipType'] = self.eip_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IpInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('privateIp') is not None:
            self.private_ip = m.get('privateIp')
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('primary') is not None:
            self.primary = m.get('primary')
        if m.get('eipId') is not None:
            self.eip_id = m.get('eipId')
        if m.get('eipAllocationId') is not None:
            self.eip_allocation_id = m.get('eipAllocationId')
        if m.get('eipSize') is not None:
            self.eip_size = m.get('eipSize')
        if m.get('eipStatus') is not None:
            self.eip_status = m.get('eipStatus')
        if m.get('eipGroupId') is not None:
            self.eip_group_id = m.get('eipGroupId')
        if m.get('eipType') is not None:
            self.eip_type = m.get('eipType')
        return self
