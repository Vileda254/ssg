import functools

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def toHTML(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props:
            return functools.reduce(lambda current_prop, next_prop: current_prop + f'{next_prop[0]}="{next_prop[1]}" ' , self.props.items(), "")[:-1]
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"