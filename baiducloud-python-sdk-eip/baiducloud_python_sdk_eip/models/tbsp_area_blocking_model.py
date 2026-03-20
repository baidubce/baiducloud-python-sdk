"""
TbspAreaBlockingModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspAreaBlockingModel(AbstractModel):
    """
    TbspAreaBlockingModel
    """

    def __init__(self, ip=None, block_area=None, block_begin_time=None, block_end_time=None, block_type=None):
        """
        Initialize TbspAreaBlockingModel instance.

        :param ip: DDoS增强防护包防护对象IP地址
        :type ip: str (optional)

        :param block_area: DDoS增强防护包防护对象封禁区域，包含大陆地区 (continent) 和海外及港澳台地区 (overseas)
        :type block_area: str (optional)

        :param block_begin_time: DDoS增强防护包防护对象区域封禁起始时间
        :type block_begin_time: str (optional)

        :param block_end_time: DDoS增强防护包防护对象区域封禁终止时间
        :type block_end_time: str (optional)

        :param block_type: DDoS增强防护包防护对象区域封禁类型
        :type block_type: str (optional)
        """
        super().__init__()
        self.ip = ip
        self.block_area = block_area
        self.block_begin_time = block_begin_time
        self.block_end_time = block_end_time
        self.block_type = block_type

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.block_area is not None:
            result['blockArea'] = self.block_area
        if self.block_begin_time is not None:
            result['blockBeginTime'] = self.block_begin_time
        if self.block_end_time is not None:
            result['blockEndTime'] = self.block_end_time
        if self.block_type is not None:
            result['blockType'] = self.block_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TbspAreaBlockingModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('blockArea') is not None:
            self.block_area = m.get('blockArea')
        if m.get('blockBeginTime') is not None:
            self.block_begin_time = m.get('blockBeginTime')
        if m.get('blockEndTime') is not None:
            self.block_end_time = m.get('blockEndTime')
        if m.get('blockType') is not None:
            self.block_type = m.get('blockType')
        return self
