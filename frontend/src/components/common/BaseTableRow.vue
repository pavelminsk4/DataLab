<template>
  <tr :class="isSelectedProxy && 'selected-row'">
    <td class="checkbox-containter">
      <BaseCheckbox v-model="modelValueProxy" :id="id" />
    </td>
    <slot></slot>
    <div class="divider"></div>
  </tr>
</template>

<script>
import BaseCheckbox from '@/components/BaseCheckbox2'

export default {
  name: 'BaseTableRow',
  components: {
    BaseCheckbox,
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
    vertical-align: top;
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

.divider {
  position: absolute;
  left: 0;
  bottom: 0;

  width: calc(100% - 5px);

  border-bottom: var(--border-primary);
}
</style>
