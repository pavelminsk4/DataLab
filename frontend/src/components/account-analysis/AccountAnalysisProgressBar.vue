<template>
  <ProgressBar v-bind="$attrs" :progressBarSteps="progressBarSteps" />
</template>

<script>
import ProgressBar from '@/components/ProgressBar'

export default {
  name: 'AccountAnalysisProgressBar',
  components: {ProgressBar},
  created() {
    this.progressBarSteps = ['Create workspace', 'Create project']
  },
}
</script>
