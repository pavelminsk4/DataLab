<template>
  <div
    :class="[
      'dimensions-list__item',
      isSelectListOpen && 'open-select-list',
      isOpenDropDown && !isDisabled && 'dimensions-list__item-active',
      isDisabled && 'item-disabled',
    ]"
  >
    <section @click="toggleDropdown" class="dropdown-section">
      <div>{{ title }}</div>
      <ArrowDownIcon
        :class="[isOpenDropDown && !isDisabled && 'active-icon']"
      />
    </section>

    <BaseSelect
      v-if="isOpenDropDown && !isDisabled"
      class="select"
      :name="title"
      :list="selectList"
      :is-search="true"
      :current-value="selectedValue"
      @select-option="selectDimension"
      @click="toggleSelectList"
    />
  </div>
</template>

<script>
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import BaseSelect from '@/components/BaseSelect'
export default {
  name: 'DimensionsItem',
  components: {BaseSelect, ArrowDownIcon},
  props: {
    title: {
      type: String,
      required: true,
    },
    id: {
      type: Number,
      required: false,
    },
    isDisabled: {
      type: Boolean,
      required: true,
    },
    selectList: {
      type: [Array, Object],
      required: false,
    },
    selectedValue: {
      type: [String, Number],
      required: false,
    },
  },
  data() {
    return {
      isOpenDropDown: false,
      isSelectListOpen: false,
    }
  },
  methods: {
    toggleDropdown() {
      this.isOpenDropDown = !this.isOpenDropDown
    },
    toggleSelectList() {
      this.isSelectListOpen = !this.isSelectListOpen
    },
    selectDimension(name, option, visible) {
      if (option === 'Reject selection') {
        this.$emit('update-widget-view', name, null)
      } else {
        this.$emit('update-widget-view', name, option)
      }
      this.isSelectListOpen = visible
    },
  },
}
</script>

<style lang="scss" scoped>
.dimensions-list__item {
  display: flex;
  flex-direction: column;

  margin-top: 6px;
  padding: 16px 25px;

  border-bottom: 1px solid var(--input-border-color);

  cursor: pointer;

  .dropdown-section {
    display: flex;
    justify-content: space-between;
    align-items: center;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
  }
}

.dimensions-list__item-active {
  background: var(--primary-bg-color);
  border-radius: 15px;
  border-bottom: none;

  animation: rotateMenu 300ms ease-in-out forwards;
}

.open-select-list {
  height: inherit;
}

.item-disabled {
  cursor: not-allowed;

  color: var(--secondary-text-color);
}

.active-icon {
  transform: rotate(180deg);
}

.select {
  margin-top: 20px;
}

@keyframes rotateMenu {
  0% {
    transform: scaleY(0);
  }
  80% {
    transform: scaleY(1.1);
  }
  100% {
    transform: scaleY(1);
  }
}
</style>
