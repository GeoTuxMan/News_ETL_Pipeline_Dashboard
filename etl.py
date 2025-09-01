from extract import extract
from transform import transform
from load import save_to_db

def run_etl_pipeline():
    print("Extracting articles...")
    df = extract()
    
    print("Transforming data...")
    df = transform(df)
    
    print("Loading to database...")
    save_to_db(df)
    
    print("ETL pipeline completed! Articles saved to news.db")

if __name__ == "__main__":
    run_etl_pipeline()
