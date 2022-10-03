<template>
  <div class="step-hint">{{ hint }}</div>

  <CheckIcon v-if="currentStep > value" class="step-item" />
  <div v-else class="step-item">{{ value }}</div>
</template>

<script>
import CheckIcon from '@/components/icons/CheckIcon'

export default {
  name: 'StepHints',
  components: {CheckIcon},
  props: {
    hint: {
      type: String,
      required: true,
    },
    value: {
      type: Number,
      required: true,
    },
    currentStep: {
      type: [Number, String],
      required: true,
    },
  },
}
</script>

<style lang="scss" scoped>
.step-hint {
  position: absolute;
  top: -64px;

  visibility: hidden;
  opacity: 0;
  transition: visibility 0s, opacity 0.5s linear;

  white-space: nowrap;

  margin-left: 4px;
  padding: 12px 17px;

  border-radius: 10px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.22);
  background-color: var(--primary-text-color);

  color: var(--secondary-button-color);

  &::after {
    content: '';

    position: absolute;
    left: 50%;
    right: 50%;
    bottom: -10px;
    transform: translate(-50%, 0) rotate(-135deg);

    box-sizing: border-box;
    border-top: solid 6px var(--primary-text-color);
    border-left: solid 30px var(--primary-text-color);
    border-top-left-radius: 5px;
    border-bottom: solid 30px transparent;
  }
}
</style>

<style lang="scss">
.progress-item {
  &:hover {
    .step-hint {
      visibility: visible;
      opacity: 1;
    }
  }
}
</style>
