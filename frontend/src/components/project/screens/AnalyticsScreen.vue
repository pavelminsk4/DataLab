<template>
  <div>
    <NavigationBar
      v-if="currentProject"
      :title="currentProject.title"
      :hint="'Search by keywords and phrases '"
      :is-show-button="false"
    />
  </div>
</template>

<script>
import NavigationBar from '@/components/navigation/NavigationBar'

export default {
  name: 'AnalyticsScreen',
  components: {NavigationBar},
  props: {
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
}
</script>

<style scoped></style>
