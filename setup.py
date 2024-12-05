from setuptools import setup, find_packages

setup(
    name="MyosinCK",                 
    version="0.1.0",                   
    author="Jeffrey Pham",
    author_email="jeffp12@uw.edu",
    description="The goal of this program is to establish a visualization tool tailored to describing cardiac-specific muscle dynamics and how the alterations of parameters mentioned above (due to disease mutations) can impact the efficiency of muscle dynamics.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jeffp12/Myosin-Crossbridge-Cycling-Kinetics",  # Link to your repo
    packages=find_packages(),            # Automatically find packages
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "tellurium>=2.0.0",
        "pandas>=1.3.0",
        "Pillow>=8.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',             # Minimum Python version
)