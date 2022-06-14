# update ADL dataProcessRegion
curl -u "username:apiKey" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --request PATCH "https://cloud.mongodb.com/api/atlas/v1.0/groups/{GROUP-ID}/dataLakes/{NAME}?pretty=true"
 --data '{
   "cloudProviderConfig" : {
     "aws" : {
       "roleId" : "1a234bcd5e67f89a12b345c6",
       "testS3Bucket" : "user-metric-data-bucket"
     }
   },
   "dataProcessRegion" : {
     "cloudProvider" : "AWS",
     "region" : "OREGON_USA"
   }
 }'