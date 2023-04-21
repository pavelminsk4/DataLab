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
  name: 'AlertsProgressBar',
  components: {ProgressBar},
  created() {
    this.progressBarSteps = [
      'Name the alert',
      'Set alert triggering',
      'Choose projects',
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
