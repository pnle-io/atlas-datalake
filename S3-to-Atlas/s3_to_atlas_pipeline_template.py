
pipeline = [{
        '$project': {
            'year': 1, 
            'VendorID': { '$concat': [ 'vendor_', '$VendorID' ] }, 
            'fare_amount': {
                '$cond': {
                    'if': {
                        '$eq': [
                            '', '$fare_amount'
                        ]
                    }, 
                    'then': 0, 
                    'else': '$fare_amount'
                }
            }, 
            'passenger_count': {
                '$cond': {
                    'if': {
                        '$eq': [
                            '', '$passenger_count'
                        ]
                    }, 
                    'then': 0, 
                    'else': '$passenger_count'
                }
            }, 
            'total_amount': {
                '$cond': {
                    'if': {
                        '$eq': [
                            '', '$total_amount'
                        ]
                    }, 
                    'then': 0, 
                    'else': '$total_amount'
                }
            }, 
            'trip_distance': {
                '$cond': {
                    'if': {
                        '$eq': [
                            '', '$trip_distance'
                        ]
                    }, 
                    'then': 0, 
                    'else': '$trip_distance'
                }
            }
        }
    }, {
        '$group': {
            '_id': '$VendorID', 
            'total_fare_amount': {
                '$sum': {
                    '$toDecimal': '$fare_amount'
                }
            }, 
            'total_passenger_count': {
                '$sum': {
                    '$toDecimal': '$passenger_count'
                }
            }, 
            'total_amount': {
                '$sum': {
                    '$toDecimal': '$total_amount'
                }
            }, 
            'total_trip_distance': {
                '$sum': {
                    '$toDecimal': '$trip_distance'
                }
            }, 
            'avg_fare_amount': {
                '$avg': {
                    '$toDecimal': '$fare_amount'
                }
            }, 
            'avg_passenger_count': {
                '$avg': {
                    '$toDecimal': '$passenger_count'
                }
            }, 
            'avg_amount': {
                '$avg': {
                    '$toDecimal': '$total_amount'
                }
            }, 
            'avg_trip_distance': {
                '$avg': {
                    '$toDecimal': '$trip_distance'
                }
            }
        }
    },{
        "$out": { 
            "atlas": {
                "projectId": "<project_id>" ,
                "clusterName": "<cluster_name>",
                "db": "<output_db_name>",
                "coll": "<output_coll_name>" ,
            }
        }
    }
]