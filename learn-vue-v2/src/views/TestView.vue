<template>
  <div>
    {{this.$route.params.id}}
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  name: "TestView",

  data() {
    return {
    };
  },

  computed: {
  },

  mounted() {
  },

  methods: {
  }
}
</script>




<style scoped>

</style>