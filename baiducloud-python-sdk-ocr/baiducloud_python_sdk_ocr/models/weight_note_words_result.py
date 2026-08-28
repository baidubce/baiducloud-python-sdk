"""
WeightNoteWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.weight_note_word_item import WeightNoteWordItem

from baiducloud_python_sdk_ocr.models.weight_note_word_item import WeightNoteWordItem

from baiducloud_python_sdk_ocr.models.weight_note_word_item import WeightNoteWordItem

from baiducloud_python_sdk_ocr.models.weight_note_word_item import WeightNoteWordItem

from baiducloud_python_sdk_ocr.models.weight_note_word_item import WeightNoteWordItem

from baiducloud_python_sdk_ocr.models.weight_note_word_item import WeightNoteWordItem

from baiducloud_python_sdk_ocr.models.weight_note_word_item import WeightNoteWordItem

from baiducloud_python_sdk_ocr.models.weight_note_word_item import WeightNoteWordItem


class WeightNoteWordsResult(AbstractModel):
    """
    WeightNoteWordsResult
    """

    def __init__(
        self,
        plate_num=None,
        print_time=None,
        cross_weight=None,
        tare_weight=None,
        net_weight=None,
        sending_company=None,
        receiving_company=None,
        delivery_number=None,
    ):
        """
        Initialize WeightNoteWordsResult instance.

        :param plate_num: 车牌号
        :type plate_num: List[WeightNoteWordItem] (optional)

        :param print_time: 打印时间
        :type print_time: List[WeightNoteWordItem] (optional)

        :param cross_weight: 毛重
        :type cross_weight: List[WeightNoteWordItem] (optional)

        :param tare_weight: 皮重
        :type tare_weight: List[WeightNoteWordItem] (optional)

        :param net_weight: 净重
        :type net_weight: List[WeightNoteWordItem] (optional)

        :param sending_company: 发货单位
        :type sending_company: List[WeightNoteWordItem] (optional)

        :param receiving_company: 收货单位
        :type receiving_company: List[WeightNoteWordItem] (optional)

        :param delivery_number: 单号
        :type delivery_number: List[WeightNoteWordItem] (optional)
        """
        super().__init__()
        self.plate_num = plate_num
        self.print_time = print_time
        self.cross_weight = cross_weight
        self.tare_weight = tare_weight
        self.net_weight = net_weight
        self.sending_company = sending_company
        self.receiving_company = receiving_company
        self.delivery_number = delivery_number

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
        if self.plate_num is not None:
            result['PlateNum'] = [i.to_dict() for i in self.plate_num]
        if self.print_time is not None:
            result['PrintTime'] = [i.to_dict() for i in self.print_time]
        if self.cross_weight is not None:
            result['CrossWeight'] = [i.to_dict() for i in self.cross_weight]
        if self.tare_weight is not None:
            result['TareWeight'] = [i.to_dict() for i in self.tare_weight]
        if self.net_weight is not None:
            result['NetWeight'] = [i.to_dict() for i in self.net_weight]
        if self.sending_company is not None:
            result['SendingCompany'] = [i.to_dict() for i in self.sending_company]
        if self.receiving_company is not None:
            result['ReceivingCompany'] = [i.to_dict() for i in self.receiving_company]
        if self.delivery_number is not None:
            result['DeliveryNumber'] = [i.to_dict() for i in self.delivery_number]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: WeightNoteWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('PlateNum') is not None:
            self.plate_num = [WeightNoteWordItem().from_dict(i) for i in m.get('PlateNum')]
        if m.get('PrintTime') is not None:
            self.print_time = [WeightNoteWordItem().from_dict(i) for i in m.get('PrintTime')]
        if m.get('CrossWeight') is not None:
            self.cross_weight = [WeightNoteWordItem().from_dict(i) for i in m.get('CrossWeight')]
        if m.get('TareWeight') is not None:
            self.tare_weight = [WeightNoteWordItem().from_dict(i) for i in m.get('TareWeight')]
        if m.get('NetWeight') is not None:
            self.net_weight = [WeightNoteWordItem().from_dict(i) for i in m.get('NetWeight')]
        if m.get('SendingCompany') is not None:
            self.sending_company = [WeightNoteWordItem().from_dict(i) for i in m.get('SendingCompany')]
        if m.get('ReceivingCompany') is not None:
            self.receiving_company = [WeightNoteWordItem().from_dict(i) for i in m.get('ReceivingCompany')]
        if m.get('DeliveryNumber') is not None:
            self.delivery_number = [WeightNoteWordItem().from_dict(i) for i in m.get('DeliveryNumber')]
        return self
