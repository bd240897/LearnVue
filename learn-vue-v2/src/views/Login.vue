<template>
  <section class="login h-100">
    <div class="container h-100">
      <div class="row h-100  justify-content-center align-items-center p-0 ">
        <div class="login__col col-4 bg-white border p-4">

          <h3 class="login__header text-center mb-2">Вход</h3>
          <form class="login__form">
            <div class="login__form__email form-group my-2">
              <label for="exampleInputEmail1">Username</label>
              <input v-model="username" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            </div>
            <div class="login__form__password form-group my-2">
              <label for="exampleInputPassword1">Пароль</label>
              <input v-model="password" type="password" class="form-control" id="exampleInputPassword1">
            </div>
            <button class="login__button btn btn-primary w-100" type="submit" >Войти</button>
          </form>

        </div>
      </div>
    </div>
  </section>

</template>

<script>
// import '../assets/css/login.css'
export default {
  name: "Login",
  data() {
    return {
      username: '',
      password: '',
    }
  },
}
</script>

<style scoped>
  @import "../assets/css/login.css";
</style>