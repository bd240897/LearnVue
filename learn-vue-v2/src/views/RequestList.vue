<template>
  <h1>req list</h1>
  {{img_list}}
</template>



<script>

import {mapActions, mapState} from 'vuex'
export default {
  name: "RequestList",
  computed: {
    ...mapState('request_list', ['img_list',]),
  },
  methods: {
    ...mapActions('request_list', ['getImgList',])
  },
  created() {
    this.getImgList({});
  }
}
</script>

<style scoped>

</style>