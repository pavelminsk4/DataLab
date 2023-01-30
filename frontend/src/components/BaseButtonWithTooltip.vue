<template>
  <BaseButton :is-disabled="isDisabled" class="disabled-creation">
    <BaseTooltip v-if="hasTooltip" class="tooltip">
      {{ tooltipTitle }}
    </BaseTooltip>
    <slot />
  </BaseButton>
</template>

<script>
import BaseButton from '@/components/buttons/BaseButton'
import BaseTooltip from '@/components/BaseTooltip'
export default {
  name: 'BaseButtonWithTooltip',
  components: {BaseTooltip, BaseButton},
  props: {
    tooltipTitle: {
      type: String,
      default: '',
    },
    isDisabled: {
      type: Boolean,
      default: false,
    },
    hasTooltip: {
      type: Boolean,
      default: false,
    },
  },
}
</script>

<style lang="scss" scoped>
.disabled-creation {
  position: relative;

  &:hover {
    opacity: 0.9;
    .tooltip {
      visibility: visible;
    }
  }
}

.tooltip {
  right: 105%;
  visibility: hidden;
}
</style>
