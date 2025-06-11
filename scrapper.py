import requests
from bs4 import BeautifulSoup
import time
import csv

BASE_URL = "https://example.com/reviews?page={}"  # Replace with actual URL
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ReviewScraper/1.0; +http://yourdomain.com)"
}

MAX_REVIEWS = 2000
SLEEP_BETWEEN_REQUESTS = 1  # Be kind to the server

def get_reviews_from_page(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to fetch: {url}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    # Replace with actual selector for review content
    review_elements = soup.select(".review-text")  # Example
    reviews = [review.get_text(strip=True) for review in review_elements]

    return reviews

def scrape_reviews():
    all_reviews = []
    page = 1

    while len(all_reviews) < MAX_REVIEWS:
        print(f"Scraping page {page}...")

        url = BASE_URL.format(page)
        reviews = get_reviews_from_page(url)

        if not reviews:
            print("No more reviews found or page load error.")
            break

        all_reviews.extend(reviews)
        page += 1
        time.sleep(SLEEP_BETWEEN_REQUESTS)

    return all_reviews[:MAX_REVIEWS]

def save_reviews_to_csv(reviews, filename="reviews.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Review"])
        for review in reviews:
            writer.writerow([review])

if __name__ == "__main__":
    reviews = scrape_reviews()
    save_reviews_to_csv(reviews)
    print(f"Saved {len(reviews)} reviews to 'reviews.csv'")
