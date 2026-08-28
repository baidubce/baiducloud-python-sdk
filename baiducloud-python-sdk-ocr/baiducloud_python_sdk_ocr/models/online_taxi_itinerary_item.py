"""
OnlineTaxiItineraryItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OnlineTaxiItineraryItem(AbstractModel):
    """
    OnlineTaxiItineraryItem
    """

    def __init__(
        self,
        item_id=None,
        pickup_time=None,
        pickup_date=None,
        car_type=None,
        distance=None,
        start_place=None,
        destination_place=None,
        city=None,
        fare=None,
        item_provider=None,
    ):
        """
        Initialize OnlineTaxiItineraryItem instance.

        :param item_id: 行程信息的对应序号
        :type item_id: str (optional)

        :param pickup_time: 上车时间
        :type pickup_time: str (optional)

        :param pickup_date: 上车日期
        :type pickup_date: str (optional)

        :param car_type: 车型
        :type car_type: str (optional)

        :param distance: 里程
        :type distance: str (optional)

        :param start_place: 起点
        :type start_place: str (optional)

        :param destination_place: 终点
        :type destination_place: str (optional)

        :param city: 城市
        :type city: str (optional)

        :param fare: 金额
        :type fare: str (optional)

        :param item_provider: 服务提供方
        :type item_provider: str (optional)
        """
        super().__init__()
        self.item_id = item_id
        self.pickup_time = pickup_time
        self.pickup_date = pickup_date
        self.car_type = car_type
        self.distance = distance
        self.start_place = start_place
        self.destination_place = destination_place
        self.city = city
        self.fare = fare
        self.item_provider = item_provider

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
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.pickup_time is not None:
            result['PickupTime'] = self.pickup_time
        if self.pickup_date is not None:
            result['PickupDate'] = self.pickup_date
        if self.car_type is not None:
            result['CarType'] = self.car_type
        if self.distance is not None:
            result['Distance'] = self.distance
        if self.start_place is not None:
            result['StartPlace'] = self.start_place
        if self.destination_place is not None:
            result['DestinationPlace'] = self.destination_place
        if self.city is not None:
            result['City'] = self.city
        if self.fare is not None:
            result['Fare'] = self.fare
        if self.item_provider is not None:
            result['item_provider'] = self.item_provider
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OnlineTaxiItineraryItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('PickupTime') is not None:
            self.pickup_time = m.get('PickupTime')
        if m.get('PickupDate') is not None:
            self.pickup_date = m.get('PickupDate')
        if m.get('CarType') is not None:
            self.car_type = m.get('CarType')
        if m.get('Distance') is not None:
            self.distance = m.get('Distance')
        if m.get('StartPlace') is not None:
            self.start_place = m.get('StartPlace')
        if m.get('DestinationPlace') is not None:
            self.destination_place = m.get('DestinationPlace')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Fare') is not None:
            self.fare = m.get('Fare')
        if m.get('item_provider') is not None:
            self.item_provider = m.get('item_provider')
        return self
