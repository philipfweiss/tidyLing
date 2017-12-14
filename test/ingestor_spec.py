import unittest
import glob
import os

from lib import Ingestor


EXAMPLE_COUNTS = {
    "green2014.tex": 2,
    "resolving_scope_ambiguities.tex": 16,
    "schuster2016enhanced.tex": 21,
    "schuster2017gapping.tex": 39,
    "sebastian_lexsem.tex": 63,
    "sebastian_qp1.tex": 54,
    "sebastian_qp2_v3.tex": 37,
    "sebastian_syntax.tex": 34,
    "abstract-e.tex": 5,
    "Jasbi_nacilProceedings_ra": 19,
    "Jasbi16-Persian-indefinites": 14,
    "lsa-i-abstract.tex": 5,
    "ucsd_sembabble.tex": 51 
}


PATH_TO_TEST_TEX_FILES = "test/fixtures/tex/*.tex"

class IngestorTest(unittest.TestCase):
    
    def test_ingest(self):
        ingestor = Ingestor()
        
        filepaths = glob.glob(PATH_TO_TEST_TEX_FILES)
        for f in filepaths:
            results = ingestor.ingest(f)
            filename = os.path.basename(f)

            self.assertTrue(filename in EXAMPLE_COUNTS)
            self.assertEqual(len(results), EXAMPLE_COUNTS[filename])
        

# Should ingest all of the files in fixtures

# Should invoke parser on all files in fixtures


if __name__ == '__main__':
    unittest.main()