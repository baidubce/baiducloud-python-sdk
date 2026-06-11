"""
Request entity for CreateImageRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateImageRequest(AbstractModel):
    """
    Request entity for CreateImageRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, image_name, instance_id=None, snapshot_id=None, encrypt_key=None, relate_cds=None, detection=None
    ):
        """
        Initialize CreateImageRequest request entity.

        :param image_name: 待创建的自定义镜像名称，支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65
        :type image_name: str (required)

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)

        :param snapshot_id: snapshot_id parameter
        :type snapshot_id: str (optional)

        :param encrypt_key: 加密密钥
        :type encrypt_key: str (optional)

        :param relate_cds: 是否创建包含了所有cds盘的大镜像，如果为true，镜像不能加密，且必须在白名单内，默认为false
        :type relate_cds: bool (optional)

        :param detection: detection parameter
        :type detection: bool (optional)
        """
        super().__init__()
        self.image_name = image_name
        self.instance_id = instance_id
        self.snapshot_id = snapshot_id
        self.encrypt_key = encrypt_key
        self.relate_cds = relate_cds
        self.detection = detection

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
        if self.image_name is not None:
            result['imageName'] = self.image_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id
        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key
        if self.relate_cds is not None:
            result['relateCds'] = self.relate_cds
        if self.detection is not None:
            result['detection'] = self.detection
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateImageRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageName') is not None:
            self.image_name = m.get('imageName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')
        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')
        if m.get('relateCds') is not None:
            self.relate_cds = m.get('relateCds')
        if m.get('detection') is not None:
            self.detection = m.get('detection')
        return self
