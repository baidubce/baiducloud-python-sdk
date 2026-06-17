"""
ShipperSummary information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ShipperSummary(AbstractModel):
    """
    ShipperSummary
    """

    def __init__(
        self,
        log_shipper_id=None,
        log_shipper_name=None,
        project=None,
        log_store_name=None,
        dest_type=None,
        status=None,
        create_date_time=None,
        err_message=None,
    ):
        """
        Initialize ShipperSummary instance.

        :param log_shipper_id: 投递任务ID
        :type log_shipper_id: str (optional)

        :param log_shipper_name: 投递任务名称
        :type log_shipper_name: str (optional)

        :param project: 日志组名称
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)

        :param dest_type: 投递目的端类型
        :type dest_type: str (optional)

        :param status: 任务状态
        :type status: str (optional)

        :param create_date_time: 创建时间
        :type create_date_time: str (optional)

        :param err_message: 错误信息
        :type err_message: str (optional)
        """
        super().__init__()
        self.log_shipper_id = log_shipper_id
        self.log_shipper_name = log_shipper_name
        self.project = project
        self.log_store_name = log_store_name
        self.dest_type = dest_type
        self.status = status
        self.create_date_time = create_date_time
        self.err_message = err_message

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
        if self.log_shipper_id is not None:
            result['logShipperID'] = self.log_shipper_id
        if self.log_shipper_name is not None:
            result['logShipperName'] = self.log_shipper_name
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.dest_type is not None:
            result['destType'] = self.dest_type
        if self.status is not None:
            result['status'] = self.status
        if self.create_date_time is not None:
            result['createDateTime'] = self.create_date_time
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ShipperSummary

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logShipperID') is not None:
            self.log_shipper_id = m.get('logShipperID')
        if m.get('logShipperName') is not None:
            self.log_shipper_name = m.get('logShipperName')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('destType') is not None:
            self.dest_type = m.get('destType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createDateTime') is not None:
            self.create_date_time = m.get('createDateTime')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        return self
