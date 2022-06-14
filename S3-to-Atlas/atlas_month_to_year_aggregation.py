from datetime import datetime
from pymongo import MongoClient
import s3_to_atlas_pipeline_template

# connection to ADL
client = MongoClient('<ADL_connection_string>')
db = client.get_database("ADL_db_name")
coll = db.get_collection("ADL_col_name")

# Load pipeline definition
pipeline = s3_to_atlas_pipeline_template.pipeline

# Track start datetime 
start_datetime = datetime.now()
print("Started the aggregation in ADL at {0}".format(
    datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f'))
)

# execute aggregation pipeline
print("Process aggregation and write to Atlas DB Cluster....")
coll.aggregate(pipeline)

# Track end datetime
end_datetime = datetime.now()
print("Complete the aggregation in ADL at {0} in {1} seconds"
    .format(
        datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f'),
        (end_datetime-start_datetime).total_seconds()
    )
)