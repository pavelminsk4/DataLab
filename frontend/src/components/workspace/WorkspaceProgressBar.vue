<template>
  <ProgressBar v-bind="$attrs" :progressBarSteps="progressBarSteps" />
</template>

<script>
import ProgressBar from '@components/ProgressBar'

export default {
  name: 'WorkspaceProgressBar',
  components: {ProgressBar},
  created() {
    this.progressBarSteps = [
      'Create workspace',
      'Create project',
      'Define the search',
    ]
  },
}
</script>
