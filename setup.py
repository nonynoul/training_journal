from setuptools import setup, find_packages

setup(
    name='training-journal', # Название вашей программы
    version='1.0.0', # Версия вашей программы.
    packages=find_packages(),
    scripts=["bin/training-journal.py"], # Расположение главного исполняемого файла.
    url='https://github.com/nonynoul/coursach', # Адрес репозитория с вашей курсовой работой.
    license='Apache-2.0',
    author='...', # ФИО автора.
    author_email='...', # Электронная почта автора.
    description='Программа для учёта тренировок', # Описание вашей поделки. Что она может, для чего сделана.
    include_package_data=True,
    install_requires=[
      # Список зависимостей если есть.
      ],
)
