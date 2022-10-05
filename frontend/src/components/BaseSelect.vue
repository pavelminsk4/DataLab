<template>
  <div
    :class="['selector', {open: visible}, `selector-${name}`]"
    :data-value="value"
    :data-list="list"
    @click="toggle()"
  >
    <div class="label">
      <input
        v-if="isSearch"
        v-model="search"
        :placeholder="placeholder"
        type="text"
        class="select-search"
      />
      <div v-else-if="!value && !isSearch" class="placeholder">
        {{ placeholder }}
      </div>
      <div v-else-if="!isSearch">{{ value }}</div>
    </div>
    <ArrowDownIcon class="arrow" :class="{expanded: visible}" />
    <div :class="{hidden: !visible, visible}">
      <ul class="select-list">
        <li @click="select('Reject selection')" class="select-item">
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
  </div>
</template>

<script>
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
export default {
  components: {ArrowDownIcon},
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
    isSearch: {
      type: Boolean,
      default: false,
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
    document.addEventListener('click', this.close)
  },
  computed: {
    selectList() {
      return this.list.filter((item) => {
        return item?.toLowerCase().includes(this.search?.toLowerCase())
      })
    },
  },
  methods: {
    toggle() {
      this.visible = !this.visible
    },
    select(option) {
      this.$emit('select-option', this.name, option)
      this.value = option
      this.search = option
    },
    close() {
      const elements = document.querySelectorAll(`.selector-${this.name}`)

      if (!Array.from(elements).find((el) => el.contains(event.target))) {
        this.visible = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.selector {
  position: relative;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  cursor: pointer;

  .arrow {
    position: absolute;
    right: 18px;
    top: 40%;

    transform: rotateZ(0deg) translateY(0px);
    transition-duration: 0.3s;
    transition-timing-function: cubic-bezier(0.59, 1.39, 0.37, 1.01);

    color: var(--primary-text-color);
  }

  .expanded {
    transform: rotateZ(180deg) translateY(2px);
  }

  .label {
    display: block;

    padding: 9px 9px 9px 15px;

    color: var(--primary-text-color);
    font-size: 14px;

    .placeholder {
      color: var(--secondary-text-color);
    }
  }
}

.select-list {
  position: absolute;
  z-index: 1;

  padding: 0;
  margin: 0;
  width: 100%;
  max-height: 250px;

  outline: 1px solid var(--primary-button-color);
  border-top: 1px solid var(--modal-line-color);
  box-shadow: 0 3px 4px rgba(5, 95, 252, 0.49);
  border-radius: 0 0 10px 10px;
  background-color: var(--secondary-bg-color);

  font-size: 14px;

  list-style-type: none;
  overflow-y: auto;
  overflow-x: hidden;

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

.select-search {
  outline: none;

  min-width: 100%;

  border: none;
  background: var(--secondary-bg-color);

  color: var(--primary-text-color);
}

.select-item {
  padding: 9px 9px 9px 19px;

  color: var(--primary-text-color);

  &:hover {
    background: var(--primary-button-color);
  }
}

.current {
  background: var(--primary-button-color);
}

.open {
  border: 1px solid var(--primary-button-color);
  border-bottom: none;
  box-shadow: 0 3px 4px rgba(5, 95, 252, 0.49);
  border-radius: 10px 10px 0 0;
}

.hidden {
  visibility: hidden;
}

.visible {
  visibility: visible;
}
</style>
