from setuptools import setup, find_packages, Extension

ex_module = Extension(
    'ota42y_python_package_test.cxt',
    sources=['ota42y_python_package_test/extension.c'],
    include_dirs = ['/usr/local/include'],
    library_dirs = ['/usr/local/lib']     
)

setup(
    name="ota42y_python_package_test",
    version="0.1.4",
    license="MIT",
    description="test package(only linux)",
    author="ota42y",
    url="https://github.com/ota42y/ota42y_python_package_test",
    packages=find_packages("ota42y_python_package_test"),
    package_dir={"": "ota42y_python_package_test"},
    include_package_data=True,
    zip_safe=False,
    setup_requires=["pytest-runner"],
    ext_modules=[ex_module],
    python_requires='>=3.8,<4.0'
)
