from setuptools import setup, find_packages


version = '0.1'
setup(name='openprocurement.standards.prozorro',
            version=version,
            description="openprocurement.standards.prozorro",
            long_description="""\
            """,
            classifiers=[
                "License :: OSI Approved :: Apache Software License",
                "Programming Language :: Python",
            ],
            keywords='',
            author='Quintagroup, Ltd.',
            author_email='info@quintagroup.com',
            url='https://github.com/tarasvaskiv/openprocurement.standards.prozorro',
            license='Apache License 2.0',
            packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
            include_package_data=True,
            zip_safe=False,
            install_requires=[
                # -*- Extra requirements: -*-
            ],
            entry_points="""
            # -*- Entry points: -*-
            """,
            )

