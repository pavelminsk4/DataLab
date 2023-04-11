<template>
  <div :id="`select-${selectName}`" class="select">
    <button
      @click="toggle"
      :class="[
        'select__button',
        !isDisabled && 'disable',
        hasError && 'select__error',
      ]"
    >
      <div class="select__placeholder">
        <span>{{ selectPlaceholder }}</span>
        <ArrowDownIcon />
      </div>
    </button>
    <ul :class="[isOpen && 'open', 'select__options']">
      <slot></slot>
    </ul>
  </div>
</template>

<script>
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'

export default {
  components: {ArrowDownIcon},
  props: {
    options: {type: Array, required: true},
    modelValue: {type: [Boolean, Array], required: true},
    isDisabled: {type: Boolean, required: true},
    hasError: {type: Boolean, default: false},
    selectName: {type: String, required: true},
    itemName: {type: String, default: 'item'},
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
        case 0:
          return `Select at least one ${this.itemName}`
        case 1:
          return this.selectedValues.toString()
        case this.options.length:
          return `All ${this.itemName}s`
        default:
          return `${length} ${this.itemName}s selected`
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

  &__placeholder {
    display: flex;
    align-items: center;
    justify-content: space-between;

    width: 100%;
  }

  &__options {
    position: absolute;
    display: flex;
    flex-direction: column;
    gap: 15px;
    padding: 15px;

    width: 100%;
    z-index: 1;

    list-style: none;
    background-color: var(--background-secondary-color);
    border: var(--border-primary);
    border-radius: var(--border-radius);
    box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);

    visibility: hidden;
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

  &__error {
    color: var(--negative-status);
    border: 1px solid var(--negative-status);
  }
  .open {
    visibility: visible;
  }
}
</style>
