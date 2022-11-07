import axios from "axios";
import moment from 'moment'

export default ({
    namespaced: true,
    state() {
        return {
            received_img: '',
            received_description: '',
            received_name: '',
            received_user: '',
            received_time: '',
        }
    },
    getters: {
    },
    actions: {
        loadData({commit, rootState},  {url=this.state.URL_BACKEND_GET_IMG, id}) {
            console.log(id)
            // let url= this.state.request.URL_GET_IMG

            axios.get(url, {params: {id: id}})
                .then(function(x){
                    console.log(x.data)
                    console.log('SUCCESS!!');

                    commit('SET_RECEIVED_IMG', x.data.img)
                    commit('SET_RECEIVED_DESCRIPTION', x.data.description)
                    commit('SET_RECEIVED_NAME', x.data.name)
                    commit('SET_RECEIVED_USER', x.data.user)
                    commit('SET_RECEIVED_TIME', x.data.time)

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
        SET_RECEIVED_IMG (state, received_img) {
            state.received_img = received_img
        },
        SET_RECEIVED_DESCRIPTION (state, received_description) {
            state.received_description = received_description
        },
        SET_RECEIVED_NAME (state, received_name) {
            state.received_name = received_name
        },
        SET_RECEIVED_USER (state, received_user) {
            state.received_user = received_user
        },
        SET_RECEIVED_TIME (state, received_time) {
            state.received_time = moment(received_time).format('MM.DD.YYYY')
        },
    },
})

