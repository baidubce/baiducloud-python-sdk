"""
KafkaConfig information
"""


class KafkaConfig:
    """
    Enum class for KafkaConfig
    Allowed values: BROKERS, TOPIC, MAXRETRIES
    """

    BROKERS = 'brokers'
    TOPIC = 'topic'
    MAXRETRIES = 'maxRetries'

    @staticmethod
    def is_valid(value):
        """Check if the value is valid for this enum"""
        valid_values = ['brokers', 'topic', 'maxRetries']
        return value in valid_values
