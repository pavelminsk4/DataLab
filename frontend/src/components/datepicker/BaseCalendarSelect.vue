<template>
  <div
    :style="`width: ${selectWidth}px`"
    :class="['custom-select', `selector-${name}`]"
    :tabindex="tabindex"
    @blur="open = false"
  >
    <div class="selected" :class="{open: open}" @click="open = !open">
      <input
        v-if="isSearch"
        v-model="search"
        :placeholder="value"
        type="text"
        class="select-search"
      />
      <CustomText v-else-if="shouldBeTranslated" :text="value" />
      <div v-else>{{ value }}</div>
      <CalendarArrowDownIcon :class="['icon', open && 'open-select']" />
    </div>
    <div class="items scroll" :class="{selectHide: !open}">
      <div
        v-for="(option, i) of selectList"
        :key="i"
        @click="addOption(option)"
        class="item"
      >
        <CustomText v-if="shouldBeTranslated" tag="span" :text="option" />
        <span v-else>{{ option }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import CustomText from '@/components/CustomText'
import CalendarArrowDownIcon from '@/components/icons/CalendarArrowDownIcon'

export default {
  components: {CalendarArrowDownIcon, CustomText},
  props: {
    options: {type: Array, default: null},
    default: {type: [String, Number], required: false, default: null},
    tabindex: {type: Number, required: false, default: 0},
    name: {type: String, required: true},
    value: {type: [String, Number], required: true},
    selectWidth: {type: Number, default: 62},
    isSearch: {type: Boolean, default: false},
    shouldBeTranslated: {type: Boolean, default: false},
  },
  data() {
    return {
      selected: this.default
        ? this.default
        : this.options?.length > 0
        ? this.options[0]
        : null,
      open: false,
      search: '',
    }
  },
  created() {
    document.addEventListener('click', this.close)
    this.$emit('input', this.selected)
  },
  computed: {
    selectList() {
      return this.options.filter((item) => {
        return item?.toLowerCase().includes(this.search?.toLowerCase())
      })
    },
  },
  methods: {
    addOption(option) {
      this.$emit('select-option', option)
      this.selected = option
      this.open = false
    },
    close({target}) {
      const selectList = document.querySelector(`.selector-${this.name}`)

      if (!selectList?.contains(target)) {
        this.open = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.custom-select {
  position: relative;
  text-align: left;

  width: 100%;
  height: 47px;

  outline: none;

  .selected {
    position: relative;

    color: var(--typography-title-color);
    background-color: var(--background-secondary-color);

    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 150%;
    letter-spacing: 0.15px;

    .select-search {
      max-width: 100%;

      outline: none;
      border: none;
      background-color: var(--secondary-bg-color);

      color: var(--typography-primary-color);

      &::placeholder {
        color: var(--typography-primary-color);
      }
    }

    .icon {
      position: absolute;
      right: 0;
      top: 38%;

      cursor: pointer;

      &:hover {
        color: #0b56d9;
      }
    }

    .open-select {
      transform: rotate(180deg);
    }
  }

  .items {
    position: absolute;
    left: 0;
    right: 0;
    z-index: 1;

    overflow: auto;

    border-bottom-right-radius: 8px;
    border-bottom-left-radius: 8px;

    max-height: 200px;

    color: var(--typography-title-color);
    background-color: var(--background-secondary-color);

    font-size: 14px;

    .item {
      cursor: pointer;

      margin-left: 4px;

      color: var(--typography-primary-color);
    }
  }
}

.selectHide {
  display: none;
}
</style>
