from setuptools import setup
from Coberny import __version__ as version

setup(
  name='Coberny',
  version=version,
  description='Étude des prix des autoroutes et estimation des coûts de trajet',
  url='https://github.com/ABernard27/PROJET-groupe-3.git'
  author='Bernard Anne, Chery Fanny, Côme Olivier',
  author_email='anne.bernard27@gmail.com',
  license='MIT',
  packages=['Coberny','Coberny.map', 'Coberny.distribution_of_price', 'Coberny.graph_min_cost'],
  zip_safe=False
)
