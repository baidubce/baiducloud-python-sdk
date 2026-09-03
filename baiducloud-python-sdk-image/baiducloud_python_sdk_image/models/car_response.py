"""
Request entity for CarResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_image.models.car_result import CarResult
from baiducloud_python_sdk_image.models.car_location_result import CarLocationResult


class CarResponse(BceResponse):
    """
    CarResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        color_result=None,
        result=None,
        brand=None,
        location_result=None,
    ):
        """
        Initialize CarResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param color_result: 车身颜色。共11种颜色，分别为白色、黑色、灰色、香槟色、黄色、红色、绿色、紫色、橙色、棕色、蓝色
        :type color_result: str (optional)

        :param result: 车型识别结果数组
        :type result: List[CarResult] (optional)

        :param brand: 车型品牌，实例：宝马；当output_brand=true时返回
        :type brand: str (optional)

        :param location_result: location_result field
        :type location_result: CarLocationResult (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.color_result = color_result
        self.result = result
        self.brand = brand
        self.location_result = location_result

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
        if self.color_result is not None:
            result['color_result'] = self.color_result
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        if self.brand is not None:
            result['brand'] = self.brand
        if self.location_result is not None:
            result['location_result'] = self.location_result.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CarResponse

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
        if m.get('color_result') is not None:
            self.color_result = m.get('color_result')
        if m.get('result') is not None:
            self.result = [CarResult().from_dict(i) for i in m.get('result')]
        if m.get('brand') is not None:
            self.brand = m.get('brand')
        if m.get('location_result') is not None:
            self.location_result = CarLocationResult().from_dict(m.get('location_result'))
        return self
