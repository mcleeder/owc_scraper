from lxml.html import fromstring, etree
from typing import Self


class LightElement():
    def __init__(self, element):
        if isinstance(element, str):
            element = fromstring(element)
        if not isinstance(element, etree._Element):
            raise TypeError("Expected an lxml.etree._Element instance")
        self._element = element

    def __getattr__(self, name):
        return getattr(self._element, name)

    def __setattr__(self, name, value):
        if name == "_element":
            super().__setattr__(name, value)
        else:
            setattr(self._element, name, value)

    @property
    def attrib(self):
        return self._element.attrib
    
    @property
    def tag(self):
        return self._element.tag

    @property
    def text(self):
        return self._element.text

    def __str__(self):
        return etree.tostring(self._element).decode('utf-8')

    def element(self, xpath: str) -> Self:
        """
        Returns the first element match

        Args:
            xpath: xpath selector

        Returns:
            HtmlElement
        """
        return LightElement(self._element.xpath(f".{xpath}")[0]) if self._element.xpath(f".{xpath}") else None

    def elements(self, xpath: str) -> list[Self | None]:
        """
        Returns all matching elements

        Args:
            xpath: xpath selector

        Returns:
            list[HtmlElement]
        """
        return [LightElement(e) for e in self._element.xpath(f".{xpath}")]


    def contains_string(self, target: str) -> bool:
        """
        Recursive search of element and children for a single string

        Args:
            target: string

        Returns:
            bool
        """
        if target in (self._element.text or ''):
            return True
        for child in self._element.iterchildren():
            if LightElement(child).contains_string(target):
                return True
        return False

    def contains_any_string(self, targets: list[str]) -> bool:
        """
        Recursive search of element and children for any string in list

        Args:
            targets: list of strings

        Returns:
            bool
        """
        if any([x in (self._element.text or '') for x in targets]):
            return True
        for child in self._element.iterchildren():
            if LightElement(child).contains_any_string(targets):
                return True
        return False