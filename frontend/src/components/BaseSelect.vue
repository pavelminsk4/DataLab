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
    @click="toggle"
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
      <div v-else-if="!value && !isSearch" class="placeholder">
        {{ placeholder }}
      </div>
      <div v-else-if="!isSearch">{{ value }}</div>
    </div>
    <ArrowDownIcon
      class="arrow"
      :class="{expanded: visible}"
      @click.stop="toggle"
    />
    <div :class="{hidden: !visible, visible}">
      <ul v-if="visible" class="select-list scroll">
        <li
          v-if="isRejectSelection"
          @click="select('Reject selection')"
          class="select-item"
        >
          Reject selection
        </li>
        <li
          :class="[{current: item === value}, 'select-item']"
          v-for="item in selectList"
          :key="item"
          @click="select(item)"
        >
          {{ item }}
        </li>
      </ul>
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

export default {
  components: {ArrowDownIcon, ErrorIcon},
  emits: ['update:modelValue', 'select-option'],
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
    isRejectSelection: {
      type: Boolean,
      default: true,
    },
    currentValue: {
      type: String,
      required: false,
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
  },
  data() {
    return {
      value: '',
      search: '',
      visible: false,
    }
  },
  created() {
    if (this.currentValue) {
      this.search = this.currentValue
      this.value = this.currentValue
    }
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
  },
  methods: {
    toggle() {
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
      const selectList = document.querySelector(`.selector-${this.name}`)

      if (!selectList.contains(target)) {
        this.visible = false
      }
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
  border: 1px solid #2e2f34;
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: rgba(46, 47, 52, 0.5);
  cursor: pointer;
  .arrow {
    position: absolute;
    right: 18px;
    top: 40%;
    transform: rotateZ(0deg) translateY(0px);
    transition-duration: 0.3s;
    transition-timing-function: cubic-bezier(0.59, 1.39, 0.37, 1.01);
    color: var(--typography-primary-color);

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
    color: var(--typography-primary-color);
    font-size: 14px;
    .placeholder {
      color: var(--typography-secondary-color);
    }
  }
}
.select-list {
  position: absolute;
  z-index: 1;
  padding: 0;
  margin: -1px;
  width: calc(100% + 2px);
  max-height: 250px;
  border: 1px solid var(--button-primary-color);
  box-shadow: 0 3px 4px rgba(5, 95, 252, 0.49);
  border-radius: 0 0 10px 10px;
  background-color: var(--secondary-bg-color);
  font-size: 14px;
  list-style-type: none;
  overflow-y: auto;
  overflow-x: hidden;
}
.select-search {
  outline: none;
  min-width: 100%;
  border: none;
  background: var(--secondary-bg-color);
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
  border-bottom: none;
  box-shadow: 0 3px 4px rgba(5, 95, 252, 0.49);
  border-radius: 10px 10px 0 0;
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
