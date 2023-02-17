<template>
  <tr :class="isSelectedProxy && 'selected-row'">
    <td>
      <BaseCheckbox v-model="isSelectedProxy" />
    </td>
    <slot></slot>
    <td>
      <div class="action-buttons">
        <button class="action-button" @click.stop="$emit('delete-project')">
          <DeleteIcon />
        </button>
      </div>
    </td>

    <div class="divider"></div>
  </tr>
</template>

<script>
import BaseCheckbox from '@/components/BaseCheckbox2'
import DeleteIcon from '@/components/icons/DeleteIcon'

export default {
  name: 'TableRow',
  components: {
    BaseCheckbox,
    DeleteIcon,
  },
  props: {
    modelValue: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    isSelectedProxy: {
      get() {
        return this.modelValue
      },
      set(val) {
        this.$emit('update:modelValue', val)
      },
    },
  },
}
</script>

<style lang="scss" scoped>
tr {
  position: relative;

  &:last-child {
    .divider {
      display: none;
    }
  }
}

.selected-row {
  background-color: var(--primary-active-color);
}

.action-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;

  width: 80px;
}

.action-button {
  flex-shrink: 0;

  padding: 0;

  background: none;
  border: none;

  cursor: pointer;
}

.divider {
  position: absolute;
  left: 0;
  bottom: 0;

  width: calc(100% - 5px);

  border-bottom: var(--border-primary);
}
</style>
