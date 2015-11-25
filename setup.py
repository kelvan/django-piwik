import os

from setuptools import setup, find_packages
from piwik import __version__


setup(
    name='django-piwik',
    version=__version__,
    description='A simple app to add the Piwik JS tracking code to your template.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Raphael Jasjukaitis, Jørn Åne de Jong',
    author_email='webmaster@raphaa.de, jorn.dejong@uninett.no',
    url='https://github.com/raphaa/django-piwik',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=['Django'],
)
