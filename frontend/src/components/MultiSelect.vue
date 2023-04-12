<template>
  <BaseSelect
    v-model="selectedValues"
    :options="options"
    :has-error="hasError"
    :is-disabled="isDisabled"
    :item-name="itemName"
    :select-name="selectName"
    :placeholder="selectPlaceholder"
  >
    <li>
      <BaseCheckbox v-model="isSelectAllProxy" class="option">
        <span class="option__title">{{ `All ${itemName}s ` }}</span>
      </BaseCheckbox>
    </li>
    <li v-for="option in options" :key="option">
      <BaseCheckbox v-model="selectedValues" :id="option" class="option">
        <span class="option__title">{{ option }}</span>
      </BaseCheckbox>
    </li>
  </BaseSelect>
</template>

<script>
import BaseCheckbox from '@/components/BaseCheckbox2'
import BaseSelect from '@/components/BaseSelect2'
export default {
  name: 'MultiSelect',
  components: {BaseCheckbox, BaseSelect},
  props: {
    options: {type: Array, required: true},
    modelValue: {type: Array, required: true},
    isDisabled: {type: Boolean, default: true},
    selectName: {type: String, required: true},
    itemName: {type: String, default: 'item'},
  },
  emits: ['update:templateChecked', 'update:modelValue'],
  data() {
    return {
      isSelectAll: true,
    }
  },
  computed: {
    selectedValues: {
      get() {
        return this.modelValue
      },
      set(val) {
        this.$emit('update:modelValue', val)
        this.isSelectAll = this.options.length === val.length
      },
    },
    isSelectAllProxy: {
      get() {
        return this.isSelectAll
      },
      set(val) {
        this.isSelectAll = val
        const currProjects = this.isSelectAll ? this.options : []
        this.$emit('update:modelValue', currProjects)
      },
    },
    hasError() {
      return !this.selectedValues.length
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
}
</script>
<style lang="scss" scoped>
.option {
  display: flex;
  gap: 10px;
  cursor: pointer;
  &__title {
    display: flex;
    align-self: center;

    height: 100%;

    font-size: 16px;
  }
}
</style>
