import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='alpaca_kernel_2',
    version='0.0.1',
    author='Thijn Hoekstra',
    author_email='t.w.hoekstra@student.tudelft.nl',
    description='Fork of jupyter_micropython_kernel and IPythonkernel',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/twhoekstra/alpaca_kernel_2',
    project_urls = {
        "Bug Tracker": "https://github.com/twhoekstra/alpaca_kernel_2"
    },
    license='MIT',
    packages=['alpaca_kernel'],
    install_requires=[
        'setuptools',
        'matplotlib',
        'numpy',
        'pyserial',
    ],
)