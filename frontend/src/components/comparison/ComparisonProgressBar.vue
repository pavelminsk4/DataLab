<template>
  <ProgressBar
    v-bind="$attrs"
    :progressBarSteps="progressBarSteps"
    class="alert-progress-bar"
  />
</template>

<script>
import ProgressBar from '@/components/ProgressBar'

export default {
  name: 'ComparisonProgressBar',
  components: {ProgressBar},
  created() {
    this.progressBarSteps = [
      'Create workspace',
      'Create project',
      'Select projects',
    ]
  },
}
</script>

<style lang="scss" scoped>
.alert-progress-bar {
  --labels-side-padding: 25px;

  max-width: 850px;
}
</style>
