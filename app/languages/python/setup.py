from setuptools import setup, find_packages

setup(
    name='android-project-generator',
    version='0.1.0',
    description="A simple Android project structure generator designed and aims to streamline the setting up process of your host system for Android application development from command line (without Android Studio).",
    author='Thanatisia',
    author_email='55834101+Thanatisia@users.noreply.github.com',
    packages=find_packages(where="src"),
    package_dir={
        # "package-name" : "
        # Default package name ("") = Default package
        "":"src"
    },
    install_requires=[
        # List your dependencies here
    ],
    url='https://github.com/Thanatisia/android-project-generator/tree/development/app/languages/python',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
    ],
    entry_points = {
        "console_scripts" : [
            # "android_project_generator = android_project_generator.__main__:main",
            "android-project-generator = android_project_generator.__main__:main",
        ],
    },
)

