from setuptools import setup, find_packages

setup(
    name='your_library_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 依赖列表，例如：'requests>=2.25.1'
        'numpy',
        'pandas'
    ],
    author='kevinchu',
    author_email='chukaiyan@hotmail.com',
    description='A short description of your library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chukaiyan/MyTT.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)