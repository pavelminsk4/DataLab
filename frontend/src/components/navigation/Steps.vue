<template>
  <div class="progress-bar">
    <div
      v-for="(item, index) in progressBarData"
      :key="'step' + index"
      :class="['progress-item', step === item.name && 'active-item']"
    >
      <div class="step-hint">{{ item.hint }}</div>

      <CheckIcon v-if="currentStep > item.value" class="step-item" />
      <div v-else class="step-item">{{ item.value }}</div>
    </div>
  </div>
</template>

<script>
import CheckIcon from '@/components/icons/CheckIcon'

export default {
  name: 'StepHints',
  components: {CheckIcon},
  props: {
    currentStep: {
      type: [Number, String],
      required: true,
    },
    step: {
      type: [Number, String],
      required: true,
    },
    isExistingWorkspace: {
      type: Boolean,
      required: true,
    },
  },
  computed: {
    progressBarData() {
      return this.isExistingWorkspace
        ? [
            {
              name: 'ProjectStep1',
              hint: 'Source Type',
              value: 1,
            },
            {
              name: 'ProjectStep2',
              hint: 'Keywords',
              value: 2,
            },
          ]
        : [
            {
              name: 'Step1',
              hint: 'Create Workspace',
              value: 1,
            },
            {
              name: 'Step2',
              hint: 'Source Type',
              value: 2,
            },
            {
              name: 'Step3',
              hint: 'Keywords',
              value: 3,
            },
          ]
    },
  },
}
</script>

<style lang="scss" scoped>
.progress-bar {
  display: flex;
  align-items: center;

  margin-right: 40px;
}

.progress-item {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;

  width: 24px;
  height: 24px;

  border-radius: 100%;
  background-color: var(--disabled-color);

  cursor: pointer;

  color: var(--typography-primary-color);

  &:not(:last-child) {
    margin-right: 38px;

    &::before {
      position: absolute;
      left: 24px;

      content: '';

      width: 38px;
      height: 2px;

      background-color: var(--progress-line);
    }
  }
}

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
  background-color: var(--typography-primary-color);

  color: var(--typography-title-color);

  &::after {
    content: '';

    position: absolute;
    left: 50%;
    right: 50%;
    bottom: -10px;
    transform: translate(-50%, 0) rotate(-135deg);

    box-sizing: border-box;
    border-top: solid 6px var(--typography-primary-color);
    border-left: solid 30px var(--typography-primary-color);
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
