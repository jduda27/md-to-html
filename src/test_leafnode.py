import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "Join us!", {"href": "www.google.com"})
        node1 = LeafNode("a", "Join us!", {"href": "www.google.com"})
        self.assertEqual(node, node1)

    def test_to_html(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), "<a href=\"https://www.google.com\">Click Me!</a>")
