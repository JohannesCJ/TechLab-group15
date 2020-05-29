# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:35:34 2020

@author: Johannes Heyn
"""

"""Spider to extract URL's of books from a Listopia list on Goodreads"""
"""Run following command in bash: 
Johannes Heyn@JohannesSurface MINGW64 /d/OneDrive - Universität Münster/Studium/TechLabs-AI/TechLab-group15 (master)
$ scrapy crawl --logfile=scrapy.log -s OUTPUT_FILE_SUFFIX="book_popularByDate2" popular-list
"""

import scrapy

from .book_spider import BookSpider

GOODREADS_URL_PREFIX = "https://www.goodreads.com"

class ListSpider(scrapy.Spider):
    """Extract URLs of books from a Listopia list on Goodreads

        This subsequently passes on the URLs to BookSpider
    """
    name = "popular-list"
    goodreads_list_url = "https://www.goodreads.com/book/popular_by_date/{}/{}/"



    def __init__(self):
        super().__init__()
        self.book_spider = BookSpider()
        #months_2019 = ["October", "November", "December"]
        months_2020 = ["June", "July", "August", "September", "October", 
                       "November", "December"] #expected publications
        #months_2019 = ["January", "February", "March", "April", "May", "June",
        #               "July", "August", "September"] #missing last time
        months_2021 = ["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", 
                       "December"] #expected publications

        self.start_urls = []
        for month in months_2020:
            year = 2020
            list_url = self.goodreads_list_url.format(year, month)
            self.start_urls.append(list_url)
            
        # for month in months_2019:
        #     year = 2019
        #     list_url = self.goodreads_list_url.format(year, month)
        #     self.start_urls.append(list_url)

        for month in months_2021:
            year = 2021
            list_url = self.goodreads_list_url.format(year, month)
            self.start_urls.append(list_url)

    def parse(self, response):
        list_of_books = response.css("a.bookTitle::attr(href)").extract()

        for book in list_of_books:
            yield response.follow(book, callback=self.book_spider.parse)
