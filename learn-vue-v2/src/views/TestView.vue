<template>
  <div>
    <button class="btn btn-primary"
            data-bs-target="#collapseTarget"
            data-bs-toggle="collapse">
      Bootstrap collapse
    </button>
    <div class="collapse py-2" id="collapseTarget">
      This is the toggle-able content!
    </div>
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
    this.getImg({id:10});
  },

  methods: {
    ...mapActions("request", ["getImg"]),
  }
}
</script>




<style scoped>

</style>