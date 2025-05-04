from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Found a start tag  :", tag)
    def handle_endtag(self, tag):
        print ("Found an end tag   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Found an empty tag :", tag)

# instantiate the parser and fed it some HTML
parser = HTMLParser()
html_input = input()
parser.feed(html_input)