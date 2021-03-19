# psychopg2
Custom Psychopg2 python 3.8 driver for AWS lambda

This is a custom compiled psycopg2 C library for Python. Due to AWS Lambda missing the required PostgreSQL libraries in the AMI image, we needed to compile psycopg2 with the PostgreSQL libpq.so library statically linked libpq library instead of the default dynamic link.

Source: https://github.com/jkehler/awslambda-psycopg2

This solution will hopfully be temporary. A more perminant fix would invlove upgrade our current infrastructer to make use of Psychopg 3.
