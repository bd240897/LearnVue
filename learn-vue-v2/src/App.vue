<template>
  <nav>
    <router-link :to="{ name: 'Login'}">Login</router-link> |
    <router-link :to="{ name: 'RequestCreate'}">CreateRequest</router-link> |
    <router-link :to="{ name: 'RequestDetail', params: { id: 1 }}">Request</router-link> |
    <router-link :to="{ name: 'RequestList'}">RequestList</router-link> |
    <router-link :to="{ name: 'TestView', params: { id: 1 }}">TestView</router-link> |
  </nav>
  <router-view/>
</template>

<style>
  /*необходимо для центрации дочерних элементов по середине экрана*/
  html, body {
    height: 100%;
  }

  #app{
    height: 100%;
  }

  #app{
    background-color: #6BA3F6;
  }

</style>
