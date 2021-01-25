# Plans
## About this project:
My aim with this project is to create a whole B2C data governance architecture. From transactional data to social media and PPC data in one data warehouse. I think this can be really valuable since companies usually hire a whole consulting team for only one of this tasks.
Below we can see more specifications about the project with a Schema for the finished project.


### Technologies:
 - Scripting: 
     - Python
 - Querying:
     - SQL 
 - Pipeline:
     - Apache Airflow
 - Infrastructure:
      - Storage:
          - S3 Bucket
      - Computing:
          - Redshift for data warehousing

### Data for the project:

- Retail/Ecommerce data:
    - Place all the data inside an S3 bucket so that it mimics a transactional database.
    - Create business oriented tables.
    - Insert queries that process the data before pushing it to the data warehouse.
    - Create tests that suits this type of data.
    
- Social Media data:
    - Instagram, Twitter or TikTok.
    - Pull raw social media data via an existing API or a scraper made by me into an S3 bucket.
    - Create business oriented tables.
    - Insert queries that filter the data or clean with python.
    - Create tests that suits this type of data.
    
- Advertising Data:
    - Facebook Ads, Google Ads or Linkedin Ads.
    - Pull data from those platforms using Singer.io
    - Create business oriented tables.
    - Create various that suits this type of data.
    
### Analysis
- Do a simple Top Line report for the whole company using all the tables. Very basic and fast to read.
- Analyse best products per season.
- Create a simple report that rapidly identifies the best ads and which platform are they coming from.
- Identify a pattern in the social media behaviour.
