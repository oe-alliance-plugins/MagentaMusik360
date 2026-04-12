from setuptools import setup
import setup_translate

pkg = 'Extensions.MagentaMusik360'
setup(name='enigma2-plugin-extensions-magentamusik360',
       version='1.0',
       description='MagentaMusik360 Plugin',
       package_dir={pkg: 'MagentaMusik360'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
