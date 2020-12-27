import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="vis3d",
    version="0.0.1",
    description="Minimal 3D data visualizer",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/LukasDrsman/vis3d",
    author="Lukáš Dršman",
    author_email="lukaskodr@gmail.com",
    license="Unlicense License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages=setuptools.find_packages(),
    install_requires=["PyOpenGL", "PyOpenGL_accelerate", "pygame"],
    python_requires='>=3.6'
)
