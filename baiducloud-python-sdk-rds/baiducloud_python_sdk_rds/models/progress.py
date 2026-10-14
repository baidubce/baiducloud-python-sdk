"""
Progress information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Progress(AbstractModel):
    """
    Progress
    """

    def __init__(
        self,
        step=None,
        status=None,
        description=None,
        start_time=None,
        finish_time=None,
        percentage=None,
        estimate_time=None,
    ):
        """
        Initialize Progress instance.

        :param step: step attribute
        :type step: str (optional)

        :param status: 步骤状态，可取值：created/running/success/failed
        :type status: str (optional)

        :param description: 步骤描述
        :type description: str (optional)

        :param start_time: 步骤开始时间，未开始时可能不返回
        :type start_time: str (optional)

        :param finish_time: 步骤完成时间，未完成时可能不返回
        :type finish_time: str (optional)

        :param percentage: 当前步骤完成百分比，取值 0~100
        :type percentage: int (optional)

        :param estimate_time: 当前步骤预估剩余时间，单位：秒
        :type estimate_time: int (optional)
        """
        super().__init__()
        self.step = step
        self.status = status
        self.description = description
        self.start_time = start_time
        self.finish_time = finish_time
        self.percentage = percentage
        self.estimate_time = estimate_time

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
        if self.step is not None:
            result['step'] = self.step
        if self.status is not None:
            result['status'] = self.status
        if self.description is not None:
            result['description'] = self.description
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.percentage is not None:
            result['percentage'] = self.percentage
        if self.estimate_time is not None:
            result['estimateTime'] = self.estimate_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Progress

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('step') is not None:
            self.step = m.get('step')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('percentage') is not None:
            self.percentage = m.get('percentage')
        if m.get('estimateTime') is not None:
            self.estimate_time = m.get('estimateTime')
        return self
