<template>
  <div ref="dropdown" class="dropdown-options-container">
    <slot>
      <li
        v-for="{name, icon, action} in options"
        :key="name"
        class="option"
        @click.stop="$emit(action)"
      >
        <component :is="`${icon}Icon`"></component>
        <span>{{ name }}</span>
      </li>
    </slot>
  </div>
</template>

<script>
import {defineAsyncComponent} from 'vue'

export default {
  name: 'DropdownOptionsContainer',
  components: {
    EditIcon: defineAsyncComponent(() => import('@components/icons/EditIcon')),
    DeleteIcon: defineAsyncComponent(() =>
      import('@components/icons/DeleteIcon')
    ),
    SaveIcon: defineAsyncComponent(() => import('@components/icons/SaveIcon')),
  },
  props: {
    options: {
      type: Array,
      default: () => [],
    },
  },
  created() {
    document.addEventListener('click', this.closeDropdown)
  },
  unmounted() {
    document.removeEventListener('click', this.closeDropdown)
  },
  methods: {
    closeDropdown({target}) {
      const dropdown = this.$refs.dropdown.parentElement

      if (!dropdown?.contains(target)) {
        this.$emit('close-dropdown')
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.dropdown-options-container {
  position: absolute;
  left: 0;
  top: calc(100% + 8px);

  display: flex;
  flex-direction: column;

  white-space: nowrap;

  border-radius: 4px;
  padding: 8px;
  box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);

  background: var(--background-secondary-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 110%;
  color: var(--typography-title-color);
}

.option {
  display: flex;
  align-items: center;
  gap: 10px;

  width: 152px;
  padding: 6px 10px;

  border-radius: 8px;

  &:hover {
    background-color: var(--background-additional-color);
  }
}
</style>
