from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_stype):
    #toma la lista de nodos de texto, las separa por el tipo 
    # code ' bold ** italic *
    for node in old_nodes:
        if text_stype == "CODE":
            node.split('\'')

def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

main()
