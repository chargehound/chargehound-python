try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

try:
    from pypandoc import convert
    long_description = convert('README.md', 'rst')
except:
    """
    Don't fail if pandoc or pypandoc are not installed.
    However, it is better to publish the package with
    a formatted README.
    """
    long_description = open('README.md').read()

from chargehound.version import VERSION

setup(
    name='chargehound',
    version=VERSION,
    author='Chargehound',
    author_email='support@chargehound.com',
    packages=['chargehound'],
    description='Chargehound Python Bindings',
    long_description=long_description,
    url='https://www.chargehound.com',
    license='MIT',
    test_suite='test.all',
    install_requires=[
        'requests'
        ],
    )
