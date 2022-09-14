import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='brats_toolkit',
    version='0.4.2',
    author='Christoph Berger, Florian Kofler',
    author_email='florian.kofler@tum.de, c.berger@tum.de',
    description='Preprocessing, Segmentation and Fusion for the BraTS challenge',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/neuronflow/BraTS-Toolkit-Source',
    packages=['brats_toolkit'],
    zip_safe=False,
    install_requires=[
        'SimpleITK==2.1.1.2',
        'numpy==1.22.0',
        'python-engineio==3.14.2',
        'python-socketio==4.6.1',
        'requests==2.24.0'
    ],
    entry_points={
        'console_scripts': [
            'brats-segment = brats_toolkit.cli:segmentation',
            'brats-fuse = brats_toolkit.cli:fusion',
            'brats-batch-preprocess = brats_toolkit.cli:batchpreprocess',
            'brats-preprocess = brats_toolkit.cli:singlepreprocess'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
