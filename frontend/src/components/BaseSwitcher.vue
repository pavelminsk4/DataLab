<template>
  <div>
    <span
      class="toggle-wrapper"
      role="checkbox"
      :aria-checked="value"
      tabindex="0"
      @click="toggle"
      @keydown.space.prevent="toggle"
    >
      <span class="toggle-background" :class="backgroundStyles" />
      <span class="toggle-indicator" :style="indicatorStyles" />
    </span>
  </div>
</template>

<script>
export default {
  name: 'BaseSwitcher',
  props: {
    value: {
      type: Boolean,
      required: true,
    },
  },
  computed: {
    backgroundStyles() {
      return {
        'turn-on': this.value,
        'turn-off': !this.value,
      }
    },
    indicatorStyles() {
      return {transform: this.value ? 'translateX(14px)' : 'translateX(0)'}
    },
  },
  methods: {
    toggle() {
      this.$emit('input', !this.value)
    },
  },
}
</script>

<style scoped>
.turn-on {
  background-color: var(--button-primary-color);
}

.turn-off {
  background-color: var(--secondary-text-color);
}

.toggle-wrapper {
  position: relative;

  display: inline-block;

  width: 34px;
  height: 20px;

  cursor: pointer;
}

.toggle-wrapper:focus {
  outline: 0;
}

.toggle-background {
  display: inline-block;

  height: 100%;
  width: 100%;

  border-radius: 10px;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);

  transition: background-color 0.4s ease;
}

.toggle-indicator {
  position: absolute;
  left: 7%;
  top: 14%;
  transform: translate(-50%, -50%);

  height: 15px;
  width: 15px;

  border-radius: 100px;
  background-color: var(--secondary-bg-color);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

  transition: transform 0.4s ease;
}
</style>
