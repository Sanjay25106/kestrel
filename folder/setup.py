from setuptools import find_packages, setup

package_name = 'serial_bridge'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'pyserial'],
    zip_safe=True,
    maintainer='Sanjay',
    maintainer_email='me24b153@smail.iitm.ac.in',
    description='ROS 2 to Microcontroller serial (UART) bridge',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_bridge_node = serial_bridge.serial_bridge_node:main',
        ],
    },
)
