<template>
  <div class="progress-bar-wrapper">
    <div class="progress-bar">
      <template
        v-for="(step, index) in progressBarSteps"
        :key="`step_${index}`"
      >
        <div
          :class="[
            'circle',
            `step${index + 1}` <= activeStep && 'active-circle',
          ]"
        >
          <RectangleIcon v-if="`step${index + 1}` === activeStep" />
          <TickIcon v-if="`step${index + 1}` < activeStep" />
        </div>

        <div v-if="index + 1 < progressBarSteps.length" class="line"></div>
      </template>
    </div>

    <div class="labels">
      <div
        v-for="(step, index) in progressBarSteps"
        :key="`label_${index}`"
        class="label"
      >
        <CustomText :text="step" />
      </div>
    </div>
  </div>
</template>

<script>
import CustomText from '@/components/CustomText'

import RectangleIcon from '@/components/icons/RectangleIcon'
import TickIcon from '@/components/icons/TickIcon'

export default {
  name: 'ProgressBar',
  components: {
    RectangleIcon,
    TickIcon,
    CustomText,
  },
  props: {
    step: {type: String, default: ''},
    progressBarSteps: {type: Array, required: true},
  },
  computed: {
    currentStep() {
      return this.$route?.name.match(/Step(.*)/)[0].toLowerCase()
    },
    activeStep() {
      return this.step || this.currentStep
    },
  },
}
</script>

<style lang="scss" scoped>
.progress-bar-wrapper {
  --labels-side-padding: 8px;

  display: flex;
  flex-direction: column;
  gap: 12px;

  width: 100%;
  max-width: 496px;
}

.progress-bar {
  display: flex;
  align-items: center;
  gap: 12px;

  padding: 0 44px;

  .line {
    flex-grow: 2;

    border-radius: 3px;
    border: 3px solid var(--border-color);
  }

  .circle {
    width: 56px;
    height: 56px;

    border-radius: 50%;
    border: 13px solid var(--border-color);

    color: var(--background-secondary-color);

    svg {
      color: var(--background-secondary-color);
    }
  }

  .active-circle {
    display: flex;
    justify-content: center;
    align-items: center;

    border-color: var(--border-active-color);
    background: var(--border-active-color);
  }
}

.labels {
  display: flex;
  justify-content: space-between;
  gap: 10px;

  padding: 0 var(--labels-side-padding);

  .label {
    text-align: center;
  }
}
</style>
