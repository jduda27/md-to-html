import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_neq_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a test node", "bold", "www.myurl.com")
        node2 = TextNode("This is a test node", "bold")
        self.assertNotEqual(node, node2)

    def test_url_default(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "None")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is one", "bold")
        node2 = TextNode("This is two", "italic")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
