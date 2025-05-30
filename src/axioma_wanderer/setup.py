from setuptools import setup

package_name = 'axioma_wanderer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kike',
    maintainer_email='kike@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wanderer = axioma_wanderer.wanderer:main',
            'wanderer_server = axioma_wanderer.wanderer_server:main',
            'discoverer_server = axioma_wanderer.discoverer_server:main'
        ],
    },
)

