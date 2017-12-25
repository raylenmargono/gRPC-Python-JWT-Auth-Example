from grift import BaseConfig, EnvLoader, ConfigProperty
from schematics.types import StringType


class AppConfig(BaseConfig):
    POSTGRES_HOST = ConfigProperty(property_type=StringType(), exclude_from_varz=True)
    POSTGRES_USER = ConfigProperty(property_type=StringType(), exclude_from_varz=True)
    POSTGRES_PASSWORD = ConfigProperty(property_type=StringType(), exclude_from_varz=True)
    POSTGRES_DB = ConfigProperty(property_type=StringType(), exclude_from_varz=True)
    JWT_SECRET = ConfigProperty(property_type=StringType(), exclude_from_varz=True)
    CRYPT_SALT = ConfigProperty(property_type=StringType(), exclude_from_varz=True)


loaders = [EnvLoader()]
settings = AppConfig(loaders)
