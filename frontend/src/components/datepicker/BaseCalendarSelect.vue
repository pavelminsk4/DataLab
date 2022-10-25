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
      <div v-else>{{ value }}</div>
      <CalendarArrowDownIcon :class="['icon', open && 'open-select']" />
    </div>
    <div class="items" :class="{selectHide: !open}">
      <div
        v-for="(option, i) of selectList"
        :key="i"
        @click="addOption(option)"
        class="item"
      >
        {{ option }}
      </div>
    </div>
  </div>
</template>

<script>
import CalendarArrowDownIcon from '@/components/icons/CalendarArrowDownIcon'

export default {
  components: {CalendarArrowDownIcon},
  props: {
    options: {
      type: Array,
      default: null,
    },
    default: {
      type: [String, Number],
      required: false,
      default: null,
    },
    tabindex: {
      type: Number,
      required: false,
      default: 0,
    },
    name: {
      type: String,
      required: true,
    },
    value: {
      type: [String, Number],
      required: true,
    },
    selectWidth: {
      type: Number,
      default: 62,
    },
    isSearch: {
      type: Boolean,
      default: false,
    },
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
    close() {
      const elements = document.querySelectorAll(`.selector-${this.name}`)

      if (!Array.from(elements).find((el) => el.contains(event.target))) {
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

    color: var(--primary-text-color);
    background-color: var(--secondary-bg-color);

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

      color: var(--primary-text-color);

      &::placeholder {
        color: var(--primary-text-color);
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

    color: var(--primary-text-color);
    background-color: var(--secondary-bg-color);

    font-size: 14px;

    .item {
      cursor: pointer;

      margin-left: 4px;

      color: var(--primary-text-color);
    }

    &::-webkit-scrollbar {
      height: 5px;
      width: 5px;
    }

    &::-webkit-scrollbar-track {
      background: var(--secondary-bg-color);
      border: 1px solid var(--input-border-color);
      border-radius: 0 10px 10px 0;
    }

    &::-webkit-scrollbar-thumb {
      height: 4px;

      background: var(--secondary-text-color);
      border-radius: 10px;
    }
  }
}

.selectHide {
  display: none;
}
</style>
