<template>
  <BaseSelect
    v-model="selectedValues"
    v-bind="$attrs"
    :options="options"
    :has-error="hasError"
    :is-custom-select="true"
    :placeholder="selectPlaceholder"
  >
    <li>
      <BaseCheckbox v-model="isSelectAllProxy" class="option">
        <CustomText
          tag="span"
          :text="`All ${itemName}s`"
          class="option__title"
        />
      </BaseCheckbox>
    </li>
    <li v-for="option in options" :key="option">
      <BaseCheckbox
        v-model="selectedValues"
        :id="option.id"
        :value="option"
        class="option"
      >
        <span class="option__title">{{ option.title }}</span>
      </BaseCheckbox>
    </li>
  </BaseSelect>
</template>

<script>
import CustomText from '@components/CustomText'
import BaseCheckbox from '@components/BaseCheckbox'
import BaseSelect from '@components/BaseSelect2'

export default {
  name: 'MultiSelect',
  components: {BaseCheckbox, BaseSelect, CustomText},
  props: {
    options: {type: Array, required: true},
    modelValue: {type: Array, required: true},
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
          return this.selectedValues[0].title
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
