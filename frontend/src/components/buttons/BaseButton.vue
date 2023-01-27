<template>
  <button
    v-bind="$attrs"
    :class="[
      'base-button',
      isNotBackground && 'not-background',
      (isDisabled || isLoading || buttonLoading) && 'disabled',
      hasTooltip && 'disabled-creation',
    ]"
    :disabled="isDisabled || isLoading || buttonLoading"
  >
    <BaseTooltip v-if="hasTooltip" class="tooltip">
      {{ tooltipTitle }}
    </BaseTooltip>
    <BaseButtonSpinner v-if="isLoading || buttonLoading" />
    <slot v-else></slot>
  </button>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'
import BaseButtonSpinner from '@/components/BaseButtonSpinner'
import BaseTooltip from '@/components/BaseTooltip'

export default {
  name: 'BaseButton',
  components: {BaseTooltip, BaseButtonSpinner},
  props: {
    isNotBackground: {
      type: Boolean,
      default: false,
    },
    isDisabled: {
      type: Boolean,
      default: false,
    },
    buttonLoading: {
      type: Boolean,
      default: false,
    },
    tooltipTitle: {
      type: String,
      default: '',
    },
    hasTooltip: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    ...mapGetters({isLoading: get.LOADING}),
  },
}
</script>

<style lang="scss">
.base-button {
  display: flex;
  align-items: center;
  justify-content: center;

  cursor: pointer;
  outline: none;

  height: 40px;
  max-width: 100%;

  border: none;
  border-radius: 8px;

  color: var(--primary-text-color);
  background: var(--primary-button-color);

  &:hover {
    background: rgba(5, 95, 252, 0.6);
  }
}

.not-background {
  background: var(--secondary-button-color);
}

.disabled {
  opacity: 0.5;
  cursor: not-allowed;

  color: var(--primary-text-color);
  background: var(--disabled-color);
}

.disabled-creation {
  &:hover {
    opacity: 0.9;
    .tooltip {
      visibility: visible;
    }
  }
}

.tooltip {
  margin-right: 216px;
  visibility: hidden;
}
</style>
