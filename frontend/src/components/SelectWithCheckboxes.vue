<template>
  <div
    :ref="`selector-${name}`"
    :class="[
      'selector',
      {open: visible},
      `selector-${name}`,
      hasError && 'error',
    ]"
  >
    <div class="label" @click="visible = true">
      <input
        v-if="isSearch"
        v-bind="$attrs"
        type="text"
        :dir="currentDir"
        :value="modelValue"
        :placeholder="placeholder"
        :class="['input', isSearch && 'input-search', 'select-search']"
        @focus="visible = true"
        @input="handleInput"
      />
      <div v-if="!isSearch">{{ value }}</div>
    </div>
    <div
      :ref="`toggle-btn-${name}`"
      :class="['arrow', {expanded: visible}]"
      @click="toggle"
    >
      <ArrowDownIcon />
    </div>
    <div :class="{hidden: !visible, visible}">
      <div v-if="visible" class="select-list scroll">
        <BaseCheckbox
          v-for="(item, index) in selectList"
          :key="item + index"
          v-model="selectedItems"
          :id="item + index"
          :value="item"
          class="list-item"
        >
          {{ item }}
        </BaseCheckbox>
      </div>
    </div>

    <div v-if="hasError" class="error-container">
      <CustomText :text="errorMessage" />
      <ErrorIcon class="error-icon" />
    </div>
  </div>
</template>

<script>
import translate from '@lib/mixins/translate.js'

import CustomText from '@components/CustomText'
import ArrowDownIcon from '@components/icons/ArrowDownIcon'
import ErrorIcon from '@components/icons/ErrorIcon'
import BaseCheckbox from '@components/BaseCheckbox2'

export default {
  name: 'SelectWithCheckboxes',
  mixins: [translate],
  components: {BaseCheckbox, ErrorIcon, ArrowDownIcon, CustomText},
  emits: ['update:modelValue', 'select-option', 'get-selected-items'],
  props: {
    dir: {type: String, default: 'ltr'},
    list: {type: Array, default: null},
    placeholder: {type: String, default: 'Select option'},
    name: {type: String, required: true},
    modelValue: {type: [String, Array], required: true},
    isSearch: {type: Boolean, default: false},
    isClearSelectedValue: {type: Boolean, default: false},
    hasError: {type: Boolean, default: false},
    errorMessage: {type: String, default: 'Error'},
    selectedCheckboxes: {type: Array, default: () => []},
  },
  data() {
    return {
      value: '',
      search: '',
      visible: false,
      items: [],
    }
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
    selectedItems: {
      get() {
        return this.selectedCheckboxes || this.items
      },
      set(value) {
        this.items = value
        this.$emit('get-selected-items', this.items, this.name)
      },
    },
  },
  mounted() {
    document.addEventListener('click', this.clickOut)
  },
  unmounted() {
    document.removeEventListener('click', this.clickOut)
  },
  watch: {
    isClearSelectedValue() {
      if (this.isClearSelectedValue) {
        this.value = ''
        this.search = ''
      }
    },
  },
  methods: {
    toggle() {
      if (this.visible) {
        this.close()
      } else {
        this.visible = true
      }
    },
    handleInput({target}) {
      this.visible = true
      this.$emit('update:modelValue', target.value, this.name)
    },
    select(option) {
      this.$emit('select-option', this.name, option, this.visible)
      this.value = option
      this.search = option
      this.visible = false
    },
    close() {
      this.visible = false
      this.$emit('update:modelValue', '', this.name)
    },
    clickOut({target}) {
      if (!this.visible) return
      const element = this.$refs[`selector-${this.name}`]

      if (!element.contains(target)) {
        this.close()
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.selector {
  position: relative;

  border: var(--border-primary);
  border-radius: 10px;
  background: var(--background-secondary-color);

  cursor: pointer;

  .arrow {
    position: absolute;
    right: 8px;
    top: 0;

    display: flex;
    align-items: center;

    height: 100%;
    padding: 0 10px;

    transform: rotateZ(0deg) translateY(0px);
    transition-duration: 0.3s;
    transition-timing-function: cubic-bezier(0.59, 1.39, 0.37, 1.01);

    color: var(--typography-primary-color);

    svg {
      pointer-events: none;
    }

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

    color: var(--typography-primary-color);
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

    height: auto;
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

  color: var(--typography-primary-color);
}
.select-item {
  padding: 9px 9px 9px 19px;
  color: var(--typography-primary-color);

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
