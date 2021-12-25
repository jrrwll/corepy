from distutils.core import setup

setup(
    name='corepy',
    packages=[
        'corepy',
        'corepy.argparse',
        'corepy.conv',
        'corepy.crypto',
        'corepy.httpclient',
        'corepy.lang',
        'corepy.matrix',
    ],
    version='0.1.2',
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='Apache License 2.0',
    description='',
    author='bobbystrange',
    author_email='bobby.j.strange@gmail.com',
    url='https://github.com/bobbystrange/corepy',
    download_url='https://github.com/bobbystrange/corepy/archive/0.1.tar.gz',
    keywords=['argparse', ],
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        # as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
