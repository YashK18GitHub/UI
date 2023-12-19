from setuptools import setup, find_packages

setup(
    name='UI',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyQt5',  # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'ui-script = UI.test:main',  # Change 'ui-script' to the desired command name
        ],
    },
    package_data={
        'UI': ['*.ui', '*.qrc'],
    },
    include_package_data=True,
    zip_safe=False,
)
