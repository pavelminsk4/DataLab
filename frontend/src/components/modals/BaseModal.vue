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
          <button type="button" class="close" @click="$emit('close')">
            <IconCross :class="closeIconClass" />
          </button>
          <div class="base-modal-body">
            <slot></slot>
          </div>
        </div>
      </div>
    </div>
    <div class="base-modal-backdrop"></div>
  </div>
</template>

<script>
import IconCross from '@components/icons/IconCross'

export default {
  name: 'BaseModal',
  components: {IconCross},
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
      if (e.target.id === 'modal') this.sendClose()
    },
    pressedEsc(evt) {
      switch (evt.key) {
        case 'Esc':
        case 'Escape':
          evt.preventDefault()
          this.sendClose()
          break
        default:
          return undefined
      }
    },
    sendClose() {
      this.togglePageScroll(false)
      this.$emit('close')
    },
    togglePageScroll(isOpen) {
      if (isOpen) {
        document.body.classList.add('overflow-hidden')
      } else {
        document.body.classList.remove('overflow-hidden')
      }
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
  padding: 30px 50px 68px;

  background: var(--secondary-bg-color);
  color: var(--primary-text-color);

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 0 10px 10px 0;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
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
