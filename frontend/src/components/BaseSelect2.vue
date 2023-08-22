<template>
  <div :id="`select-${selectName}`" class="select">
    <button
      :class="[
        'select__button',
        isDisabled && 'disable',
        hasError && 'select__error',
      ]"
      @click="toggle"
    >
      <div class="select__placeholder">
        <span>{{ currentPlaceholder || selectedValues }}</span>
        <ArrowDownIcon />
      </div>
    </button>
    <ul :class="[isOpen && 'open', 'select__options', 'scroll']">
      <slot :close="toggle">
        <li
          v-for="option in options"
          :key="option"
          :value="option"
          class="option"
          @click="handleClick"
        >
          {{ option }}
        </li>
      </slot>
    </ul>
  </div>
</template>

<script>
import translate from '@/lib/mixins/translate.js'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'

export default {
  name: 'BaseSelect',
  components: {ArrowDownIcon},
  mixins: [translate],
  props: {
    options: {type: Array, default: () => []},
    modelValue: {type: [Boolean, Array, String, Number], required: true},
    isDisabled: {type: Boolean, default: false},
    isCloseOptions: {type: Boolean, default: false},
    hasError: {type: Boolean, default: false},
    selectName: {type: String, required: true},
    itemName: {type: String, default: 'item'},
    placeholder: {type: String, default: ''},
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
    handleClick({target}) {
      this.selectedValues = target.innerText
      this.isOpen = false
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
    max-height: 300px;
    z-index: 1;

    list-style: none;
    background-color: var(--background-secondary-color);
    border: var(--border-primary);
    border-radius: var(--border-radius);
    box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);

    visibility: hidden;
    overflow-y: auto;
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

.option {
  cursor: pointer;
  &__title {
    display: flex;
    align-self: center;

    height: 100%;

    font-size: 16px;
  }
}
</style>
