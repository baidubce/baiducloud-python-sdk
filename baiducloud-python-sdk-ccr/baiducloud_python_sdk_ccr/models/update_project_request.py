"""
Request entity for UpdateProjectRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateProjectRequest(AbstractModel):
    """
    Request entity for UpdateProjectRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, project_name, auto_scan, public):
        """
        Initialize UpdateProjectRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param project_name: project_name parameter
        :type project_name: str (required)

        :param auto_scan: 推送时是否自动扫描镜像，有效值为true、false
        :type auto_scan: str (required)

        :param public: 命名空间类型，有两种类型。true表示公有，false表示私有
        :type public: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.project_name = project_name
        self.auto_scan = auto_scan
        self.public = public

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
        if self.auto_scan is not None:
            result['autoScan'] = self.auto_scan
        if self.public is not None:
            result['public'] = self.public
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateProjectRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('autoScan') is not None:
            self.auto_scan = m.get('autoScan')
        if m.get('public') is not None:
            self.public = m.get('public')
        return self
