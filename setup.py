from distutils.core import setup

setup(name='dstapi',
      version='0.1',
      description='',
      url='https://github.com/JonasW01ff/dstapi/tree/master',
      author='',
      author_email='',
      license='MIT',
      packages=['.dstapi.py'],
      install_requires=[
          'requests', 
          'pandas'
      ],
      zip_safe=False)
