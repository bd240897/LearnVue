<template>
  <nav>
    <router-link :to="{ name: 'Login'}">Login</router-link> |
    <router-link :to="{ name: 'CreateRequest'}">CreateRequest</router-link> |
    <router-link :to="{ name: 'Request'}">Request</router-link> |
    <router-link :to="{ name: 'RequestList'}">RequestList</router-link> |
    <router-link :to="{ name: 'TestView'}">TestView</router-link> |
  </nav>
  <router-view/>
</template>

<style>

</style>
