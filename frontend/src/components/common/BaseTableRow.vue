<template>
  <tr :class="isSelectedProxy && 'selected-row'">
    <td>
      <BaseCheckbox v-model="modelValueProxy" :id="id" />
    </td>
    <slot></slot>
    <td>
      <div class="action-buttons">
        <button class="action-button" @click.stop="$emit('delete-entity')">
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
  name: 'BaseTableRow',
  components: {
    BaseCheckbox,
    DeleteIcon,
  },
  props: {
    modelValue: {type: [Boolean, Array], default: false},
    id: {type: [Number, String], default: null},
  },
  computed: {
    modelValueProxy: {
      get() {
        return this.modelValue
      },
      set(val) {
        this.$emit('update:modelValue', val)
      },
    },
    isSelectedProxy() {
      return this.modelValueProxy.includes(this.id)
    },
  },
}
</script>

<style lang="scss" scoped>
tr {
  position: relative;
  td {
    vertical-align: initial;
  }

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
