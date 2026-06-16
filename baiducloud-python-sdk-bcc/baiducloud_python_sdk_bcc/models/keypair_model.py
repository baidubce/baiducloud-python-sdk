"""
KeypairModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.pass_instance_model import PassInstanceModel


class KeypairModel(AbstractModel):
    """
    KeypairModel
    """

    def __init__(
        self,
        keypair_id=None,
        name=None,
        description=None,
        instance_count=None,
        created_time=None,
        public_key=None,
        finger_print=None,
        private_key=None,
        region_id=None,
        paas_instance_count=None,
    ):
        """
        Initialize KeypairModel instance.

        :param keypair_id: 密钥对ID
        :type keypair_id: str (optional)

        :param name: 密钥对名称
        :type name: str (optional)

        :param description: 密钥对描述
        :type description: str (optional)

        :param instance_count: 密钥对绑定的虚机数目
        :type instance_count: int (optional)

        :param created_time: 密钥对创建时间
        :type created_time: str (optional)

        :param public_key: 公钥内容
        :type public_key: str (optional)

        :param finger_print: 公钥指纹
        :type finger_print: str (optional)

        :param private_key: 私钥内容
        :type private_key: str (optional)

        :param region_id: 密钥对所在的地域id
        :type region_id: str (optional)

        :param paas_instance_count: paas应用数目（查询密钥对列表、查询密钥对详情返回）
        :type paas_instance_count: List[PassInstanceModel] (optional)
        """
        super().__init__()
        self.keypair_id = keypair_id
        self.name = name
        self.description = description
        self.instance_count = instance_count
        self.created_time = created_time
        self.public_key = public_key
        self.finger_print = finger_print
        self.private_key = private_key
        self.region_id = region_id
        self.paas_instance_count = paas_instance_count

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
        if self.keypair_id is not None:
            result['keypairId'] = self.keypair_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.public_key is not None:
            result['publicKey'] = self.public_key
        if self.finger_print is not None:
            result['fingerPrint'] = self.finger_print
        if self.private_key is not None:
            result['privateKey'] = self.private_key
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.paas_instance_count is not None:
            result['paasInstanceCount'] = [i.to_dict() for i in self.paas_instance_count]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: KeypairModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('keypairId') is not None:
            self.keypair_id = m.get('keypairId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('publicKey') is not None:
            self.public_key = m.get('publicKey')
        if m.get('fingerPrint') is not None:
            self.finger_print = m.get('fingerPrint')
        if m.get('privateKey') is not None:
            self.private_key = m.get('privateKey')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('paasInstanceCount') is not None:
            self.paas_instance_count = [PassInstanceModel().from_dict(i) for i in m.get('paasInstanceCount')]
        return self
