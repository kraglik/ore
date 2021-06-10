try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    long_description_content_type='text/markdown',
    name='ore-combinators',
    version='0.0.5',
    description='Parser combinator library for Python',
    python_requires='==3.*,>=3.6.0',
    project_urls={'homepage': 'https://github.com/kraglik/ore', 'repository': 'https://github.com/kraglik/ore'},
    author='Igor Kraglik',
    author_email='kraglik.i.d@gmail.com',
    license='MIT',
    keywords='parser combinator ore',
    packages=find_packages(),
    package_data={},
    install_requires=[],
    extras_require={},
)
