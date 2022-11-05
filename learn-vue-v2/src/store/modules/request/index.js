import axios from "axios";

export default ({
    namespaced: true,
    state() {
        return {
            img_url: '',
        }
    },
    getters: {
    },
    actions: {
        getImg({commit, rootState},  {url=this.state.URL_BACKEND_GET_IMG, id}) {
            console.log(id)
            // let url= this.state.request.URL_GET_IMG

            axios.get(url, {params: {id: id}})
                .then(function(x){
                    console.log(x.data)
                    console.log('SUCCESS!!');

                    commit('SET_RECEIVED_IMG', x.data.img)
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
                    return err
                })
        },
    },
    mutations: {
        SET_RECEIVED_IMG (state, img_url) {
            state.img_url = img_url
        },
    },
})

