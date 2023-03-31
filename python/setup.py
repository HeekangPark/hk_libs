import setuptools

setuptools.setup(
    name="hk_utils",
    version="1.1.1",
    license="MIT",
    author="Heekang Park",
    author_email="park.heekang33@gmail.com",
    description="Python utilities by Heekang Park",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HeekangPark/hk-utils",
    python_requires=">=3",
    packages=["hk_utils"],
    include_package_data=True,
    package_data={
        "hk_utils": [
        ]
    },
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
