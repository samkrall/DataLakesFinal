# Data Lakes Final README

General Plan


•	Collection
    o	Data Source: (https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2025/index.html)
    o	Orchestration: NiFi
    o	Raw Data Storage: AWS S3
•	Preparation
    o	Transformation: PySpark
        	Removal of Duplicate Datapoints
        	Datatype Decisions
        	Aggregations
        	Flags for when a ship is in port to distinguish “voyages”
    o	Mllib
•	Analysis (3 questions)
    o	What is the breakdown between international shipping and US only shipping? Are their other modes of US transport that this dataset is not capturing?
    o	What are America’s busiest ports?
    o	Can you group routes into specific routes?
    o	Can you group ships into specific ships?
•	Visualization (Seaborn and/or Matplotlib?)
    o	Voyages by month (bar)
    o	Datapoints per month (pie)
    o	Distance travelled per day
    o	Count of distinct ships per month
    o	Longest time sitting still
