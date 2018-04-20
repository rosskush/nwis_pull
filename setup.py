import sys
from distutils.core import setup
# from setuptools import setup

DESCRIPTION = """\
Classes for pulling nwis data.
"""

# setup(name="nwis_pull",version="0.1",description="Classes for pulling nwis data into pandas dataframes",
	# author="Ross Kushnereit",packages=["nwis_pull"])


def run():
    setup(name="nwis_pull",
          version="0.1",
          description="Classes for pulling nwis data into pandas dataframes",
          author="Ross Kushnereit",
          packages=["nwis_pull"],
          )
if __name__ == "__main__":
    run()