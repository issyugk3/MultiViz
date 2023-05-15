import re

from setuptools import find_packages, setup

deps = [
    "appdirs==1.4.4",
    "certifi==2021.5.30",
    "charset-normalizer==2.0.4",
    "click==8.0.1",
    "cycler==0.10.0",
    "filelock==3.0.12",
    "huggingface-hub==0.0.12",
    "idna==3.2",
    "imageio==2.9.0",
    "joblib==1.0.1",
    "kiwisolver==1.3.1",
    "lime==0.2.0.1",
    "matplotlib==3.4.3",
    "networkx==2.6.2",
    "numpy==1.21.2",
    "packaging==21.0",
    "Pillow==8.3.1",
    "pyparsing==2.4.7",
    "python-dateutil==2.8.2",
    "PyWavelets==1.1.1",
    "PyYAML==5.4.1",
    "regex==2021.8.3",
    "requests==2.26.0",
    "sacremoses==0.0.45",
    "scikit-image==0.18.2",
    "scikit-learn==0.24.2",
    "scipy==1.7.1",
    "six==1.16.0",
    "threadpoolctl==2.2.0",
    "tifffile==2021.8.8",
    "tokenizers==0.10.3",
    "torch==1.9.0",
    "tqdm==4.62.1",
    "transformers==4.9.2",
    "typing-extensions==3.10.0.0",
    "urllib3==1.26.6",
    "h5py==3.1.0",
    "glm_saga==0.1.2"
]

setup(
    name="mma",
    version="0.0.1.dev0",
    author="Paul Liang, Gunjan Chhablani",
    author_email="pliang@cs.cmu.edu",
    description="Multimodal Analysis Tool",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="multimodal deep learning pytorch",
    license="Apache",
    url="https://github.com/pliang/multimodal_analysis",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.7.11",
    install_requires=deps,
    classifiers=[
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
