<template>
  <section class="create_request h-100">

    <div class="container h-100">
      <div class="row h-100 justify-content-center align-items-center p-0">

        <div class="create__col col-8 bg-white border p-4">

          <h3 class="create_header text-center mb-3">Создать заявку</h3>

          <div class="create_body">
            <form>
              <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Название запроса</label>
                <input v-model="name" type="email" class=" create_body__name form-control" id="exampleFormControlInput1" placeholder="Мое собаке плохо">
              </div>
              <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">Описание</label>
                <textarea v-model="description" class="create_body__description form-control" id="exampleFormControlTextarea1" rows="3" placeholder="Не есть, не спит, не пьет"></textarea>
              </div>
              <div class="mb-3">
                <label for="file" class="form-label">Фотография</label>
                <input v-on:change="handleFileUpload()" class="create_body__file form-control" type="file" id="file" ref="file" multiple>
              </div>
              <div class="d-grid">
                <button v-on:click="submitFile()" class="create_body__button btn btn-success" type="button">Создать новую заявку</button>
              </div>
            </form>
          </div>

        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import {mapActions} from "vuex";

export default {
  name: "RequestCreate",
  data(){
    return {
      name: '',
      description: '',
      file: '',
    }
  },
  methods: {
    ...mapActions("request_create", ["sendData"]),

    handleFileUpload(){
      this.file = this.$refs.file.files[0];
    },

    submitFile(){
      let formData = new FormData();
      formData.append('file', this.file);

      if (this.description) {
        formData.append('description', this.description);
      }

      if (this.name) {
        formData.append('name', this.name);
      }

      this.sendData({formData:formData})
    },
  }
}
</script>

<style scoped>
  @import "../assets/css/request_create.css";
</style>