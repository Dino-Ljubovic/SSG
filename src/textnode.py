class Textnode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, Textnode):
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"Textnode({self.text}, {self.text_type}, {self.url})"
    
def main():
    textnode1 = Textnode("This is a text node", "bold", "https://boot.dev")
    textnode2 = Textnode("This is not a text node", "bold", "https://boot.dev")
    print(textnode1)
    print(textnode2)
    print(textnode1 == textnode2)
main()
