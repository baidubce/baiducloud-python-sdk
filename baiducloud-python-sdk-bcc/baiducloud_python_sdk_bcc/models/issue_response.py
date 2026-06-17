"""
IssueResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class IssueResponse(BceResponse):
    """
    IssueResponse
    """

    def __init__(
        self,
        issue_name=None,
        issue_alias=None,
        issue_effect=None,
        issue_description=None,
        issue_occur_time=None,
        issue_source=None,
    ):
        """
        Initialize IssueResponse instance.

        :param issue_name: 故障名称
        :type issue_name: str (optional)

        :param issue_alias: 事件中文名称
        :type issue_alias: str (optional)

        :param issue_effect: 故障影响
        :type issue_effect: str (optional)

        :param issue_description: 故障描述
        :type issue_description: str (optional)

        :param issue_occur_time: 故障发生时间，符合BCE规范的日期格式
        :type issue_occur_time: str (optional)

        :param issue_source: 事件来源
        :type issue_source: str (optional)
        """
        super().__init__()
        self.issue_name = issue_name
        self.issue_alias = issue_alias
        self.issue_effect = issue_effect
        self.issue_description = issue_description
        self.issue_occur_time = issue_occur_time
        self.issue_source = issue_source

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.issue_name is not None:
            result['issueName'] = self.issue_name
        if self.issue_alias is not None:
            result['issueAlias'] = self.issue_alias
        if self.issue_effect is not None:
            result['issueEffect'] = self.issue_effect
        if self.issue_description is not None:
            result['issueDescription'] = self.issue_description
        if self.issue_occur_time is not None:
            result['issueOccurTime'] = self.issue_occur_time
        if self.issue_source is not None:
            result['issueSource'] = self.issue_source
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IssueResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('issueName') is not None:
            self.issue_name = m.get('issueName')
        if m.get('issueAlias') is not None:
            self.issue_alias = m.get('issueAlias')
        if m.get('issueEffect') is not None:
            self.issue_effect = m.get('issueEffect')
        if m.get('issueDescription') is not None:
            self.issue_description = m.get('issueDescription')
        if m.get('issueOccurTime') is not None:
            self.issue_occur_time = m.get('issueOccurTime')
        if m.get('issueSource') is not None:
            self.issue_source = m.get('issueSource')
        return self
