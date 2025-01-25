import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_noteq_text(self):
        node3 = TextNode("This is base text node", TextType.BOLD)
        node4 = TextNode("This is a diferent node", TextType.BOLD)
        self.assertNotEqual(node3, node4)
    def test_noteq_type(self):
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node3, node4)
        


if __name__ == "__main__":
    unittest.main()
