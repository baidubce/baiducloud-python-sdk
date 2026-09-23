"""
Request entity for AddressResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class AddressResponse(BceResponse):
    """
    AddressResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        text=None,
        province=None,
        province_code=None,
        city=None,
        city_code=None,
        county=None,
        county_code=None,
        town=None,
        town_code=None,
        person=None,
        detail=None,
        phonenum=None,
        lat=None,
        lng=None,
    ):
        """
        Initialize AddressResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 请求唯一标识码
        :type log_id: int (optional)

        :param text: 原始输入的文本内容
        :type text: str (optional)

        :param province: 省（直辖市/自治区）
        :type province: str (optional)

        :param province_code: 省国标code
        :type province_code: str (optional)

        :param city: 市
        :type city: str (optional)

        :param city_code: 城市国标code
        :type city_code: str (optional)

        :param county: 区（县）
        :type county: str (optional)

        :param county_code: 区县国标code
        :type county_code: str (optional)

        :param town: 街道（乡/镇）
        :type town: str (optional)

        :param town_code: 街道/乡镇国标code
        :type town_code: str (optional)

        :param person: 姓名
        :type person: str (optional)

        :param detail: 详细地址
        :type detail: str (optional)

        :param phonenum: 电话号码
        :type phonenum: str (optional)

        :param lat: 纬度（百度坐标，仅供参考）
        :type lat: float (optional)

        :param lng: 经度（百度坐标，仅供参考）
        :type lng: float (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.text = text
        self.province = province
        self.province_code = province_code
        self.city = city
        self.city_code = city_code
        self.county = county
        self.county_code = county_code
        self.town = town
        self.town_code = town_code
        self.person = person
        self.detail = detail
        self.phonenum = phonenum
        self.lat = lat
        self.lng = lng

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.log_id is not None:
            result['log_id'] = self.log_id
        if self.text is not None:
            result['text'] = self.text
        if self.province is not None:
            result['province'] = self.province
        if self.province_code is not None:
            result['province_code'] = self.province_code
        if self.city is not None:
            result['city'] = self.city
        if self.city_code is not None:
            result['city_code'] = self.city_code
        if self.county is not None:
            result['county'] = self.county
        if self.county_code is not None:
            result['county_code'] = self.county_code
        if self.town is not None:
            result['town'] = self.town
        if self.town_code is not None:
            result['town_code'] = self.town_code
        if self.person is not None:
            result['person'] = self.person
        if self.detail is not None:
            result['detail'] = self.detail
        if self.phonenum is not None:
            result['phonenum'] = self.phonenum
        if self.lat is not None:
            result['lat'] = self.lat
        if self.lng is not None:
            result['lng'] = self.lng
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddressResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('log_id') is not None:
            self.log_id = m.get('log_id')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('province_code') is not None:
            self.province_code = m.get('province_code')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')
        if m.get('county') is not None:
            self.county = m.get('county')
        if m.get('county_code') is not None:
            self.county_code = m.get('county_code')
        if m.get('town') is not None:
            self.town = m.get('town')
        if m.get('town_code') is not None:
            self.town_code = m.get('town_code')
        if m.get('person') is not None:
            self.person = m.get('person')
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('phonenum') is not None:
            self.phonenum = m.get('phonenum')
        if m.get('lat') is not None:
            self.lat = m.get('lat')
        if m.get('lng') is not None:
            self.lng = m.get('lng')
        return self
