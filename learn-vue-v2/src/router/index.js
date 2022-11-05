import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import RequestList from '../views/RequestList.vue'
import Request from '../views/Request.vue'
import CreateRequest from '../views/CreateRequest.vue'
import TestView from "../views/TestView";

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/request/list',
    name: 'RequestList',
    component: RequestList
  },
  {
    path: '/request/look',
    name: 'Request',
    component: Request
  },
  {
    path: '/request/create',
    name: 'CreateRequest',
    component: CreateRequest
  },
  {
  path: '/test',
  name: 'TestView',
  component: TestView
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
