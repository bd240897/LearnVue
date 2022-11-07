<template>
  <div>

    <div class="menu_burger" v-on:click='showDropdown'>
      <div class="">
        <img class="menu_burger__icon" src="@/assets/icons/hamburger.png">
      </div>
    </div>

    <div v-if="isShowDropdown">
      <section class="menu_screen">
        <div class="menu_screen__container">
          <div class="menu_screen__body  w-50 py-3">
            <div class="menu d-flex flex-column align-items-center">
              <h3 class="my-2">Меню</h3>

              <router-link :to="{ name: 'Login'}" custom v-slot="{ navigate }">
                <div role="link" v-on:click="navigate(); showDropdown()"  class="menu__element my-2 text-center w-75">Login</div>
              </router-link>

              <router-link :to="{ name: 'RequestCreate'}" custom v-slot="{ navigate }">
                <div role="link" v-on:click="navigate(); showDropdown()" class="menu__element my-2 text-center w-75">RequestCreate</div>
              </router-link>

              <router-link :to="{ name: 'RequestDetail', params: { id: 1 }}" custom v-slot="{ navigate }">
                <div role="link" v-on:click="navigate(); showDropdown()" class="menu__element my-2 text-center w-75">RequestDetail</div>
              </router-link>

              <router-link :to="{ name: 'RequestList'}" custom v-slot="{ navigate }">
                <div role="link" v-on:click="navigate(); showDropdown()" class="menu__element my-2 text-center w-75">RequestList</div>
              </router-link>

              <router-link :to="{ name: 'TestView', params: { id: 1 }}" custom v-slot="{ navigate }">
                <div role="link" v-on:click="navigate(); showDropdown()" class="menu__element my-2 text-center w-75">TestView</div>
              </router-link>

              <button v-on:click='showDropdown' class="menu_screen__button btn btn-success" type="button">X</button>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Menu',
  data() {
    return {
      isShowDropdown: false,
    }
  },
  methods: {
    showDropdown() {
      this.isShowDropdown = !this.isShowDropdown
    },
  },
}
</script>

<style scoped>

/* Настройки нопки */

.menu_burger {
  position: relative;
}

.menu_burger__icon{
  height: 30px;
  width: 30px;
    position: absolute;
    top: 10px;
    right: 10px;
}

/* Модальное окно с меню */

.menu_screen {
  display: block;
}

.menu_screen__container {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.8);
}

.menu_screen__body {
  /*width: 300px;*/
  /*min-height: 180px;*/
  background-color: white;
}

/* Custom styles */
.menu_screen__container {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>