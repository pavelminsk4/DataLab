<template>
  <div @click="clickedOut">
    <div
      id="modal"
      class="base-modal-wrapper"
      aria-labelledby="Modal"
      aria-modal="true"
    >
      <div :style="modalFrameStyle" class="base-modal">
        <div class="base-modal-content">
          <button type="button" class="close" @click="close">
            <CrossIcon :class="closeIconClass" />
          </button>
          <div class="base-modal-body scroll">
            <slot></slot>
          </div>
        </div>
      </div>
    </div>
    <div class="base-modal-backdrop"></div>
  </div>
</template>

<script>
import CrossIcon from '@components/icons/CrossIcon'

export default {
  name: 'BaseModal',
  components: {CrossIcon},
  props: {
    closeIconClass: {type: String, default: ''},
    modalFrameStyle: {type: String, default: ''},
  },
  created() {
    document.addEventListener('keydown', this.pressedEsc)
    this.togglePageScroll(true)
  },
  beforeUnmount() {
    document.removeEventListener('keydown', this.pressedEsc)
  },
  methods: {
    clickedOut(e) {
      if (e.target.id === 'modal') this.close()
    },
    pressedEsc(evt) {
      switch (evt.key) {
        case 'Esc':
        case 'Escape':
          evt.preventDefault()
          this.close()
          break
        default:
          return undefined
      }
    },
    close() {
      this.togglePageScroll(false)
      this.$emit('close')
    },
  },
}
</script>

<style lang="scss" scoped>
.base-modal-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 105;

  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;

  width: 100%;
  height: 100%;
  min-height: 200px;

  outline: 0;
  transition: opacity 0.15s linear;

  background: rgba(0, 0, 0, 0.7);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
}

.base-modal {
  position: relative;

  display: flex;
  flex-direction: column;

  max-width: 90vw;
  max-height: 90vh;
  padding: 30px 50px 68px;

  background: var(--secondary-bg-color);
  pointer-events: none;
  transition: transform 0.3s ease-out;
}

@media (prefers-reduced-motion: reduce) {
  .base-modal {
    transition: none;
  }
}

.base-modal-content {
  position: relative;

  display: flex;
  flex-direction: column;
  overflow: hidden;

  width: 100%;
  height: 100%;

  background-color: #000000;
  background-clip: padding-box;
  border-radius: 10px;

  outline: 0;
  pointer-events: auto;
}

.base-modal-body {
  overflow-y: auto;

  height: 100%;
  width: 100%;

  background: var(--secondary-bg-color);
  color: var(--primary-text-color);
}

.base-modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 104;

  width: 100vw;
  height: 100vh;

  background-color: #787878;
  opacity: 0.9;
}

.close {
  position: absolute;
  top: 15px;
  right: 15px;
  z-index: 3;

  padding: 0;

  background-color: transparent;
  border: none;
  cursor: pointer;

  color: var(--primary-text-color);
}

@media (max-width: 767px) {
  .base-modal-content {
    height: auto;
  }
}
</style>
