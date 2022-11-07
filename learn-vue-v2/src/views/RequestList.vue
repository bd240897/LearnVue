<template>
<!--  <h1>req list</h1>-->
<!--  {{img_list}}-->
  <section class="request_list h-100">

    <div class="container h-100">
      <div class="row h-100 justify-content-center align-items-center p-0 ">

        <div class="list__col col-8 bg-white border p-4">


          <h3 class="list_header text-center mb-3">Список запросов</h3>

          <div class="list_body">

            <div class="request mb-4">
              <div class="row mx-1 py-2">

                <div class="col-md-1 col-sm-2 col-2 request__text request__text__number">
                  #1
                </div>
                <div class="col-md-5 col-sm-10 col-10 request__text request__text__name">
                  Название запроса
                </div>
                <div class="col-md-3 col-sm-1 request__text request__text__date">
                  10.10.2010
                </div>
                <div class="col-md-3 col-sm-1 request__text request__text__status">
                  Обработано
                </div>
              </div>
            </div>

            <div class="request mb-4">
              <div class="row mx-1 py-2">

                <div class="col-md-1 col-sm-2 col-2 request__text request__text__number">
                  #1
                </div>
                <div class="col-md-5 col-sm-10 col-10 request__text request__text__name">
                  Название запроса
                </div>
                <div class="col-md-3 col-sm-1 request__text request__text__date">
                  10.10.2010
                </div>
                <div class="col-md-3 col-sm-1 request__text request__text__status">
                  Обработано
                </div>
              </div>
            </div>

            <div class="request mb-4">
              <div class="row mx-1 py-2">

                <div class="col-md-1 col-sm-2 col-2 request__text request__text__number">
                  #1
                </div>
                <div class="col-md-5 col-sm-10 col-10 request__text request__text__name">
                  Название запроса
                </div>
                <div class="col-md-3 col-sm-1 request__text request__text__date">
                  10.10.2010
                </div>
                <div class="col-md-3 col-sm-1 request__text request__text__status">
                  Обработано
                </div>
              </div>
            </div>
          </div>

          <div class="list_pagination d-flex justify-content-center">
            <nav aria-label="...">
              <ul class="pagination">
                <li class="page-item active" aria-current="page">
                  <span class="page-link">1</span>
                </li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
              </ul>
            </nav>
          </div>


          <div class="d-grid">
            <button class="list_button btn btn-success" type="button">Создать новую заявку</button>
          </div>

        </div>
      </div>
    </div>
  </section>
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
  @import "../assets/css/request_list.css";
</style>