from funding_scraper.sources import sample_item
from funding_scraper.sheets_push import push_rows

def main():
    rows = [sample_item()]
    print("Sample rows:", rows)
    # push_rows(rows)  # uncomment after Google Sheets setup

if __name__ == "__main__":
    main()
