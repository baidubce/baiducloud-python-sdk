"""
HandwritingGetEssayResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.handwriting_get_essay_overall import HandwritingGetEssayOverall

from baiducloud_python_sdk_ocr.models.title import Title

from baiducloud_python_sdk_ocr.models.handwriting_composition_get_result_content import (
    HandwritingCompositionGetResultContent,
)


class HandwritingGetEssayResult(AbstractModel):
    """
    HandwritingGetEssayResult
    """

    def __init__(
        self, recognize_granularity=None, grade=None, ids=None, name=None, essay_overall=None, title=None, content=None
    ):
        """
        Initialize HandwritingGetEssayResult instance.

        :param recognize_granularity: 识别粒度，控制坐标返回，可选值：line：行级坐标返回；word：行级坐标+字级别坐标返回；none：不返回坐标
        :type recognize_granularity: str (optional)

        :param grade: 识别的学生班级信息
        :type grade: str (optional)

        :param ids: 识别的学生学号信息
        :type ids: str (optional)

        :param name: 识别的学生姓名信息
        :type name: str (optional)

        :param essay_overall: essay_overall attribute
        :type essay_overall: HandwritingGetEssayOverall (optional)

        :param title: title attribute
        :type title: Title (optional)

        :param content: content attribute
        :type content: HandwritingCompositionGetResultContent (optional)
        """
        super().__init__()
        self.recognize_granularity = recognize_granularity
        self.grade = grade
        self.ids = ids
        self.name = name
        self.essay_overall = essay_overall
        self.title = title
        self.content = content

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
        if self.recognize_granularity is not None:
            result['recognize_granularity'] = self.recognize_granularity
        if self.grade is not None:
            result['grade'] = self.grade
        if self.ids is not None:
            result['ids'] = self.ids
        if self.name is not None:
            result['name'] = self.name
        if self.essay_overall is not None:
            result['essayOverall'] = self.essay_overall.to_dict()
        if self.title is not None:
            result['title'] = self.title.to_dict()
        if self.content is not None:
            result['content'] = self.content.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HandwritingGetEssayResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('recognize_granularity') is not None:
            self.recognize_granularity = m.get('recognize_granularity')
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('essayOverall') is not None:
            self.essay_overall = HandwritingGetEssayOverall().from_dict(m.get('essayOverall'))
        if m.get('title') is not None:
            self.title = Title().from_dict(m.get('title'))
        if m.get('content') is not None:
            self.content = HandwritingCompositionGetResultContent().from_dict(m.get('content'))
        return self
