# УРЛЫ

##### URL_BACKEND_GET_IMG
        URL: 'http://127.0.0.1:8000/api/expose/',
        TYPE: GET
        REQUEST PARAMS:
            {
                id: 16
            }
        RESPONSE SUCCESS:
            {
                "id": 12,
                "data": 
                "img": "http://link/name.JPG"
            }
##### URL_BACKEND_SEND_IMG
        URL: 'http://127.0.0.1:8000/api/upload/',
        TYPE: POST
        REQUEST PARAMS:
            {
            file: fule
            }
        RESPONSE SUCCESS:
            {
                "id": 10
            }
##### URL_BACKEND_GET_LIST_REQUEST
        URL: '',
        TYPE: POST
        REQUEST PARAMS:
            {

            }
        RESPONSE SUCCESS:
            {
                "list": [
                    {                
                        "id": 12,
                        "data": 
                        "img": "http://link/name.JPG"
                    },
                                    {                
                        "id": 13,
                        "data": 
                        "img": "http://link/name.JPG"
                    },
                ]
            }

# BACKEND