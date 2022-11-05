// import axios from "axios";
const axios = require('axios');

let url = 'http://127.0.0.1:8000/api/test'

axios.get(url)
    .then(res => {
        console.log("do good things")
        console.log(res.data)
    })
.catch(err => {
    if (err.response) {
        console.log("client received an error response (5xx, 4xx)")
    } else if (err.request) {
        console.log("client never received a response, or request never left")
    } else {
        console.log("anything else ")
    }
})