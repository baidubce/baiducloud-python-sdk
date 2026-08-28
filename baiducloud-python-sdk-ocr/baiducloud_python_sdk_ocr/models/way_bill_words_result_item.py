"""
WayBillWordsResultItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.image_info import ImageInfo

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem

from baiducloud_python_sdk_ocr.models.waybill_word_item import WaybillWordItem


class WayBillWordsResultItem(AbstractModel):
    """
    WayBillWordsResultItem
    """

    def __init__(
        self,
        image_info=None,
        bar_code=None,
        waybill_number=None,
        three_segment_code=None,
        recipient_name=None,
        sender_name=None,
        recipient_addr=None,
        sender_addr=None,
        recipient_phone=None,
        sender_phone=None,
        virtual_number=None,
        virtual_number_last=None,
        is_virtual_waybill=None,
    ):
        """
        Initialize WayBillWordsResultItem instance.

        :param image_info: image_info attribute
        :type image_info: ImageInfo (optional)

        :param bar_code: 条形码
        :type bar_code: List[WaybillWordItem] (optional)

        :param waybill_number: 快递运单号
        :type waybill_number: List[WaybillWordItem] (optional)

        :param three_segment_code: 三段码
        :type three_segment_code: List[WaybillWordItem] (optional)

        :param recipient_name: 收件人姓名
        :type recipient_name: List[WaybillWordItem] (optional)

        :param sender_name: 寄件人姓名
        :type sender_name: List[WaybillWordItem] (optional)

        :param recipient_addr: 收件人地址
        :type recipient_addr: List[WaybillWordItem] (optional)

        :param sender_addr: 寄件人地址
        :type sender_addr: List[WaybillWordItem] (optional)

        :param recipient_phone: 收件人电话
        :type recipient_phone: List[WaybillWordItem] (optional)

        :param sender_phone: 寄件人电话
        :type sender_phone: List[WaybillWordItem] (optional)

        :param virtual_number: 虚拟面单号，当请求参数is_identify_virtual_waybill=true时返回该字段
        :type virtual_number: List[WaybillWordItem] (optional)

        :param virtual_number_last: 隐私面单的4位转接号，当请求参数is_identify_virtual_waybill=true时返回该字段
        :type virtual_number_last: List[WaybillWordItem] (optional)

        :param is_virtual_waybill: is_virtual_waybill attribute
        :type is_virtual_waybill: List[WaybillWordItem] (optional)
        """
        super().__init__()
        self.image_info = image_info
        self.bar_code = bar_code
        self.waybill_number = waybill_number
        self.three_segment_code = three_segment_code
        self.recipient_name = recipient_name
        self.sender_name = sender_name
        self.recipient_addr = recipient_addr
        self.sender_addr = sender_addr
        self.recipient_phone = recipient_phone
        self.sender_phone = sender_phone
        self.virtual_number = virtual_number
        self.virtual_number_last = virtual_number_last
        self.is_virtual_waybill = is_virtual_waybill

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
        if self.image_info is not None:
            result['image_info'] = self.image_info.to_dict()
        if self.bar_code is not None:
            result['bar_code'] = [i.to_dict() for i in self.bar_code]
        if self.waybill_number is not None:
            result['waybill_number'] = [i.to_dict() for i in self.waybill_number]
        if self.three_segment_code is not None:
            result['three_segment_code'] = [i.to_dict() for i in self.three_segment_code]
        if self.recipient_name is not None:
            result['recipient_name'] = [i.to_dict() for i in self.recipient_name]
        if self.sender_name is not None:
            result['sender_name'] = [i.to_dict() for i in self.sender_name]
        if self.recipient_addr is not None:
            result['recipient_addr'] = [i.to_dict() for i in self.recipient_addr]
        if self.sender_addr is not None:
            result['sender_addr'] = [i.to_dict() for i in self.sender_addr]
        if self.recipient_phone is not None:
            result['recipient_phone'] = [i.to_dict() for i in self.recipient_phone]
        if self.sender_phone is not None:
            result['sender_phone'] = [i.to_dict() for i in self.sender_phone]
        if self.virtual_number is not None:
            result['virtual_number'] = [i.to_dict() for i in self.virtual_number]
        if self.virtual_number_last is not None:
            result['virtual_number_last'] = [i.to_dict() for i in self.virtual_number_last]
        if self.is_virtual_waybill is not None:
            result['is_virtual_waybill'] = [i.to_dict() for i in self.is_virtual_waybill]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: WayBillWordsResultItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image_info') is not None:
            self.image_info = ImageInfo().from_dict(m.get('image_info'))
        if m.get('bar_code') is not None:
            self.bar_code = [WaybillWordItem().from_dict(i) for i in m.get('bar_code')]
        if m.get('waybill_number') is not None:
            self.waybill_number = [WaybillWordItem().from_dict(i) for i in m.get('waybill_number')]
        if m.get('three_segment_code') is not None:
            self.three_segment_code = [WaybillWordItem().from_dict(i) for i in m.get('three_segment_code')]
        if m.get('recipient_name') is not None:
            self.recipient_name = [WaybillWordItem().from_dict(i) for i in m.get('recipient_name')]
        if m.get('sender_name') is not None:
            self.sender_name = [WaybillWordItem().from_dict(i) for i in m.get('sender_name')]
        if m.get('recipient_addr') is not None:
            self.recipient_addr = [WaybillWordItem().from_dict(i) for i in m.get('recipient_addr')]
        if m.get('sender_addr') is not None:
            self.sender_addr = [WaybillWordItem().from_dict(i) for i in m.get('sender_addr')]
        if m.get('recipient_phone') is not None:
            self.recipient_phone = [WaybillWordItem().from_dict(i) for i in m.get('recipient_phone')]
        if m.get('sender_phone') is not None:
            self.sender_phone = [WaybillWordItem().from_dict(i) for i in m.get('sender_phone')]
        if m.get('virtual_number') is not None:
            self.virtual_number = [WaybillWordItem().from_dict(i) for i in m.get('virtual_number')]
        if m.get('virtual_number_last') is not None:
            self.virtual_number_last = [WaybillWordItem().from_dict(i) for i in m.get('virtual_number_last')]
        if m.get('is_virtual_waybill') is not None:
            self.is_virtual_waybill = [WaybillWordItem().from_dict(i) for i in m.get('is_virtual_waybill')]
        return self
