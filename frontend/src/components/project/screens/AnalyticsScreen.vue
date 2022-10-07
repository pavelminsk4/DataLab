<template>
  <div v-if="currentProject">
    <NavigationBar
      v-if="currentProject"
      :title="currentProject.title"
      :hint="'Search by keywords and phrases '"
      :is-show-button="false"
    />

    <WidgetsView :project-id="currentProject.id" />
  </div>
</template>

<script>
import NavigationBar from '@/components/navigation/NavigationBar'
import WidgetsView from '@/components/widgets/WidgetsView'

export default {
  name: 'AnalyticsScreen',
  components: {WidgetsView, NavigationBar},
  props: {
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
}
</script>

<style scoped></style>
