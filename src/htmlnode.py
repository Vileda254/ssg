import functools

class HTMLNode():
    def __init__(self, value=None, children=None, props=None, tag=None):
        self.value = value
        self.children = children
        self.props = props
        self.tag = tag

    def toHTML(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props:
            return functools.reduce(lambda current_prop, next_prop: current_prop + f'{next_prop[0]}="{next_prop[1]}" ' , self.props.items(), "")[:-1]
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.value}, {self.children}, {self.props}, {self.tag})"