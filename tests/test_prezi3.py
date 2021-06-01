"""Test code for iiif_prezi3"""
from __future__ import unicode_literals
import unittest
import json
import sys
sys.path.insert(1,'.')

from iiif_prezi.prezi3 import Manifest

class TestAll(unittest.TestCase):

    def testLoadJson(self):
        with open('tests/testdata/3.0/0003-mvm-video.json') as json_file:
            data = json.load(json_file)

            manifest = Manifest(data)

            self.assertEqual(manifest.id, "https://iiif.io/api/cookbook/recipe/0003-mvm-video/manifest.json", 'ID should be https://iiif.io/api/cookbook/recipe/0003-mvm-video/manifest.json but is "{}"'.format(manifest.id))
            self.assertEqual("Manifest", manifest.type, 'Type should be manifest')
            self.assertEqual(manifest.label['en'][0], "Video Example 3", 'Label should be Video Example 3')

            with self.assertRaises(AttributeError, msg="Should get error if we get a unspecified property"):
                print ("Should not be allowed to read a non existant attribute {} ".format(manifest.notvalid))

            manifest.notvalid = 10
            print ('But once weve set it we can get it {}'.format(manifest.notvalid))

        
if __name__ == '__main__':
    unittest.main()


