<template>
  <div
    :class="['selector', {open: visible}]"
    :data-value="value"
    :data-list="list"
    @click="toggle()"
  >
    <div class="label">
      <span>{{ value }}</span>
    </div>
    <ArrowDownIcon class="arrow" :class="{expanded: visible}" />
    <div :class="{hidden: !visible, visible}">
      <ul class="select-list">
        <li
          :class="[{current: item === value}, 'select-item']"
          v-for="item in list"
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
  data() {
    return {
      value: 'Select Workspace',
      list: ['Orange', 'Apple', 'Kiwi', 'Lemon', 'Pineapple'],
      visible: false,
    }
  },
  methods: {
    toggle() {
      this.visible = !this.visible
    },
    select(option) {
      this.value = option
    },
  },
}
</script>

<style lang="scss" scoped>
.selector {
  position: relative;
  z-index: 1;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  cursor: pointer;

  .arrow {
    position: absolute;
    right: 28px;
    top: 40%;

    transform: rotateZ(0deg) translateY(0px);
    transition-duration: 0.3s;
    transition-timing-function: cubic-bezier(0.59, 1.39, 0.37, 1.01);
  }

  .expanded {
    transform: rotateZ(180deg) translateY(2px);
  }

  .label {
    display: block;

    padding: 9px;

    color: var(--secondary-text-color);
    font-size: 14px;
  }
}

.select-list {
  position: absolute;
  z-index: 1;

  padding: 0;
  margin: 0;
  width: 100%;

  border: 1px solid var(--primary-button-color);
  border-top: none;
  box-shadow: 0 3px 4px rgba(5, 95, 252, 0.49);
  border-radius: 0 0 10px 10px;
  background-color: var(--secondary-bg-color);

  font-size: 14px;

  list-style-type: none;
}

.select-item {
  padding: 9px;

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
