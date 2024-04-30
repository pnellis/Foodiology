import mysql.connector
from recipe_scrapers import scrape_me
import csv
import uuid
import time
import requests
from bs4 import BeautifulSoup

def connect_to_database():
    return mysql.connector.connect(
        host="foodiology.cxwwgy2c4rn6.us-east-1.rds.amazonaws.com",
        port="3306",
        user="admin",
        password="Foodiology123",
        database="foodiology_final"
    )

def insert_recipe_data(scraper, created_by_id="c33920bb2da146fb94b58f987a94a91d", Created_at="2021-06-27"):
    db = connect_to_database()
    cursor = db.cursor()
    try:
        title = scraper.title()
        canonical_url = scraper.canonical_url() if scraper.canonical_url() else "Not available"

        # Check for existing recipe by title and canonical URL
        cursor.execute("""
            SELECT id FROM post_post WHERE title = %s OR canonical_url = %s LIMIT 1;
        """, (title, canonical_url))
        if cursor.fetchone():
            print(f"Skipping duplicate recipe: {title}")
            return  # Skip insertion if duplicate found

        # Generate a random hexadecimal ID
        id = uuid.uuid4().hex
        ingredients_str = ', '.join(scraper.ingredients())
        nutrients_dict = scraper.nutrients() if scraper.nutrients() else {}
        nutrients_str = ', '.join(f"{k}: {v}" for k, v in nutrients_dict.items())

        # Insert into recipes table
        cursor.execute("""
            INSERT INTO post_post (created_by_id, id, Created_at, host, title, total_time, image_url,
                        instructions, yields, meal_type, canonical_url, cuisine_type, ingredients, nutrients)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            created_by_id, id, Created_at, scraper.host(), title, scraper.total_time(), scraper.image(),
            scraper.instructions(), scraper.yields(), scraper.category() if scraper.category() else "Not available",
            canonical_url, scraper.cuisine() if scraper.cuisine() else "Not available", ingredients_str, nutrients_str
        ))

    except Exception as e:
        print(f"Error during database operation: {e}")
    finally:
        db.commit()
        cursor.close()
        db.close()

def scrape_recipe(url):
    scraper = scrape_me(url)
    insert_recipe_data(scraper)

def read_urls_and_scrape(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                url = row[2]  # Assuming the URL is in the first column of each row
                print(f"Scraping recipe from URL: {url}")
                scrape_recipe(url)
            except Exception as e:
                print(f"Error scraping {url}: {e}")

def fetch_all_recipe_urls(base_url):
    urls = set()
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Finding category links
    category_links = [a['href'] for a in soup.find_all('a', href=True) if '/recipes/' in a['href']]
    for link in category_links:
        urls.update(fetch_recipe_urls_from_category(link))
    
    return list(urls)

def fetch_recipe_urls_from_category(category_url):
    urls = set()
    while category_url:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all recipe links on the current page
        urls.update([link['href'] for link in soup.find_all('a', href=True) if link['href'].startswith('https://www.allrecipes.com/recipe/')])

        # Find next page link
        next_page = soup.find('a', class_='next-link')
        category_url = next_page['href'] if next_page and 'href' in next_page.attrs else None
        time.sleep(1)  # Sleep to respect rate limits and avoid getting blocked

    return urls

def main_scrape_function():
    base_url = "https://www.food.com/recipe/"
    recipe_urls = fetch_all_recipe_urls(base_url)
    for url in recipe_urls:
        print(f"Scraping recipe from URL: {url}")
        try:
            scrape_recipe(url)
        except Exception as e:
            print(f"Error scraping {url}: {e}")
        time.sleep(1)  # Adding delay to prevent rapid requests

# Example usage
if __name__ == "__main__":
    # recipe_url = "https://www.allrecipes.com/agua-fresca-de-fresas-con-crema-strawberries-and-cream-recipe-7560919"
    # scrape_recipe(recipe_url)
    # csv_file_path = "sampleurls.csv"
    # read_urls_and_scrape(csv_file_path)
    main_scrape_function()
