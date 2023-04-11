<template>
  <ProgressBar
    v-bind="$attrs"
    :progressBarSteps="progressBarSteps"
    class="report-progress-bar"
  />
</template>

<script>
import ProgressBar from '@/components/ProgressBar'

export default {
  name: 'WorkspaceProgressBar',
  components: {ProgressBar},
  created() {
    this.progressBarSteps = [
      'Name the report',
      'Set send time',
      'Choose projects',
      'Choose templates',
      'Edit the report',
    ]
  },
}
</script>

<style lang="scss" scoped>
.report-progress-bar {
  --labels-side-padding: 25px;

  max-width: 850px;
}
</style>
