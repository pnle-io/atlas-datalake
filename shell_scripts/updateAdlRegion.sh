# update ADL dataProcessRegion
curl -u "username:apiKey" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --request PATCH "<api_url>"
 --data '{
   "cloudProviderConfig" : {
     "aws" : {
       "roleId" : "<role_id>",
       "<adl-name>" : "user-metric-data-bucket"
     }
   },
   "dataProcessRegion" : {
     "cloudProvider" : "AWS",
     "region" : "OREGON_USA"
   }
 }'