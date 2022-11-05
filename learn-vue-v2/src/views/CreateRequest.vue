<template>
  <div>
    <h1>create req</h1>
    <div class="container">
      <div class="large-12 medium-12 small-12 cell">
        <label>File
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        </label>
        <button v-on:click="submitFile()">Submit</button>
      </div>
    </div>
  </div>

</template>

<script>
import axios from "axios";
import {mapActions} from "vuex";

export default {
  name: "CreateRequest",
  data(){
    return {
      file: ''
    }
  },
  methods: {
    ...mapActions("create_request", ["sendImg"]),

    handleFileUpload(){
      this.file = this.$refs.file.files[0];
    },

    submitFile(){
      let formData = new FormData();
      formData.append('file', this.file);

      this.sendImg({formData:formData})
    },
  }
}
</script>

<style scoped>

</style>