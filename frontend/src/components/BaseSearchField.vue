<template>
  <div
    :class="['selector', {open: list.length && visible}, `selector-${name}`]"
    :data-value="value"
    :data-list="list"
  >
    <div v-if="isLoading" class="spinner">
      <BaseButtonSpinner />
    </div>

    <div class="label">
      <input
        v-if="isSearch"
        v-bind="$attrs"
        :value="modelValue"
        :class="['input', isSearch && 'input-search']"
        :placeholder="currentPlaceholder"
        :dir="currentDir"
        type="text"
        class="select-search"
        @input="handleInput"
        @focus="focusInput"
      />
      <CustomText
        v-else-if="!value && !isSearch"
        :text="placeholder"
        class="placeholder"
      />
      <div v-else-if="!isSearch">{{ value }}</div>
    </div>
    <div :class="{hidden: !visible, visible}">
      <ul v-if="visible && list.length" class="select-list scroll">
        <CustomText
          v-if="isRejectSelection"
          tag="li"
          text="Reject selection"
          class="select-item"
          @click="select('Reject selection')"
        />
        <li
          v-for="item in selectList"
          :key="item"
          :class="[{current: item === value}, 'select-item']"
          @click="select(item)"
        >
          <slot :item="item" name="select-item"></slot>{{ item }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import {get, action} from '@store/constants'
import debounce from 'lodash/debounce'
import CustomText from '@/components/CustomText'
import BaseButtonSpinner from '@/components/BaseButtonSpinner'

export default {
  emits: ['update:modelValue', 'select-option', 'focus-input'],
  components: {
    CustomText,
    BaseButtonSpinner,
  },
  props: {
    list: {type: Array, default: null},
    placeholder: {type: String, default: 'Select option'},
    name: {type: String, required: true},
    modelValue: {type: [String, Array], required: true},
    isSearch: {type: Boolean, default: false},
    isRejectSelection: {type: Boolean, default: true},
    currentValue: {type: [String, Array], required: false},
    isClearSelectedValue: {type: Boolean, default: false},
    isLoading: {type: Boolean, default: false},
    dir: {type: String, default: 'ltr'},
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
    ...mapGetters({
      platformLanguages: get.PLATFORM_LANGUAGE,
      translated: get.TRANSLATION,
    }),
    currentDir() {
      return this.platformLanguages === 'ar' ? 'rtl' : this.dir
    },
    currentPlaceholder() {
      if (this.platformLanguage === 'en') return this.placeholder

      this[action.GET_TRANSLATED_TEXT](this.placeholder)
      return this.translated[this.placeholder]
    },
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
    ...mapActions([action.GET_TRANSLATED_TEXT]),
    handleInput: debounce(function (e) {
      this.$emit('update:modelValue', e.target.value, this.name)
    }, 500),
    focusInput({target}) {
      this.visible = true
      this.$emit('focus-input', target.value, this.name)
    },
    select(option) {
      this.$emit('select-option', this.name, option, this.visible)
      this.value = option
      this.search = option
      this.visible = false
    },
    close({target}) {
      const dropdownList = document.querySelector(`.selector-${this.name}`)

      if (!dropdownList?.contains(target)) {
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

  border: var(--border-primary);
  border-radius: 10px;
  background: var(--background-secondary-color);

  cursor: pointer;

  .expanded {
    transform: rotateZ(180deg) translateY(2px);
  }

  .label {
    display: block;

    padding: 9px 35px 9px 15px;

    color: var(--typography-primary-color);
    font-size: 14px;

    .placeholder {
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

  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 50px;
  max-height: 250px;

  outline: 1px solid var(--button-primary-color);
  border-top: 1px solid var(--modal-line-color);
  box-shadow: 0 3px 4px rgba(5, 95, 252, 0.49);
  border-radius: 0 0 10px 10px;
  background-color: var(--background-secondary-color);

  font-size: 14px;

  list-style-type: none;
  overflow-y: auto;
  overflow-x: hidden;
}

.select-search {
  outline: none;

  min-width: 100%;

  border: none;
  background: transparent;

  color: var(--typography-primary-color);
}

.select-item {
  display: flex;
  align-items: center;

  padding: 9px 9px 9px 19px;

  color: var(--typography-primary-color);

  &:hover {
    color: var(--button-text-color);
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

.spinner {
  position: absolute;
  right: 5px;

  display: flex;
  align-items: center;

  height: 100%;

  opacity: 0.7;
}
</style>
