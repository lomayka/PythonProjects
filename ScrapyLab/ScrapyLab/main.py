import os
from lxml import etree
from scrapy import cmdline


def articles_parse():
    try:
        os.remove("results/articles.xml")
    except OSError:
        print("OS Error occurred while trying to delete articles.xml")

    cmdline.execute("scrapy crawl articles -o results/articles.xml -t xml".split())

def print_urls():
    root = etree.parse("results/articles.xml")
    for url in root.iterfind(".//item//url"):
        print(url.text)

def products_parse():
    try:
        os.remove("results/products.xml")
    except OSError:
        print("OS Error occurred while trying to delete products.xml")

    cmdline.execute("scrapy crawl products -o results/products.xml -t xml".split())


def xml_to_xhtml():
    dom = etree.parse("results/products.xml")
    xslt = etree.parse("xslscripts/products.xsl")
    transform = etree.XSLT(xslt)
    result = transform(dom)
    try:
        os.remove("results/products.html")
    except OSError:
        print("OS Error occurred while trying to delete products.html")
    result.write_output("results/products.html")


def do_products():
    products_parse()


def do_articles():
    articles_parse()


#do_articles()
#do_products()
xml_to_xhtml()
#print_urls()