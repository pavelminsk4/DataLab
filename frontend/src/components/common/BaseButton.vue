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
    <BaseButtonSpinner v-if="isLoading" class="spinner" />
    <div :class="[isLoading && 'hide-content', 'button-content']">
      <slot></slot>
    </div>
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
    isNotBackground: {type: Boolean, default: false},
    isDisabled: {type: Boolean, default: false},
    buttonLoading: {type: Boolean, default: false},
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
  position: relative;

  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;

  cursor: pointer;
  outline: none;

  width: fit-content;
  height: 36px;
  padding: 8px 12px;

  background: var(--button-primary-color);
  border: 1px solid var(--button-primary-color);
  border-radius: 12px;

  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
  color: var(--button-text-color);

  &:hover {
    background: var(--button-primary-hover-color);
  }

  .spinner {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .button-content {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
  }

  .hide-content {
    opacity: 0;
  }

  svg {
    color: var(--button-text-color);
  }
}

.not-background {
  background: transparent;

  color: var(--button-primary-color);

  &:hover {
    border-color: var(--button-primary-hover-color);
    color: var(--button-primary-hover-color);
    background: transparent;

    svg {
      color: var(--button-primary-hover-color);
    }
  }

  svg {
    color: var(--button-primary-color);
  }
}

.disabled {
  background: var(--button-primary-disabled-color);
  border-color: var(--button-primary-disabled-color);
  opacity: 0.5;
  cursor: not-allowed;

  color: var(--typography-primary-color);

  &:hover {
    background: var(--button-primary-disabled-color);
  }
}

.not-background-disabled {
  border-color: var(--button-primary-disabled-color);

  color: var(--button-text-disabled-color);
}
</style>
