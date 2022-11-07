import axios from "axios";
// import app from '../../../main.js'

import router from '../../../router'


export default ({
    namespaced: true,
    state() {
        return {
            img_id: '3',
        }
    },
    getters: {
    },
    actions: {
        sendImg({commit, rootState},  {url=this.state.URL_BACKEND_SEND_IMG, formData}){


            axios.post( url, formData, {headers: {'Content-Type': 'multipart/form-data'}})
                .then(function(x){
                    console.log(x.data)
                    console.log('SUCCESS!!');

                    commit('SET_ID_IMG', x.data.id)
                    // router.push({ name: 'Request'})
                    // _this.$store.state.id_request = x.data.id
                    // _this.$router.push({ name: 'Request' })
                })
                .catch(err => {
                    console.log(err)
                    if (err.response) {
                        console.log("client received an error response (5xx, 4xx)")
                    } else if (err.request) {
                        console.log("client never received a response, or request never left")
                    } else {
                        console.log("anything else ")
                    }
                })
        },
    },
    mutations: {
        SET_ID_IMG (state, img_id) {
            state.img_id = img_id
        },
    },
})
