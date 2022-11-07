import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import RequestList from '../views/RequestList.vue'
import RequestDetail from '../views/RequestDetail.vue'
import RequestCreate from '../views/RequestCreate.vue'
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
    name: 'RequestDetail',
    component: RequestDetail
  },
  {
    path: '/request/create',
    name: 'RequestCreate',
    component: RequestCreate
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
