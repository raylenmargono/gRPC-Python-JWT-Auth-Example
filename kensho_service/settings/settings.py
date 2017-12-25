from grift import BaseConfig, EnvLoader, ConfigProperty
from schematics.types import StringType


class AppConfig(BaseConfig):
    JWT_SECRET = ConfigProperty(property_type=StringType(), exclude_from_varz=True)
    ACCESS_TOKEN = ConfigProperty(property_type=StringType(), exclude_from_varz=True)


loaders = [EnvLoader()]
settings = AppConfig(loaders)
