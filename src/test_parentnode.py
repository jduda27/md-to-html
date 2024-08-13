import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class testParentNode(unittest.TestCase):
    def testParentNode(self):
        lNodes1 = LeafNode("a","click me",{"href":"www.google.com"})
        lNodes2 = LeafNode("a","click me",{"href":"www.google.com"})
        pNode1 = ParentNode("div",[lNodes1,lNodes2],{"id":"main"})
        self.assertEqual(pNode1.to_html(),"<div id=\"main\"><a href=\"www.google.com\">click me</a><a href=\"www.google.com\">click me</a></div>")

    def testParentSubNode(self):
        lNode1 = LeafNode("a","click me",{"href":"banana.com"})
        lNode2 = LeafNode("button","Hello world")
        pNode2 = ParentNode("div",[lNode1,lNode2],{"id":"main"})
        pNode1 = ParentNode("html",[pNode2],None)
        print(pNode1.to_html())

    def testParentofParentofParent(self):
        lNode1 = LeafNode("p","test Node",None)
        pNode1 = ParentNode("div",[lNode1,lNode1],{"id":"main"})
        pNode2 = ParentNode("body",[lNode1,pNode1],None)
        pNode3 = ParentNode("html",[pNode2],None)
        print(pNode3.to_html())
