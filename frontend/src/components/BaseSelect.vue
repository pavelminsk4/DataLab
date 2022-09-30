<template>
  <div
    :class="['selector', {open: visible}]"
    :data-value="value"
    :data-list="list"
    @click="toggle()"
  >
    <div class="label">
      <div v-if="!value" class="placeholder">{{ placeholder }}</div>
      <div>{{ value }}</div>
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
  },
  data() {
    return {
      value: '',
      visible: false,
    }
  },
  computed: {
    selectList() {
      return this.list
    },
  },
  methods: {
    toggle() {
      this.visible = !this.visible
    },
    select(option) {
      this.$emit('select-option', option)
      this.value = option
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
  overflow: auto;

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
