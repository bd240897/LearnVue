<template>
  <div v-if="!isMobile">
<!--    <desktop/>-->
      desktop
  </div>
  <div v-else>
<!--    <mobile/>-->
      mobile
  </div>
  {{isMobile}}
<!--  another aproach -->
<!--  <production-list v-if="!isMobile()"></production-list>-->
<!--  <production-list-mobile v-else></production-list-mobile>-->
</template>

<script>
export default {
  name: 'HeaderComponent',
  data() {
    return {
      width: 0,
    }
  },
  created() {
    window.addEventListener('resize', this.updateWidth);
  },
  methods: {
    // isMobile() {
    //   if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    //     return true
    //   } else {
    //     return false
    //   }
    // },
    updateWidth() {
      this.width = window.innerWidth;
    },

  },
  computed: {
    isMobile() {
      return this.width <= 760;
    },
  }
}
</script>

<style scoped>


</style>