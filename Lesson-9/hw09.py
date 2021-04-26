from abc import ABC, abstractmethod

class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def create_tag(self):
        tag = self.factory_method()
        return tag.operation()

class Tag1(Creator):
    def factory_method(self):
        return Image()

class Tag2(Creator):
    def factory_method(self):
        return Input()

class Tag3(Creator):
    def factory_method(self):
        return Text()

class Tag4(Creator):
    def factory_method(self):
        return Link()

class Tag(ABC):

    @abstractmethod
    def operation(self):
        pass

class Image(Tag):
    def operation(self):
        return '<img>'

class Input(Tag):
    def operation(self):
        return '<input></input>'

class Text(Tag):
    def operation(self):
        return '<p></p>'

class Link(Tag):
    def operation(self):
        return '<a></a>'

def client_code(factory: Creator):
    return factory.create_tag()

if __name__ == '__main__':
    elements = [Tag1(), Tag2(), Tag3(), Tag4()]
    for el in elements:
        print(client_code(el))