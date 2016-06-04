import os
from setuptools import setup, find_packages


def load_file(fp):
    with open(fp) as fd:
        return fd.readlines()


def load_version(fp):
    with open(fp) as fd:
        for line in fd:
            if '__version__' not in line:
                continue
            _, value = line.split('=', 1)
            return eval(value)


def load_extras():
    extras_require = {}
    for _, _, files in os.walk():
        for fp in files:
            if not fp.endswith('_extra_require.txt'):
                continue
            pkg, _ = fp.split('_')
            extras_require[pkg] = load_file(fp)
        break
    return extras_require


setup(
        name='txpy',
        description='Txomon python helper functions',
        version=load_version('txpy/__init__.py'),
        author='Javier Domingo Cansino',
        author_email='javierdo1@gmail.com',
        url='https://github.com/txomon/txpy',
        packages=find_packages(),
        install_requires=load_file('requirements.txt'),
        extras_require=load_extras(),
        zip_safe=False,
)
