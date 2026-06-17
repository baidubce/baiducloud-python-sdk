"""
ResourceBo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.config_item import ConfigItem


class ResourceBo(AbstractModel):
    """
    ResourceBo
    """

    def __init__(
        self,
        id=None,
        serial_number=None,
        name=None,
        recycle_time=None,
        delete_time=None,
        payment_timing=None,
        service_name=None,
        service_type=None,
        config_item=None,
        config_items=None,
    ):
        """
        Initialize ResourceBo instance.

        :param id: 实例ID
        :type id: str (optional)

        :param serial_number: 实例长ID
        :type serial_number: str (optional)

        :param name: 实例名称
        :type name: str (optional)

        :param recycle_time: 进入回收站的时间
        :type recycle_time: str (optional)

        :param delete_time: 从回收站删除的时间
        :type delete_time: str (optional)

        :param payment_timing: 付费类型 prepay/postpay
        :type payment_timing: str (optional)

        :param service_name: 资源名称，这里为\"云服务器\"
        :type service_name: str (optional)

        :param service_type: 资源类型，这里为\"BCC\"
        :type service_type: str (optional)

        :param config_item: config_item attribute
        :type config_item: ConfigItem (optional)

        :param config_items: 实例配置列表
        :type config_items: List[str] (optional)
        """
        super().__init__()
        self.id = id
        self.serial_number = serial_number
        self.name = name
        self.recycle_time = recycle_time
        self.delete_time = delete_time
        self.payment_timing = payment_timing
        self.service_name = service_name
        self.service_type = service_type
        self.config_item = config_item
        self.config_items = config_items

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
        if self.id is not None:
            result['id'] = self.id
        if self.serial_number is not None:
            result['serialNumber'] = self.serial_number
        if self.name is not None:
            result['name'] = self.name
        if self.recycle_time is not None:
            result['recycleTime'] = self.recycle_time
        if self.delete_time is not None:
            result['deleteTime'] = self.delete_time
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.config_item is not None:
            result['configItem'] = self.config_item.to_dict()
        if self.config_items is not None:
            result['configItems'] = self.config_items
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResourceBo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('serialNumber') is not None:
            self.serial_number = m.get('serialNumber')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('recycleTime') is not None:
            self.recycle_time = m.get('recycleTime')
        if m.get('deleteTime') is not None:
            self.delete_time = m.get('deleteTime')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('configItem') is not None:
            self.config_item = ConfigItem().from_dict(m.get('configItem'))
        if m.get('configItems') is not None:
            self.config_items = m.get('configItems')
        return self
