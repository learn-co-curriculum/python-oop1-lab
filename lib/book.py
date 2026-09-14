#!/usr/bin/env python3
class Book:
    def __init__(self,title,pageCount):
        self.title=title
        self.pageCount=pageCount
    @property
    def page_count(self,count):
        if not isinstance(count,int):
            print("Page Count must be an int")
        elif count<=0:
            print("Pages must be greater than 0")
        else:
            self.pageCount=count
    def turn_page():
        print("Flipping the page...wow, you read fast!")
    
        