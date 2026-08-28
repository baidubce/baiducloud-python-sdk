"""
OnlineTaxiItineraryWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.online_taxi_itinerary_item import OnlineTaxiItineraryItem


class OnlineTaxiItineraryWordsResult(AbstractModel):
    """
    OnlineTaxiItineraryWordsResult
    """

    def __init__(
        self,
        service_provider=None,
        start_time=None,
        end_time=None,
        phone=None,
        application_date=None,
        total_fare=None,
        item_num=None,
        service_type=None,
        items=None,
    ):
        """
        Initialize OnlineTaxiItineraryWordsResult instance.

        :param service_provider: 服务商
        :type service_provider: str (optional)

        :param start_time: 行程开始时间
        :type start_time: str (optional)

        :param end_time: 行程结束时间
        :type end_time: str (optional)

        :param phone: 行程人手机号
        :type phone: str (optional)

        :param application_date: 申请日期
        :type application_date: str (optional)

        :param total_fare: 总金额
        :type total_fare: str (optional)

        :param item_num: 行程信息中包含的行程数量
        :type item_num: str (optional)

        :param service_type: 服务类型
        :type service_type: str (optional)

        :param items: 行程信息
        :type items: List[OnlineTaxiItineraryItem] (optional)
        """
        super().__init__()
        self.service_provider = service_provider
        self.start_time = start_time
        self.end_time = end_time
        self.phone = phone
        self.application_date = application_date
        self.total_fare = total_fare
        self.item_num = item_num
        self.service_type = service_type
        self.items = items

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
        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.application_date is not None:
            result['ApplicationDate'] = self.application_date
        if self.total_fare is not None:
            result['TotalFare'] = self.total_fare
        if self.item_num is not None:
            result['ItemNum'] = self.item_num
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.items is not None:
            result['items'] = [i.to_dict() for i in self.items]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OnlineTaxiItineraryWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ApplicationDate') is not None:
            self.application_date = m.get('ApplicationDate')
        if m.get('TotalFare') is not None:
            self.total_fare = m.get('TotalFare')
        if m.get('ItemNum') is not None:
            self.item_num = m.get('ItemNum')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('items') is not None:
            self.items = [OnlineTaxiItineraryItem().from_dict(i) for i in m.get('items')]
        return self
