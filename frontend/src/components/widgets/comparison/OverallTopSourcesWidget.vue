<template>
  <WidgetContainerWithSwitcher
    :tabs="tabs"
    @switch-tab="switchTab"
    widget-max-height="fit-content"
  >
    <OverallTopWidget
      :widget-details="widgetDetails"
      :widget-data="widgetData"
      :table-header="tableHeader"
      :is-show-settings-btn="false"
    />
  </WidgetContainerWithSwitcher>
</template>

<script>
import WidgetContainerWithSwitcher from '@/components/widgets/WidgetContainerWithSwitcher'
import OverallTopWidget from '@/components/widgets/OverallTopWidget'

export default {
  name: 'OverallTopSourcesWidget',
  components: {OverallTopWidget, WidgetContainerWithSwitcher},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  data() {
    return {
      activeTab: this.widgetDetails.widgetData[0].project,
    }
  },
  computed: {
    widgetData() {
      return this.widgetDetails.widgetData.find(
        (project) => project.project === this.activeTab
      ).data
    },
    tabs() {
      return this.widgetDetails.widgetData.map((project) => project.project)
    },
  },
  created() {
    this.tableHeader = [
      {name: '', width: '5%'},
      {name: 'Author', width: '15%', sortProperty: 'name', hasSort: true},
      {name: 'Posts', width: '10%', sortProperty: 'posts', hasSort: true},
      {name: 'Sentiment', width: '25%'},
      {name: 'Reach', width: '10%', sortProperty: 'reach', hasSort: true},
      {
        name: 'Engagement',
        width: '10%',
        sortProperty: 'engagements',
        hasSort: true,
      },
    ]
  },
  methods: {
    switchTab(tab) {
      this.activeTab = tab
    },
  },
}
</script>
