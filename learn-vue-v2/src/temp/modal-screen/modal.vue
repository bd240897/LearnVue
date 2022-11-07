<script>
export default {
  name: 'modal',
  methods: {
    close() {
      this.$emit('close');
    },
  },
};
</script>

<template>
  <div class="">
    <transition name="modal-fade-v2">
      <div class="modal-backdrop-v2">
        <div class="modal-v2"
             role="dialog"
             aria-labelledby="modalTitle"
             aria-describedby="modalDescription"
        >
          <header
              class="modal-header-v2"
              id="modalTitle"
          >
            <slot name="header">
              This is the default tile!

              <button
                  type="button"
                  class="btn-close"
                  @click="close"
                  aria-label="Close modal"
              >
                x
              </button>
            </slot>
          </header>
          <section
              class="modal-body-v2"
              id="modalDescription"
          >
            <slot name="body">
              I'm the default body!
            </slot>
          </section>
          <footer class="modal-footer-v2">
            <slot name="footer">
              I'm the default footer!

              <button
                  type="button"
                  class="btn-green"
                  @click="close"
                  aria-label="Close modal"
              >
                Close me!
              </button>
            </slot>
          </footer>
        </div>
      </div>
    </transition>
  </div>
</template>

<style>
.modal-backdrop-v2 {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-v2 {
  background: #FFFFFF;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
}

.modal-header-v2,
.modal-footer-v2 {
  padding: 15px;
  display: flex;
}

.modal-header-v2 {
  border-bottom: 1px solid #eeeeee;
  color: #4AAE9B;
  justify-content: space-between;
}

.modal-footer-v2 {
  border-top: 1px solid #eeeeee;
  justify-content: flex-end;
}

.modal-body-v2 {
  position: relative;
  padding: 20px 10px;
}

.btn-close {
  border: none;
  font-size: 20px;
  padding: 20px;
  cursor: pointer;
  font-weight: bold;
  color: #4AAE9B;
  background: transparent;
}

.btn-green {
  color: white;
  background: #4AAE9B;
  border: 1px solid #4AAE9B;
  border-radius: 2px;
}
</style>
