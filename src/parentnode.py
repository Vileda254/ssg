from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag argument missing")
        
        if not self.children:
            raise ValueError("Children nodes argument missing")
        
        def combine_children_nodes(children):
            children_html = ""
            for child in children:
                if not child.children:
                    print("child to html")
                    children_html += child.to_html()
                else:
                    print("parent to html")
                    child.to_html()
            
            return children_html
        
        return f'<{self.tag} {self.props_to_html()}>{combine_children_nodes(self.children)}</{self.tag}>'
        

        

        
        


        

        
