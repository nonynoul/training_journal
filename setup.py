"""
Базовые данные о проекте
"""

from setuptools import setup, find_packages

setup(
    name='training-journal',
    version='1.0.0',
    packages=find_packages(),
    scripts=["bin/training-journal.py"],
    url='https://github.com/nonynoul/training_journal',
    license='Apache-2.0',
    author='Tsiplakov Igor',
    author_email='factinname@gmail.com',
    description='Программа для учёта тренировок',
    include_package_data=True,
    install_requires=[
      # Список зависимостей если есть.
      ],
)
