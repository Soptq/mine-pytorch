import setuptools

setuptools.setup(
    name="mine", # Replace with your own username
    version="0.0.1",
    author="",
    author_email="",
    description="An implementation of the MINE algorithm in Pytorch",
    long_description="",
    long_description_content_type="",
    url="https://github.com/gtegner/mine-pytorch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = [
        'pytorch_lightning==1.9',
        'matplotlib==3.7.2',
        'numpy==1.25.0',
        'tqdm==4.57.0',
        'torch==1.13.1',
        'torchvision==0.14.1',
        'scikit_learn==1.1.3',
        'pillow==10.0.0'
    ]
)
