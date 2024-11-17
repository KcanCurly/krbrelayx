from setuptools import setup, find_packages

setup(
    name="krbrelayx",
    version="1.0.0",
    author="KcanCurly",
    description="Toolkit for abusing Kerberos.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/krbrelayx",
    packages=find_packages(),
    install_requires=[
        "ldap3-bleeding-edge==2.10.1.1337",
        "impacket==0.12.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "addspn.py=src.addspn:main",
            "dnstool.py=src.dnstool:main",
            "krbrelayx.py=src.krbrelayx:main",
            "printerbug.py=src.printerbug:main",
        ],
    },
)