from setuptools import find_packages, setup

package_name = 'user_service_client'

setup(name=package_name,
      version='0.0.1',
      packages=find_packages(),
      install_requires=[
          'grpcio==1.7.0',
      ]
)