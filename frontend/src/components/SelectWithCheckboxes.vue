<template>
  <div
    :class="[
      'selector',
      {open: visible},
      `selector-${name}`,
      hasError && 'error',
    ]"
    :data-value="value"
    :data-list="list"
    @click="visible = true"
  >
    <div class="label">
      <input
        v-if="isSearch"
        v-bind="$attrs"
        :value="modelValue"
        :class="['input', isSearch && 'input-search']"
        :placeholder="placeholder"
        @focus="visible = true"
        @input="handleInput"
        type="text"
        class="select-search"
      />
      <div v-if="!isSearch">{{ value }}</div>
    </div>
    <ArrowDownIcon
      class="arrow"
      :class="{expanded: visible}"
      @click.stop="toggle"
    />
    <div :class="{hidden: !visible, visible}">
      <div v-if="visible" class="select-list scroll">
        <BaseCheckbox
          v-for="(item, index) in selectList"
          :key="item + index"
          :id="item"
          :model-value="isCheckedElement(item)"
          class="list-item"
          @change="onChange"
        >
          {{ item }}
        </BaseCheckbox>
      </div>
    </div>

    <div v-if="hasError" class="error-container">
      {{ errorMessage }}
      <ErrorIcon class="error-icon" />
    </div>
  </div>
</template>

<script>
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import ErrorIcon from '@/components/icons/ErrorIcon'
import BaseCheckbox from '@/components/BaseCheckbox'

export default {
  name: 'SelectWithCheckboxes',
  components: {BaseCheckbox, ErrorIcon, ArrowDownIcon},
  emits: ['update:modelValue', 'select-option', 'get-selected-items'],
  props: {
    list: {
      type: Array,
      default: null,
    },
    placeholder: {
      type: String,
      default: 'Select option',
    },
    name: {
      type: String,
      required: true,
    },
    modelValue: {
      type: String,
      required: true,
    },
    isSearch: {
      type: Boolean,
      default: false,
    },
    isClearSelectedValue: {
      type: Boolean,
      default: false,
    },
    hasError: {
      type: Boolean,
      default: false,
    },
    errorMessage: {
      type: String,
      default: 'Error',
    },
    selectedCheckboxes: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      value: '',
      search: '',
      visible: false,
      selectedItems: [],
    }
  },
  mounted() {
    document.addEventListener('click', this.close)
  },
  computed: {
    selectList() {
      if (this.isSearch && !!this.modelValue) {
        return this.list.filter((item) => {
          return item?.toLowerCase().includes(this.modelValue?.toLowerCase())
        })
      }
      if (this.isSearch) {
        return this.list.filter((item) => {
          return item?.toLowerCase().includes(this.modelValue?.toLowerCase())
        })
      }
      return this.list
    },
    selectedValuesProxy: {
      get() {
        return this.selectedCheckboxes || this.selectedItems
      },
      set(val) {
        this.selectedItems = val
      },
    },
  },
  methods: {
    toggle() {
      document.addEventListener('click', this.close)
      this.visible = !this.visible
    },
    handleInput(e) {
      this.visible = true
      this.$emit('update:modelValue', e.target.value, this.name)
    },
    select(option) {
      this.$emit('select-option', this.name, option, this.visible)
      this.value = option
      this.search = option
      this.visible = false
    },
    close({target}) {
      const elements = document.querySelectorAll(`.selector-${this.name}`)
      if (!Array.from(elements).find((el) => el.contains(target))) {
        this.visible = false
      }
    },
    isCheckedElement(item) {
      return this.selectedValuesProxy?.some((el) => el === item)
    },
    onChange(args) {
      const {id, checked} = args
      if (checked) {
        this.selectedValuesProxy.push(id)
      } else {
        let element = this.selectedValuesProxy.indexOf(id)
        this.removeSelectedFilter(element, id)
      }

      this.$emit('get-selected-items', this.selectedValuesProxy, this.name)
    },
    removeSelectedFilter(index) {
      this.selectedValuesProxy.splice(index, 1)
    },
  },
  watch: {
    isClearSelectedValue() {
      if (this.isClearSelectedValue) {
        this.value = ''
        this.search = ''
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.selector {
  position: relative;

  border: 1px solid var(--border-color);
  border-radius: 10px;
  background: var(--background-secondary-color);

  cursor: pointer;

  .arrow {
    position: absolute;
    right: 18px;
    top: 40%;

    transform: rotateZ(0deg) translateY(0px);
    transition-duration: 0.3s;
    transition-timing-function: cubic-bezier(0.59, 1.39, 0.37, 1.01);

    color: var(--primary-text-color);

    &:hover {
      cursor: pointer;
      color: var(--primary-color);
    }
  }
  .expanded {
    transform: rotateZ(180deg) translateY(2px);
  }

  .label {
    display: block;

    padding: 9px 35px 9px 15px;

    z-index: 3;

    color: var(--primary-text-color);
    font-size: 14px;

    .placeholder {
      z-index: 1;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--typography-primary-color);
    }
  }
}
.select-list {
  position: absolute;
  z-index: 1;

  padding: 8px;
  margin-top: 4px;
  width: calc(100% + 2px);
  max-height: 250px;

  border: 1px solid var(--button-primary-color);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  background-color: var(--background-secondary-color);

  font-size: 14px;
  list-style-type: none;
  overflow-y: auto;
  overflow-x: hidden;

  .list-item {
    display: flex;
    gap: 10px;

    padding: 8px 12px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    color: var(--typography-primary-color);

    &:hover {
      border-radius: 8px;
      background-color: var(--button-secondary-hover-color);
    }
  }
}

.select-search {
  outline: none;
  min-width: 100%;

  border: none;
  background: var(--background-secondary-color);

  color: var(--primary-text-color);
}
.select-item {
  padding: 9px 9px 9px 19px;
  color: var(--primary-text-color);

  &:hover {
    background: var(--button-primary-color);
  }
}
.current {
  background: var(--button-primary-color);
}
.open {
  border: 1px solid var(--button-primary-color);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
}
.hidden {
  visibility: hidden;

  .select-list {
    height: 0;
  }
}
.visible {
  visibility: visible;
}

.error {
  border: 1px solid var(--negative-status);
  border-radius: 10px;

  .error-container {
    --height-icon: 16px;

    position: absolute;
    top: calc(50% - var(--height-icon) / 2);
    right: 40px;

    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;

    white-space: nowrap;

    font-size: 12px;
    color: var(--negative-status);
  }
}
</style>
