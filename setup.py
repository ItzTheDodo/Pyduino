from setuptools import setup

with open("README.md", "r") as f:
  desc = f.read()

setup(
  name="Pyduino",
  version="1.0"
  author="ItzTheDodo",
  author_email="-",
  description="A library that enables coding for the Arduino",
  long_description=desc,
  long_description_content_type="text/markdown",
  url="https://github.com/ItzTheDodo/Pyduino",
  packages=["Pyduino"],
  license='LICENSE',
  install_requires=[
        "pyserial >= 3.0"
  ]
)
