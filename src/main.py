from textnode import TextType, TextNode

def main():
    bold_node = TextNode("No Idea", TextType.BOLD, "http://www.bold.com")
    print(bold_node.__repr__())

main()