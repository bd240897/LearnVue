<template>
  <div>
    <h1>req</h1>
    {{img_url}}
  </div>
  <img v-bind:src="img_url" />
</template>

<script>
import axios from "axios";

import { mapState, mapActions } from "vuex";
export default {
  name: "Request",
  data(){
    return {
      // img_url: ''
    }
  },
  computed: {
    ...mapState('request', ['img_url',]),
    ...mapState('create_request', ['img_id',]),
  },
  methods: {
    ...mapActions('request', ['getImg',])
  },
  created() {
    // let id = this.$store.state.id_request
    // console.log(id)

    let id = this.img_id
    this.getImg({id:id});
  }
}
</script>

<style scoped>

</style>