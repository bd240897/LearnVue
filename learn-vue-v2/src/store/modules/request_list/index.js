import axios from "axios";
import moment from 'moment'

export default ({
    namespaced: true,
    state() {
        return {
            data: [],
        }
    },
    getters: {},
    actions: {
        getDataList({commit, rootState}, {url = this.state.URL_BACKEND_GET_LIST_REQUEST,}) {
            axios.get(url)
                .then(function (x) {
                    console.log(x.data)
                    console.log('SUCCESS!!');

                    commit('SET_RECEIVED_DATA_LIST', x.data)
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
        // correctTime({commit, rootState}, time="2022-11-05T00:40:53.527308+03:00") {
        //     return moment(time).format('MM.DD.YYYY')
        // },
    },

    mutations: {
        SET_RECEIVED_DATA_LIST(state, data) {
            state.data = data
        },
    },
})
