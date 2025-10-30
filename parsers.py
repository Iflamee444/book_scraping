import re
import requests as rq
from scrapy import Selector
from settings import BASE_URL, NUMBER_WORDS, HEADERS, TIMEOUT
from utils import download_file


def get_category_links():
    response = rq.get(BASE_URL, headers=HEADERS, timeout=TIMEOUT)
    selector = Selector(text=response.text)
    categorie_url_list = selector.css("ul.nav-list ul li a::attr(href)").getall()
    return [u.replace('index.html', '') for u in categorie_url_list]

def parse_list_page(url):
    response = rq.get(url, headers=HEADERS, timeout=TIMEOUT)
    selector = Selector(text=response.text)
    book_links = selector.css("article.product_pod h3 a::attr(href)").getall()
    has_next = selector.css("li.next a::text").get() == "next"
    return book_links, has_next

def make_book_url(book_link, category_url):
    return f"{BASE_URL}{category_url}{book_link}"

def make_image_url(relative_link):
    return f"{BASE_URL}{re.sub(r'^(\.\./)+', '', relative_link)}"

def parse_product_page(book_url):
    response = rq.get(book_url, headers=HEADERS, timeout=TIMEOUT)
    selector = Selector(text=response.text)

    title = selector.css(".product_main h1::text").get()
    price = selector.css(".product_main .price_color::text").get().replace("Â", "").replace("£", "")
    availability = selector.css(".product_main .availability::text").getall()[1].strip()
    note_class = selector.css(".product_main .star-rating").attrib.get("class", "")
    note = NUMBER_WORDS.get(note_class.replace("star-rating", "").strip().lower())
    image_rel = selector.css(".carousel-inner img::attr(src)").get()
    upc = selector.css("table.table.table-striped tr:nth-child(1) td::text").get()
    category = selector.css("ul.breadcrumb li a::text").getall()[2]

    image_url = make_image_url(image_rel)
    return {
        "titre": title,
        "prix": price,
        "disponibilite": availability,
        "note": note,
        "url": book_url,
        "url_image": image_url,
        "upc": upc,
        "categorie": category,
    }

def download_book_image(book_detail,outdir):
    
    img_folder = f"{outdir}/images/{book_detail['categorie']}"
    img_path = f"{img_folder}/{book_detail['upc']}.jpg"
    download_file(book_detail["url_image"], img_path)
