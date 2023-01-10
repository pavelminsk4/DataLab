<template>
  <section
    @click="openDropdown"
    :class="[`dropdown-wrapper-${id}`, 'dropdown-wrapper']"
  >
    {{ title }}
    <ArrowDownIcon
      :class="[isOpenDropdown && 'arrow-open-dropdown', 'arrow-down']"
    />

    <div v-if="isOpenDropdown" @click="openDropdown" class="dropdown">
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
    id: {
      type: Number,
      required: true,
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
    closeDropdown() {
      const elements = document.querySelectorAll(`.dropdown-wrapper-${this.id}`)

      if (!Array.from(elements).find((el) => el.contains(event.target))) {
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

  font-size: 12px;

  .dropdown {
    z-index: 1000;

    position: absolute;
    top: 20px;
    right: 2px;

    display: flex;
    flex-direction: column;

    cursor: pointer;

    min-width: 100%;

    background: var(--progress-line);
    border: 1px solid var(--modal-border-color);
    border-radius: 10px;

    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 20px;
    color: var(--primary-text-color);

    .item {
      cursor: pointer;

      padding: 9px 24px 8px;
    }
  }
}

.arrow-down {
  cursor: pointer;

  width: 10px;
  height: 10px;

  margin: 0 11px 0 7px;

  color: var(--primary-text-color);

  &:hover {
    color: var(--primary-button-color);
  }
}

.arrow-open-dropdown {
  transform: rotate(180deg);
  color: var(--primary-button-color);
}
</style>
