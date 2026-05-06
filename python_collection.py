# install dependencies using the following code, copy without # into the terminall
# pip install boto3 httpx

# import statements
import boto3
import httpx
import io
import time
from datetime import date, timedelta
import calendar

# set bucket, url with data, and s3
bucket = "seis-745-final-bronze"
base_url = "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2025/"
s3 = boto3.client("s3")

# check if uploaded
def already_uploaded(s3_key):
    try:
        s3.head_object(Bucket=bucket, Key=s3_key)
        return True
    except:
        return False
# attempt to upload, 3 tries
def upload_day(d: date, retries=3):
    filename = f"ais-{d.isoformat()}.csv.zst"
    s3_key = f"ais/{d.strftime('%B')}/{filename}"
    if already_uploaded(s3_key):
        print(f"{filename} already in S3")
        return
    for attempt in range(retries):
        try:
            print(f"Downloading {filename} (attempt {attempt+1})...")
            with httpx.stream("GET", base_url + filename, timeout=300) as r:
                r.raise_for_status()
                raw = b"".join(r.iter_bytes())
            print(f"Uploading to s3://{bucket}/{s3_key}...")
            s3.upload_fileobj(io.BytesIO(raw), bucket, s3_key)
            print("DONE")
            return
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(10)
    print(f"Giving up on {d}")

# for each date, try uploading into S3
year = 2025
for month in range(1, 13):
    _, num_days = calendar.monthrange(year, month)
    days = [date(year, month, 1) + timedelta(n) for n in range(num_days)]
    for day in days:
        upload_day(day)

print('script complete')
