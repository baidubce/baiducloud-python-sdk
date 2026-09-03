"""
HslParams information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HslParams(AbstractModel):
    """
    HslParams
    """

    def __init__(self, hsl_brightness=None, hsl_saturation=None, hsl_gamut=None, hsl_hue=None):
        """
        Initialize HslParams instance.

        :param hsl_brightness:
        :type hsl_brightness: float (optional)

        :param hsl_saturation:
        :type hsl_saturation: float (optional)

        :param hsl_gamut: 色域选择：0-红、1-橙、2-黄、3-绿、4-青、5-蓝、6-紫、7-洋红
        :type hsl_gamut: int (optional)

        :param hsl_hue:
        :type hsl_hue: float (optional)
        """
        super().__init__()
        self.hsl_brightness = hsl_brightness
        self.hsl_saturation = hsl_saturation
        self.hsl_gamut = hsl_gamut
        self.hsl_hue = hsl_hue

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
        if self.hsl_brightness is not None:
            result['hsl_brightness'] = self.hsl_brightness
        if self.hsl_saturation is not None:
            result['hsl_saturation'] = self.hsl_saturation
        if self.hsl_gamut is not None:
            result['hsl_gamut'] = self.hsl_gamut
        if self.hsl_hue is not None:
            result['hsl_hue'] = self.hsl_hue
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HslParams

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('hsl_brightness') is not None:
            self.hsl_brightness = m.get('hsl_brightness')
        if m.get('hsl_saturation') is not None:
            self.hsl_saturation = m.get('hsl_saturation')
        if m.get('hsl_gamut') is not None:
            self.hsl_gamut = m.get('hsl_gamut')
        if m.get('hsl_hue') is not None:
            self.hsl_hue = m.get('hsl_hue')
        return self
