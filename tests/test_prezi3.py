"""Test code for iiif_prezi3"""
from __future__ import unicode_literals
import unittest
import json
import sys
sys.path.insert(1,'.')

from iiif_prezi.prezi3helper import Manifest, Canvas

class TestAll(unittest.TestCase):

    def testLoadJson(self):
        with open('tests/testdata/3.0/0003-mvm-video.json') as json_file:
            data = json.load(json_file)

            manifest = Manifest(**data)

            self.assertEqual(manifest.id, "https://iiif.io/api/cookbook/recipe/0003-mvm-video/manifest.json", 'ID should be https://iiif.io/api/cookbook/recipe/0003-mvm-video/manifest.json but is "{}"'.format(manifest.id))
            self.assertEqual("Manifest", manifest.type, 'Type should be manifest')
            self.assertEqual(manifest.label['en'][0], "Video Example 3", 'Label should be Video Example 3')

            with self.assertRaises(AttributeError, msg="Should get error if we get a unspecified property"):
                print ("Should not be allowed to read a non existant attribute {} ".format(manifest.notvalid))

            with self.assertRaises(ValueError, msg="Should get error if we set a unspecified property"):
                manifest.notvalid = 10
                print ('But once weve set it we can get it {}'.format(manifest.notvalid))

            #print (json.dumps(json.loads(manifest.json(exclude_unset=True)), indent=4))

    def testNewManifest(self):
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0')

        canvas = Canvas(id='http://iiif.example.org/prezi/Canvas/0')
        canvas.height = 100
        canvas.width = 200

        canvas2 = Canvas(id='http://iiif.example.org/prezi/Canvas/1')
        canvas2.height = 100

        manifest.items = [canvas, canvas2]

        print (json.dumps(json.loads(manifest.json(exclude_unset=True)), indent=4))
        
    def testOverloadCanvas(self):
        manifest = Manifest(id='http://iiif.example.org/prezi/Manifest/0')

        canvas = Canvas(label="test")
        canvas.height = 100
        canvas.width = 200
        #print ('Canvas id {}'.format(canvas.id))

        self.assertEqual("test", canvas.label['en'], 'Label should be updated')
        self.assertEqual("http://example.com/canvas/1", canvas.id, 'Id should be the default one')
        
if __name__ == '__main__':
    unittest.main()


