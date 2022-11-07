<template>
<!--  <div>-->
<!--    <h1>req</h1>-->
<!--    {{img_url}}-->
<!--  </div>-->
<!--  <img v-bind:src="img_url" />-->
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

              <div class="block_img container-fluid mb-3">

                <div class="block_img__body row">
                  <div class="col-6">
                    <h5 class="img_head text-center">Исходное фото</h5>
                    <div>
                      <img class="img_item" src="@/assets/img/starfield.png">
                    </div>
                  </div>
                  <div class="col-6">
                    <h5 class="img_head text-center">Обработанное</h5>
                    <div>
                      <img class="img_item" src="@/assets/img/starfield.png">
                    </div>
                  </div>
                </div>

              </div>

              <div class="block_text container-fluid mb-3">
                <div class="block_text__body row ">

                  <div class="d-flex justify-content-between">
                    <p class="block_text__user">Пользователь: Amid</p>
                    <p class="block_text__data">Дата: 10.10.2010 17:35</p>
                  </div>

                  <div>
                    <p>Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                      Duis mollis, est non commodo luctus. Vivamus sagittis lacus vel augue
                      laoreet rutrum faucibus dolor auctor. Vivamus sagittis lacus vel augue
                      laoreet rutrum faucibus dolor auctor. Duis mollis, est non commodo luctus.
                      Vivamus sagittis lacus vel augue
                      Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                      Duis mollis, est non commodo luctus. Vivamus sagittis lacus vel augue
                      laoreet rutrum faucibus dolor auctor. Vivamus sagittis lacus vel </p>
                  </div>
                </div>
              </div>

              <div class="block_button container-fluid mb-3">
                <div class="block_button__body row justify-content-between">
                  <div class="col-2">
                    <button class="create_body__button btn btn-success" type="button">Предыдущий
                    </button>
                  </div>
                  <div class="col-2">
                    <button class="create_body__button btn btn-success" type="button">Отметить</button>
                  </div>
                  <div class="col-2">
                    <button class="create_body__button btn btn-success" type="button">Следующий</button>
                  </div>
                </div>
              </div>
            </div>
          </div>


        </div>
      </div>
    </div>
  </section>

  <section class="menu_screen">
    <div class="menu_screen__container">
      <div class="menu_screen__body  w-50 py-3">
        <div class="menu d-flex flex-column align-items-center">
          <h3 class="my-2">Меню</h3>

          <div class="menu__element my-2 text-center w-75">
            Пункт 1
          </div>
          <div class="menu__element my-2 text-center w-75">
            Пункт 1
          </div>
          <div class="menu__element my-2 text-center w-75">
            Пункт 1
          </div>
          <button class="menu_screen__button btn btn-success" type="button">X</button>
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

export default {
  name: "RequestDetail",
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
  },
  mounted() {
    $(function() {
      console.log( "ready!" );
      $(".menu__element").click(function () {
        $(".menu_screen").show()
      });

      $(".menu_screen__button").click(function () {
        $(".menu_screen").hide()
      });
    })
  }
}


</script>

<style scoped>
  @import "../assets/css/request_detail.css";
</style>