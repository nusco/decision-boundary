import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decision_boundary",
    version="0.0.2",
    author="Paolo Perrotta",
    author_email="paolo.nusco.perrotta@gmail.com",
    description="A minimalist Python package to draw decision boundaries in machine learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nusco/decision-boundary",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
