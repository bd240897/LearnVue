<template>
  <section class="request_detail h-100">
    <div class="container d-flex h-100 justify-content-center align-items-center">

      <div class="container_white_bg w-100 bg-white border p-0">

        <div class="row">

          <div class="vertical_line col-3 d-flex justify-content-center ">
            <div class="menu w-75">

              <h3 class="my-2">Меню</h3>

              <div class="menu__element my-2 text-center">
                Пункт 1
              </div>
              <div class="menu__element my-2 text-center">
                Пункт 1
              </div>
              <div class="menu__element my-2 text-center">
                Пункт 1
              </div>
            </div>
          </div>

          <div class="col-9 ps-0">
            <div class="info">

              <h3 class="info__header text-center my-2">Подробности заявки</h3>
              <h4 class="info__header text-center my-2"> Имя заявки: {{received_name}} </h4>
              <div class="block_img container-fluid mb-3">

                <div class="block_img__body row">
                  <div class="col-6">
                    <h5 class="img_head text-center">Исходное фото</h5>
                    <div>
                      <img class="img_item" v-bind:src="received_img">
                    </div>
                  </div>
                  <div class="col-6">
                    <h5 class="img_head text-center">Обработанное</h5>
                    <div>
                      <img class="img_item" src="">
                    </div>
                  </div>
                </div>

              </div>

              <div class="block_text container-fluid mb-3">
                <div class="block_text__body row ">

                  <div class="d-flex justify-content-between">
                    <p class="block_text__user">Пользователь: {{received_user}}</p>
                    <p class="block_text__data">Дата: {{received_time}}</p>
                  </div>

                  <div>
                    <p> {{received_description}} </p>
                  </div>
                </div>
              </div>

              <div class="block_button container-fluid mb-3">
                <div class="block_button__body row justify-content-between">
                  <div class="col-2">
                    <button v-on:click="previousRequest" class="create_body__button btn btn-success" type="button">Предыдущий</button>
                  </div>
                  <div class="col-2">
                    <button class="create_body__button btn btn-success" type="button">Отметить</button>
                  </div>
                  <div class="col-2">
                    <button v-on:click="nextRequest" class="create_body__button btn btn-success" type="button">Следующий</button>
                  </div>
                </div>
              </div>
            </div>
          </div>


        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import { mapState, mapActions } from "vuex";
// import "../assets/js/request_detail.js";
import $ from "jquery";
import router from "@/router";

export default {
  name: "RequestDetail",
  data(){
    return {
    }
  },
  created() {
    this.loadData({id:this.id});
  },
  computed: {
    ...mapState('request_detail', ['received_img', 'received_description', 'received_name', "received_user", "received_time"]),
    id() {
      return this.$route.params.id
    },
  },
  methods: {
    ...mapActions('request_detail', ['loadData']),
    nextRequest(){
      let newId = parseInt(this.id) + 1
      this.$router.push({ name: 'RequestDetail', params: { id: newId }})
    },
    previousRequest(){
      let newId = parseInt(this.id) - 1
      if (newId <=0) {return 0}
      this.$router.push({ name: 'RequestDetail', params: { id: newId }})
    },
  },
  watch: {
    "$route.params.id": {
      handler() {
        this.loadData({id:this.id});
      }
    },
  },
  mounted() {
  },
}


</script>

<style scoped>
  @import "../assets/css/request_detail.css";
</style>