import axios from "axios";

export default ({
    namespaced: true,
    state() {
        return {
            img_list: [],
        }
    },
    getters: {
    },
    actions: {
        getImgList({commit, rootState},  { url=this.state.URL_BACKEND_GET_LIST_REQUEST, }) {
            axios.get(url)
                .then(function(x){
                    console.log(x.data)
                    console.log('SUCCESS!!');

                    commit('SET_RECEIVED_IMG_LIST', x.data)
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
        SET_RECEIVED_IMG_LIST (state, img_list) {
            state.img_list = img_list
        },
    },
})
