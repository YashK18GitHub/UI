from setuptools import setup, find_packages

setup(
    name='UI',  # This is the name under which your package will be installed
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
        'UI': ['resources_rc.py'],
    },
    include_package_data=True,
    zip_safe=False,
)
