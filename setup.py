from setuptools import setup

def readme():
  with open('README.rst') as f:
    return f.read()

setup(name='gender_ai',
      version='0.1',
      description='Neural Network to predict Gender from first name',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',
      ],
      url='http://github.com/leophagus/gender_ai',
      author='leophagus',
      author_email='',
      license='MIT',
      packages=['gender_ai'],
      install_requires=[
        'numpy',
      ],
      zip_safe=False)

