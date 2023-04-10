<template>
  <section
    @click="openDropdown"
    :class="[`dropdown-wrapper-${name}`, 'dropdown-wrapper']"
  >
    <div class="title">{{ title }}</div>
    <div v-if="selectedValue" class="selected-value">{{ selectedValue }}</div>
    <ArrowDownIcon
      :class="[isOpenDropdown && 'arrow-open-dropdown', 'arrow-down']"
    />

    <div
      v-if="isOpenDropdown"
      :style="customStyle"
      class="dropdown"
      @click="openDropdown"
    >
      <slot></slot>
    </div>
  </section>
</template>

<script>
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'

export default {
  name: 'BaseDropdown',
  components: {ArrowDownIcon},
  props: {
    title: {
      type: String,
      default: '',
    },
    selectedValue: {
      type: [Number, String],
      required: false,
    },
    name: {
      type: String,
      required: true,
    },
    customStyle: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      isOpenDropdown: false,
    }
  },
  created() {
    document.addEventListener('click', this.closeDropdown)
  },
  unmounted() {
    document.removeEventListener('click', this.closeDropdown)
  },
  methods: {
    openDropdown() {
      this.isOpenDropdown = !this.isOpenDropdown
    },
    closeDropdown({target}) {
      const dropdownList = document.querySelector(
        `.dropdown-wrapper-${this.name}`
      )

      if (!dropdownList?.contains(target)) {
        this.isOpenDropdown = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.dropdown-wrapper {
  position: relative;

  display: flex;
  align-items: center;

  cursor: pointer;

  .title {
    margin-right: 12px;

    color: var(--typography-secondary-color);
  }

  .selected-value {
    margin-right: 10px;

    color: var(--typography-title-color);
  }

  .dropdown {
    z-index: 1000;

    position: absolute;
    top: 30px;
    right: 2px;

    display: flex;
    flex-direction: column;

    cursor: pointer;

    min-width: 100%;

    background: var(--progress-line);
    border: 1px solid var(--modal-border-color);
    border-radius: 10px;

    font-size: 12px;
    color: var(--typography-primary-color);
  }
}

.arrow-down {
  cursor: pointer;

  width: 8px;
  height: 8px;

  color: var(--typography-primary-color);

  &:hover {
    color: var(--button-primary-color);
  }
}

.arrow-open-dropdown {
  transform: rotate(180deg);
  color: var(--button-primary-color);
}
</style>

<style lang="scss">
.dropdown {
  div {
    white-space: nowrap;

    padding: 5px;

    color: var(--typography-title-color);
    background-color: var(--background-secondary-color);

    &:hover {
      color: var(--primary-hover-color);
      background-color: var(--primary-active-color);
    }

    &:first-child {
      border-radius: 10px 10px 0 0;
    }

    &:last-child {
      border-radius: 0 0 10px 10px;
    }
  }
}
</style>
