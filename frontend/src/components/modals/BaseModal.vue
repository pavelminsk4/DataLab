<template>
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
          <div class="title">{{ title }}</div>
          <div class="content">
            <slot></slot>
          </div>
        </div>
      </div>
    </div>
    <div class="base-modal-backdrop" @click="close"></div>
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
    title: {type: String, default: ''},
    isGeneralPadding: {type: Boolean, default: true},
  },
  created() {
    document.addEventListener('keydown', this.pressedEsc)
    this.togglePageScroll(true)
  },
  beforeUnmount() {
    document.removeEventListener('keydown', this.pressedEsc)
  },
  methods: {
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
  --base-modal-content-padding: 24px;

  position: fixed;
  top: 0;
  left: 0;
  z-index: 104;

  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;

  width: 100vw;
  height: 100vh;
}

.base-modal {
  position: relative;
  z-index: 105;

  display: flex;
  flex-direction: column;

  max-width: 90vw;
  max-height: 90vh;

  background: var(--background-secondary-color);
  border-radius: 8px;
  box-shadow: 1px 4px 10px rgba(135, 135, 135, 0.2);
  transition: transform 0.3s ease-out;
}

.title {
  padding: 12px 24px;

  border-bottom: 1px solid var(--border-color);

  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 28px;
  color: var(--typography-title-color);
}

.content {
  padding: var(--base-modal-content-padding);
}

@media (prefers-reduced-motion: reduce) {
  .base-modal {
    transition: none;
  }
}

.base-modal-content {
  display: flex;
  flex-direction: column;
  overflow: hidden;

  width: 100%;
  height: 100%;

  border-radius: 8px;
  background-color: var(--background-secondary-color);
  background-clip: padding-box;

  outline: 0;
  pointer-events: auto;
}

.base-modal-body {
  overflow-y: auto;

  height: 100%;
  width: 100%;

  background: var(--background-secondary-color);
  color: var(--typography-primary-color);
}

.base-modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 104;

  width: 100vw;
  height: 100vh;

  opacity: 0.8;
  background: var(--background-primary-color);
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

  color: var(--typography-primary-color);
}

@media (max-width: 767px) {
  .base-modal-content {
    height: auto;
  }
}
</style>
