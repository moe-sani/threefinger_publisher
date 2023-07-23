from setuptools import setup

package_name = 'threefinger_publisher'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='msani',
    maintainer_email='moesanib@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'test_publisher = threefinger_publisher.test_publisher:main',
        'keyboard_publisher = threefinger_publisher.keyboard_publisher:main',

        ],
    },
)
