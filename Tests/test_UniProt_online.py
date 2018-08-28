# Copyright 2007-2010 by Peter Cock.  All rights reserved.
# Revisions copyright 2007-2008 by Michiel de Hoon.  All rights reserved.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

"""Testing online code for UniProt.
"""
import unittest

import UniProt


class UniProtTests(unittest.TestCase):
    """Test for UniProt module."""

    def test_search(self):
        """UniPort.search("O48109")"""
        identifier = "O48109"
        handle = UniProt.search(identifier, columns=("organism",))
        self.assertEqual(handle.read(),
                         "Organism\nPython regius (Ball python) (Boa regia)\n")
        handle = UniProt.search(identifier, output_format="fasta")
        self.assertEqual(handle.readline().split("|")[1],
                         identifier)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
