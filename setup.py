from setuptools import setup, find_packages

setup(
    name='hello-world-package',
    version='0.1.0',
    description='A simple Hello World package',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),  # Automatically finds all packages in the directory
    install_requires=[],       # Add any external dependencies here
    entry_points={
        'console_scripts': [
            'say-hello=hello_world.hello:say_hello',  # Creates a CLI command `say-hello`
        ],
    },
)
