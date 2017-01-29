import uncss
from setuptools import setup, find_packages


with open('requirements-tests.txt') as f:
    requirements_tests = f.readlines()

with open('README.rst') as readme_file:
    readme = readme_file.read()


setup(
    name='django-uncss',
    version=uncss.__version__,
    author='Naison Souza',
    author_email='naison.souza@gmail.com',
    license='BSD',
    description='Remove unused styles from CSS django applications!',
    long_description=readme,
    packages=find_packages(exclude=['*.tests']),
    keywords=['uncss', 'performance'],
    url='https://github.com/naisonsouza/django-uncss',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'Django>=1.8',
    ],
    tests_require=requirements_tests,
    zip_safe=False
)
