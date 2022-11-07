import { createStore } from 'vuex'
import request_list from "./modules/request_list/";
import request from "./modules/request/";
import login from "./modules/login/";
import create_request from "./modules/create_request/";

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
    request,
    login,
    create_request,
  }
})
