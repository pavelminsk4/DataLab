<template>
  <button
    v-bind="$attrs"
    :class="[
      'base-button',
      isNotBackground && 'not-background',
      isDisabledBtn && 'disabled',
      isDisabledBtn && isNotBackground && 'not-background-disabled',
    ]"
    :disabled="isDisabledBtn"
  >
    <BaseButtonSpinner v-if="isLoading" />
    <slot v-else></slot>
  </button>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'
import BaseButtonSpinner from '@/components/BaseButtonSpinner'

export default {
  name: 'BaseButton',
  components: {BaseButtonSpinner},
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
  },
  computed: {
    ...mapGetters({isGlobalLoading: get.LOADING}),
    isLoading() {
      return this.isGlobalLoading || this.buttonLoading
    },
    isDisabledBtn() {
      return this.isDisabled || this.isLoading
    },
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

  height: 36px;

  background: var(--button-primary-color);
  border: 1px solid var(--button-primary-color);
  border-radius: 12px;

  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
  color: var(--button-text-color);

  &:hover {
    background: var(--button-primary-hover-color);
  }
}

.not-background {
  background: transparent;

  color: var(--button-primary-color);

  &:hover {
    background: var(--button-secondary-hover-color);
  }
}

.disabled {
  background: var(--button-primary-disabled-color);
  border-color: var(--button-primary-disabled-color);
  opacity: 0.5;
  cursor: not-allowed;

  color: var(--primary-text-color);

  &:hover {
    background: var(--button-primary-disabled-color);
  }
}

.not-background-disabled {
  border-color: var(--button-primary-disabled-color);

  color: var(--button-text-disabled-color);
}
</style>
