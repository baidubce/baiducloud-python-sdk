"""
ErrTemplate information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.template import Template


class ErrTemplate(AbstractModel):
    """
    ErrTemplate
    """

    def __init__(self, index=None, template=None, message=None):
        """
        Initialize ErrTemplate instance.

        :param index: 标识第几条模板，从0开始计数
        :type index: int (optional)

        :param template: template attribute
        :type template: Template (optional)

        :param message: 错误详情
        :type message: str (optional)
        """
        super().__init__()
        self.index = index
        self.template = template
        self.message = message

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
        if self.index is not None:
            result['index'] = self.index
        if self.template is not None:
            result['template'] = self.template.to_dict()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ErrTemplate

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('template') is not None:
            self.template = Template().from_dict(m.get('template'))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self
