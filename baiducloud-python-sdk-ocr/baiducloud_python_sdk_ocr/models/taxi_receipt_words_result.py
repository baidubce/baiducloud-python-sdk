"""
TaxiReceiptWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TaxiReceiptWordsResult(AbstractModel):
    """
    TaxiReceiptWordsResult
    """

    def __init__(
        self,
        invoice_code=None,
        invoice_num=None,
        taxi_num=None,
        ocr_date=None,
        time=None,
        pickup_time=None,
        dropoff_time=None,
        fare=None,
        fuel_oil_surcharge=None,
        call_service_surcharge=None,
        total_fare=None,
        location=None,
        province=None,
        city=None,
        price_perkm=None,
        distance=None,
        service_type=None,
    ):
        """
        Initialize TaxiReceiptWordsResult instance.

        :param invoice_code: 发票代码
        :type invoice_code: str (optional)

        :param invoice_num: 发票号码
        :type invoice_num: str (optional)

        :param taxi_num: 车牌号
        :type taxi_num: str (optional)

        :param ocr_date: 日期
        :type ocr_date: str (optional)

        :param time: 上下车时间
        :type time: str (optional)

        :param pickup_time: 上车时间
        :type pickup_time: str (optional)

        :param dropoff_time: 下车时间
        :type dropoff_time: str (optional)

        :param fare: 金额
        :type fare: str (optional)

        :param fuel_oil_surcharge: 燃油附加费
        :type fuel_oil_surcharge: str (optional)

        :param call_service_surcharge: 叫车服务费
        :type call_service_surcharge: str (optional)

        :param total_fare: 总金额
        :type total_fare: str (optional)

        :param location: 开票城市
        :type location: str (optional)

        :param province: 省
        :type province: str (optional)

        :param city: 市
        :type city: str (optional)

        :param price_perkm: 单价
        :type price_perkm: str (optional)

        :param distance: 里程
        :type distance: str (optional)

        :param service_type: 服务类型
        :type service_type: str (optional)
        """
        super().__init__()
        self.invoice_code = invoice_code
        self.invoice_num = invoice_num
        self.taxi_num = taxi_num
        self.ocr_date = ocr_date
        self.time = time
        self.pickup_time = pickup_time
        self.dropoff_time = dropoff_time
        self.fare = fare
        self.fuel_oil_surcharge = fuel_oil_surcharge
        self.call_service_surcharge = call_service_surcharge
        self.total_fare = total_fare
        self.location = location
        self.province = province
        self.city = city
        self.price_perkm = price_perkm
        self.distance = distance
        self.service_type = service_type

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
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_num is not None:
            result['InvoiceNum'] = self.invoice_num
        if self.taxi_num is not None:
            result['TaxiNum'] = self.taxi_num
        if self.ocr_date is not None:
            result['Date'] = self.ocr_date
        if self.time is not None:
            result['Time'] = self.time
        if self.pickup_time is not None:
            result['PickupTime'] = self.pickup_time
        if self.dropoff_time is not None:
            result['DropoffTime'] = self.dropoff_time
        if self.fare is not None:
            result['Fare'] = self.fare
        if self.fuel_oil_surcharge is not None:
            result['FuelOilSurcharge'] = self.fuel_oil_surcharge
        if self.call_service_surcharge is not None:
            result['CallServiceSurcharge'] = self.call_service_surcharge
        if self.total_fare is not None:
            result['TotalFare'] = self.total_fare
        if self.location is not None:
            result['Location'] = self.location
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.price_perkm is not None:
            result['PricePerkm'] = self.price_perkm
        if self.distance is not None:
            result['Distance'] = self.distance
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TaxiReceiptWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNum') is not None:
            self.invoice_num = m.get('InvoiceNum')
        if m.get('TaxiNum') is not None:
            self.taxi_num = m.get('TaxiNum')
        if m.get('Date') is not None:
            self.ocr_date = m.get('Date')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('PickupTime') is not None:
            self.pickup_time = m.get('PickupTime')
        if m.get('DropoffTime') is not None:
            self.dropoff_time = m.get('DropoffTime')
        if m.get('Fare') is not None:
            self.fare = m.get('Fare')
        if m.get('FuelOilSurcharge') is not None:
            self.fuel_oil_surcharge = m.get('FuelOilSurcharge')
        if m.get('CallServiceSurcharge') is not None:
            self.call_service_surcharge = m.get('CallServiceSurcharge')
        if m.get('TotalFare') is not None:
            self.total_fare = m.get('TotalFare')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('PricePerkm') is not None:
            self.price_perkm = m.get('PricePerkm')
        if m.get('Distance') is not None:
            self.distance = m.get('Distance')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self
