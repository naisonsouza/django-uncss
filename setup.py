from setuptools import setup
import uncss


with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='django-storages',
    version=uncss.__version__,
    packages=['uncss', 'storages.backends'],
    author='Naison Souza',
    author_email='naison.souza@gmail.com',
    license='BSD',
    description='Remove unused styles from CSS django applications!',
    long_description=readme,
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    tests_require=requirements,
    zip_safe=False
)
