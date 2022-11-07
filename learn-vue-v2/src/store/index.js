import { createStore } from 'vuex'
import request_list from "./modules/request_list/";
import request_detail from "./modules/request_detail/";
import login from "./modules/login/";
import request_create from "./modules/request_create/";

export default createStore({
  state() {
    return {
      id_request: '18',
      URL_BACKEND_GET_IMG: 'http://127.0.0.1:8000/api/receive/source/',
      URL_BACKEND_SEND_IMG: 'http://127.0.0.1:8000/api/upload/',
      URL_BACKEND_GET_LIST_REQUEST: 'http://127.0.0.1:8000/api/list/',
    }
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    request_list,
    request_detail,
    login,
    request_create,
  }
})
