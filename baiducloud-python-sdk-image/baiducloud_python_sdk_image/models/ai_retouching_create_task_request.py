"""
Request entity for AiRetouchingCreateTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_image.models.i_color_params import IColorParams
from baiducloud_python_sdk_image.models.all_human_options import AllHumanOptions
from baiducloud_python_sdk_image.models.partial_human_options import PartialHumanOptions
from baiducloud_python_sdk_image.models.partial_templates import PartialTemplates
from baiducloud_python_sdk_image.models.transform_options import TransformOptions


class AiRetouchingCreateTaskRequest(AbstractModel):
    """
    Request entity for AiRetouchingCreateTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image=None,
        url=None,
        callback_data=None,
        i_color_params=None,
        all_human_options=None,
        partial_human_options=None,
        partial_templates=None,
        transform_options=None,
    ):
        """
        Initialize AiRetouchingCreateTaskRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param callback_data: 回调透传参数
        :type callback_data: str (optional)

        :param i_color_params: i_color_params parameter
        :type i_color_params: IColorParams (optional)

        :param all_human_options: all_human_options parameter
        :type all_human_options: AllHumanOptions (optional)

        :param partial_human_options: partial_human_options parameter
        :type partial_human_options: PartialHumanOptions (optional)

        :param partial_templates: partial_templates parameter
        :type partial_templates: PartialTemplates (optional)

        :param transform_options: transform_options parameter
        :type transform_options: TransformOptions (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.callback_data = callback_data
        self.i_color_params = i_color_params
        self.all_human_options = all_human_options
        self.partial_human_options = partial_human_options
        self.partial_templates = partial_templates
        self.transform_options = transform_options

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.url is not None:
            result['url'] = self.url
        if self.callback_data is not None:
            result['callback_data'] = self.callback_data
        if self.i_color_params is not None:
            result['IColorParams'] = self.i_color_params.to_dict()
        if self.all_human_options is not None:
            result['AllHumanOptions'] = self.all_human_options.to_dict()
        if self.partial_human_options is not None:
            result['PartialHumanOptions'] = self.partial_human_options.to_dict()
        if self.partial_templates is not None:
            result['PartialTemplates'] = self.partial_templates.to_dict()
        if self.transform_options is not None:
            result['transform_options'] = self.transform_options.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AiRetouchingCreateTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('callback_data') is not None:
            self.callback_data = m.get('callback_data')
        if m.get('IColorParams') is not None:
            self.i_color_params = IColorParams().from_dict(m.get('IColorParams'))
        if m.get('AllHumanOptions') is not None:
            self.all_human_options = AllHumanOptions().from_dict(m.get('AllHumanOptions'))
        if m.get('PartialHumanOptions') is not None:
            self.partial_human_options = PartialHumanOptions().from_dict(m.get('PartialHumanOptions'))
        if m.get('PartialTemplates') is not None:
            self.partial_templates = PartialTemplates().from_dict(m.get('PartialTemplates'))
        if m.get('transform_options') is not None:
            self.transform_options = TransformOptions().from_dict(m.get('transform_options'))
        return self
