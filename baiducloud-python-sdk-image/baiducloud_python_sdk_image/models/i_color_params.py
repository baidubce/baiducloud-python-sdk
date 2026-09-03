"""
IColorParams information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_image.models.hsl_params import HslParams


class IColorParams(AbstractModel):
    """
    IColorParams
    """

    def __init__(
        self,
        shadow=None,
        smart_remove_fog=None,
        tint=None,
        skin_color_refresh=None,
        ai_color=None,
        smart_exposure=None,
        saturation=None,
        highlight=None,
        bg_enhance=None,
        white=None,
        sharpen_amount=None,
        temperature=None,
        lut_value=None,
        auto_whitebalance=None,
        sharpen_radius=None,
        black=None,
        hsl_params=None,
        auto_exposure=None,
        brightness=None,
        exposure=None,
        contrast=None,
        vibrance=None,
        smart_whitebalance=None,
        remove_fog=None,
        lut_id=None,
    ):
        """
        Initialize IColorParams instance.

        :param shadow: 阴影
        :type shadow: float (optional)

        :param smart_remove_fog: 智能去薄雾
        :type smart_remove_fog: float (optional)

        :param tint: 色调
        :type tint: float (optional)

        :param skin_color_refresh: 肤色优化
        :type skin_color_refresh: int (optional)

        :param ai_color: AI 调色总开关，0 关闭，1 开启
        :type ai_color: int (optional)

        :param smart_exposure: 智能曝光
        :type smart_exposure: float (optional)

        :param saturation: 饱和度
        :type saturation: float (optional)

        :param highlight: 高光
        :type highlight: float (optional)

        :param bg_enhance: 背景增强
        :type bg_enhance: float (optional)

        :param white: 白色
        :type white: float (optional)

        :param sharpen_amount: 细节数量
        :type sharpen_amount: float (optional)

        :param temperature: 色温
        :type temperature: float (optional)

        :param lut_value: LUT 滤镜程度值
        :type lut_value: float (optional)

        :param auto_whitebalance: 智能白平衡
        :type auto_whitebalance: float (optional)

        :param sharpen_radius: 细节半径
        :type sharpen_radius: float (optional)

        :param black: 黑色
        :type black: float (optional)

        :param hsl_params: HSL 参数数组
        :type hsl_params: List[HslParams] (optional)

        :param auto_exposure: 智能曝光
        :type auto_exposure: float (optional)

        :param brightness: 亮度
        :type brightness: float (optional)

        :param exposure: 曝光
        :type exposure: float (optional)

        :param contrast: 对比度
        :type contrast: float (optional)

        :param vibrance: 自然饱和度
        :type vibrance: float (optional)

        :param smart_whitebalance: 智能白平衡
        :type smart_whitebalance: float (optional)

        :param remove_fog: 去薄雾
        :type remove_fog: float (optional)

        :param lut_id: LUT 滤镜 ID
        :type lut_id: str (optional)
        """
        super().__init__()
        self.shadow = shadow
        self.smart_remove_fog = smart_remove_fog
        self.tint = tint
        self.skin_color_refresh = skin_color_refresh
        self.ai_color = ai_color
        self.smart_exposure = smart_exposure
        self.saturation = saturation
        self.highlight = highlight
        self.bg_enhance = bg_enhance
        self.white = white
        self.sharpen_amount = sharpen_amount
        self.temperature = temperature
        self.lut_value = lut_value
        self.auto_whitebalance = auto_whitebalance
        self.sharpen_radius = sharpen_radius
        self.black = black
        self.hsl_params = hsl_params
        self.auto_exposure = auto_exposure
        self.brightness = brightness
        self.exposure = exposure
        self.contrast = contrast
        self.vibrance = vibrance
        self.smart_whitebalance = smart_whitebalance
        self.remove_fog = remove_fog
        self.lut_id = lut_id

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
        if self.shadow is not None:
            result['shadow'] = self.shadow
        if self.smart_remove_fog is not None:
            result['smart_remove_fog'] = self.smart_remove_fog
        if self.tint is not None:
            result['tint'] = self.tint
        if self.skin_color_refresh is not None:
            result['skin_color_refresh'] = self.skin_color_refresh
        if self.ai_color is not None:
            result['ai_color'] = self.ai_color
        if self.smart_exposure is not None:
            result['smart_exposure'] = self.smart_exposure
        if self.saturation is not None:
            result['saturation'] = self.saturation
        if self.highlight is not None:
            result['highlight'] = self.highlight
        if self.bg_enhance is not None:
            result['bg_enhance'] = self.bg_enhance
        if self.white is not None:
            result['white'] = self.white
        if self.sharpen_amount is not None:
            result['sharpen_amount'] = self.sharpen_amount
        if self.temperature is not None:
            result['temperature'] = self.temperature
        if self.lut_value is not None:
            result['lut_value'] = self.lut_value
        if self.auto_whitebalance is not None:
            result['auto_whitebalance'] = self.auto_whitebalance
        if self.sharpen_radius is not None:
            result['sharpen_radius'] = self.sharpen_radius
        if self.black is not None:
            result['black'] = self.black
        if self.hsl_params is not None:
            result['hsl_params'] = [i.to_dict() for i in self.hsl_params]
        if self.auto_exposure is not None:
            result['auto_exposure'] = self.auto_exposure
        if self.brightness is not None:
            result['brightness'] = self.brightness
        if self.exposure is not None:
            result['exposure'] = self.exposure
        if self.contrast is not None:
            result['contrast'] = self.contrast
        if self.vibrance is not None:
            result['vibrance'] = self.vibrance
        if self.smart_whitebalance is not None:
            result['smart_whitebalance'] = self.smart_whitebalance
        if self.remove_fog is not None:
            result['remove_fog'] = self.remove_fog
        if self.lut_id is not None:
            result['lut_id'] = self.lut_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IColorParams

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('shadow') is not None:
            self.shadow = m.get('shadow')
        if m.get('smart_remove_fog') is not None:
            self.smart_remove_fog = m.get('smart_remove_fog')
        if m.get('tint') is not None:
            self.tint = m.get('tint')
        if m.get('skin_color_refresh') is not None:
            self.skin_color_refresh = m.get('skin_color_refresh')
        if m.get('ai_color') is not None:
            self.ai_color = m.get('ai_color')
        if m.get('smart_exposure') is not None:
            self.smart_exposure = m.get('smart_exposure')
        if m.get('saturation') is not None:
            self.saturation = m.get('saturation')
        if m.get('highlight') is not None:
            self.highlight = m.get('highlight')
        if m.get('bg_enhance') is not None:
            self.bg_enhance = m.get('bg_enhance')
        if m.get('white') is not None:
            self.white = m.get('white')
        if m.get('sharpen_amount') is not None:
            self.sharpen_amount = m.get('sharpen_amount')
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')
        if m.get('lut_value') is not None:
            self.lut_value = m.get('lut_value')
        if m.get('auto_whitebalance') is not None:
            self.auto_whitebalance = m.get('auto_whitebalance')
        if m.get('sharpen_radius') is not None:
            self.sharpen_radius = m.get('sharpen_radius')
        if m.get('black') is not None:
            self.black = m.get('black')
        if m.get('hsl_params') is not None:
            self.hsl_params = [HslParams().from_dict(i) for i in m.get('hsl_params')]
        if m.get('auto_exposure') is not None:
            self.auto_exposure = m.get('auto_exposure')
        if m.get('brightness') is not None:
            self.brightness = m.get('brightness')
        if m.get('exposure') is not None:
            self.exposure = m.get('exposure')
        if m.get('contrast') is not None:
            self.contrast = m.get('contrast')
        if m.get('vibrance') is not None:
            self.vibrance = m.get('vibrance')
        if m.get('smart_whitebalance') is not None:
            self.smart_whitebalance = m.get('smart_whitebalance')
        if m.get('remove_fog') is not None:
            self.remove_fog = m.get('remove_fog')
        if m.get('lut_id') is not None:
            self.lut_id = m.get('lut_id')
        return self
