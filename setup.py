import setuptools

setuptools.setup(
    name="bom_analysis",
    version="1.0.0",
    description="A framework for performing analysis based on a Bill of Materials (BOM) structure",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    maintainer="Aditya Mishra",
    maintainer_email="aditya.iiitsp@gmail.com",
    url="https://github.com/AdityaMISHRA2803/Hierarchical-Equipment-BOM-Quality-Analytics-Engine.git",
    packages=["bom_analysis"],
    install_requires=[
        "numpy",
        "pint",
        "pandas",
        "tabulate",
        "CoolProp",
        "treelib",
        "python-box",
        "pre-commit",
    ],
    python_requires=">=3.6",
    license="BSD 3-Clause “New” or “Revised” License",
    classifiers=["License :: OSI Approved :: BSD License"],
)
