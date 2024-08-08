import unittest
from htmlnode import HTMLNode


class testHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "Hello world", "span", {
                        "href": "https://www.google.com",
                        "target": "_blank", })

        node2 = HTMLNode("div", "Hello world", "span", {
            "href": "https://www.google.com",
            "target": "_blank", })
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("div", "Hello world", "span", {
                        "href": "https://www.google.com",
                        "target": "_blank", })

        node2 = HTMLNode("p", "Hello test", "a", {
            "href": "https://www.amazon.com",
            "target": "#name", })
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "Hello world", "a", {
            "class": "test",
            "id": "helloworld",
        })
        self.assertEqual(node.props_to_html(),
                         " class=\"test\" id=\"helloworld\" ")
