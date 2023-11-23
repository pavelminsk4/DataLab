<template>
  <div
    class="flash-message"
    @mouseenter="removeTimer"
    @mouseleave="createTimer(2)"
  >
    <CrossIcon class="close-button" @click="close" />

    <div class="title">{{ title }}</div>

    <div class="message">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import CrossIcon from '@components/icons/CrossIcon'

export default {
  name: 'BaseFlashMessage',
  components: {CrossIcon},
  props: {
    title: {type: String, default: ''},
  },
  data() {
    return {
      timerId: 0,
    }
  },
  created() {
    this.createTimer(5)
  },
  methods: {
    close() {
      this.$emit('close')
    },
    createTimer(seconds) {
      this.timerId = setTimeout(this.close, seconds * 1000)
    },
    removeTimer() {
      clearTimeout(this.timerId)
    },
  },
}
</script>

<style lang="scss" scoped>
.flash-message {
  display: flex;
  flex-direction: column;
  gap: 5;

  min-width: 200px;
  max-width: 350px;
  padding: 16px 26px 16px 16px;

  border-radius: var(--border-radius);
  border: 2px solid #b1b1b1;
  background-color: #cccccc;
}

.title {
  font-size: 16px;
  font-weight: 600;
  color: var(--typography-title-color);
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;

  width: 15px;
  height: 15px;

  cursor: pointer;
}
</style>
