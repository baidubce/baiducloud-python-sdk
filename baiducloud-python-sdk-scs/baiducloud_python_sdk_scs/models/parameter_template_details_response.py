"""
Request entity for ParameterTemplateDetailsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.parameters import Parameters


class ParameterTemplateDetailsResponse(BceResponse):
    """
    ParameterTemplateDetailsResponse
    """

    def __init__(
        self,
        template_id=None,
        template_show_id=None,
        template_name=None,
        parameter_num=None,
        cluster_type=None,
        engine=None,
        engine_version=None,
        template_type=None,
        need_reboot=None,
        comment=None,
        create_time=None,
        update_time=None,
        parameters=None,
    ):
        """
        Initialize ParameterTemplateDetailsResponse response.

        :param template_id: 参数模板数字ID
        :type template_id: int (optional)

        :param template_show_id: 参数模板ID
        :type template_show_id: str (optional)

        :param template_name: 参数模板名称
        :type template_name: str (optional)

        :param parameter_num: 参数模板参数数量
        :type parameter_num: int (optional)

        :param cluster_type: 集群类型  (master_slave、default、cluster)
        :type cluster_type: str (optional)

        :param engine: 引擎类型
        :type engine: str (optional)

        :param engine_version: 引擎版本
        :type engine_version: str (optional)

        :param template_type: 参数模板类型（1为自定义参数模板）
        :type template_type: int (optional)

        :param need_reboot: 是否需要重启(该参数模版是否有需要重启生效的参数)，0：不需要，1：需要
        :type need_reboot: int (optional)

        :param comment: 备注
        :type comment: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)

        :param parameters: 参数列表
        :type parameters: List[Parameters] (optional)
        """
        super().__init__()
        self.template_id = template_id
        self.template_show_id = template_show_id
        self.template_name = template_name
        self.parameter_num = parameter_num
        self.cluster_type = cluster_type
        self.engine = engine
        self.engine_version = engine_version
        self.template_type = template_type
        self.need_reboot = need_reboot
        self.comment = comment
        self.create_time = create_time
        self.update_time = update_time
        self.parameters = parameters

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
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.template_show_id is not None:
            result['templateShowId'] = self.template_show_id
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.parameter_num is not None:
            result['parameterNum'] = self.parameter_num
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.engine is not None:
            result['engine'] = self.engine
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.template_type is not None:
            result['templateType'] = self.template_type
        if self.need_reboot is not None:
            result['needReboot'] = self.need_reboot
        if self.comment is not None:
            result['comment'] = self.comment
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.parameters is not None:
            result['parameters'] = [i.to_dict() for i in self.parameters]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ParameterTemplateDetailsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('templateShowId') is not None:
            self.template_show_id = m.get('templateShowId')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('parameterNum') is not None:
            self.parameter_num = m.get('parameterNum')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')
        if m.get('needReboot') is not None:
            self.need_reboot = m.get('needReboot')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('parameters') is not None:
            self.parameters = [Parameters().from_dict(i) for i in m.get('parameters')]
        return self
