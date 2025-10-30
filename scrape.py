import argparse
import time

from parsers import (
    get_category_links,
    parse_list_page,
    make_book_url,
    parse_product_page,
    download_book_image,
)
from utils import write_csv
from settings import BASE_URL

def extract_category_from_url(url):
    return url.split("/")[-2].split("_")[0]

def scrape_category(category_url, max_page, delay, outdir,max_book):
    page_number = 1
    has_next = True
    all_books = []

    # print("Inside : " + str(max_page) + " and " + str(page_number))

    while has_next and page_number <= max_page:
        # print("Page number : " + str(page_number))
        if page_number == 1:
            page_url = f"{BASE_URL}{category_url}index.html"
        else:
            page_url = f"{BASE_URL}{category_url}page-{page_number}.html"

        book_links, has_next = parse_list_page(page_url)
        book_urls = [make_book_url(link, category_url) for link in book_links]

        book_count = 1
        for book_url in book_urls:
            if max_book and book_count > max_book:
                break

            time.sleep(delay)
            details = parse_product_page(book_url)
            download_book_image(details,outdir)
            all_books.append(details)
            book_count += 1

        page_number += 1

    category_name = extract_category_from_url(category_url)
    csv_path = f"{outdir}/csv/category_{category_name}.csv"
    write_csv(all_books, csv_path)

def main():
    parser = argparse.ArgumentParser(description="Scrape books.toscrape.com")
    parser.add_argument("--categories", nargs="+", help="Categories to scrape (e.g. travel science)")
    parser.add_argument("--delay", type=float, help="Delay in second", default=1)
    parser.add_argument("--max_page", type=int, help="Choose the number of pages you need to scrap")
    parser.add_argument("--outdir", type=str, help="The exit folder for CVS and images files",default="output")
    parser.add_argument("--max_book", type=int, help="The number of book")
    args = parser.parse_args()

    all_categories = get_category_links()

    if args.categories:
        selected = [c for c in all_categories if any(cat.lower() in c.lower() for cat in args.categories)]
    else:
        selected = all_categories

    if args.max_page:
        max_page = args.max_page
    else:
        max_page = 255

    if args.delay:
        delay = args.delay
    else:
        delay = 0

    if args.outdir:
        outdir = args.outdir
    else:
        outdir = "output"

    if args.max_book:
        max_book = args.max_book
    else:
        max_book = 5000

    for category_url in selected:
        scrape_category(category_url, max_page, delay, outdir,max_book)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Temps : " + str(end - start))
