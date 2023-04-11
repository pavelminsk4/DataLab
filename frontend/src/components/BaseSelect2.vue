<template>
  <div :id="`select-${selectName}`" class="select">
    <button @click="toggle" :class="['select__button', {disable: !isDisabled}]">
      <span>{{ selectPlaceholder }}</span>
    </button>
    <ul :class="[{open: isOpen}, 'select__options']">
      <slot></slot>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    options: {type: Array, required: true},
    modelValue: {type: [Boolean, Array], required: true},
    selectName: {type: String, required: true},
    isDisabled: {type: Boolean, required: true},
  },
  data() {
    return {
      isOpen: false,
    }
  },
  computed: {
    selectedValues: {
      get() {
        return this.modelValue
      },
      set(val) {
        this.$emit('update:modelValue', val)
      },
    },
    selectPlaceholder() {
      const length = this.selectedValues.length
      switch (length) {
        case 1:
          return this.selectedValues.toString()
        case this.options.length:
          return 'All projects'
        default:
          return `${length} items selected`
      }
    },
  },
  created() {
    document.addEventListener('click', this.close)
  },
  unmounted() {
    document.removeEventListener('click', this.close)
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen
    },
    close({target}) {
      const selectList = document.getElementById(`select-${this.selectName}`)

      if (!selectList.contains(target)) {
        this.isOpen = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.select {
  position: relative;
  width: 100%;

  &__options {
    z-index: 1;
    position: absolute;
    display: flex;
    flex-direction: column;
    gap: 15px;
    padding: 15px;

    width: 100%;
    visibility: hidden;

    list-style: none;
    background-color: var(--background-secondary-color);
    border: var(--border-primary);
    border-radius: var(--border-radius);
    box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);
  }

  &__button {
    display: flex;
    align-items: center;

    width: 100%;
    height: 40px;
    margin-bottom: 5px;

    background-color: var(--background-secondary-color);
    border: var(--border-primary);
    border-radius: var(--border-radius);
  }
  .open {
    visibility: visible;
  }
}
</style>
