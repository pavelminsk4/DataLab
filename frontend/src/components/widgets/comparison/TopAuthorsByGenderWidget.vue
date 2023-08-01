<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    :is-show-delete-btn="false"
    style="--widget-layout-content-padding: 0px"
    class="height-reset top-authors-by-gender-widget"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <WidgetContainerWithSwitcher
      :tabs="tabs"
      @switch-tab="switchTab"
      widget-max-height="fit-content"
    >
      <OverallTopWidget
        v-for="(widget, index) in widgetData"
        :key="widget.id"
        :widget-data="widget"
        :widget-details="widgetDetails"
        :is-show-delete-btn="false"
        :is-show-settings="false"
        :is-show-settings-btn="false"
        :custom-title="`Overall top authors ${genderTypes[index]}`"
        :table-header="tableHeader"
      />
    </WidgetContainerWithSwitcher>
  </component>
</template>

<script>
import OverallTopWidget from '@/components/widgets/OverallTopWidget'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import WidgetContainerWithSwitcher from '@/components/widgets/WidgetContainerWithSwitcher'

export default {
  components: {OverallTopWidget, WidgetContainerWithSwitcher, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
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
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    tabs() {
      return this.widgetDetails.widgetData.map((project) => project.project)
    },
  },
  created() {
    this.tableHeader = [
      {name: '', width: '5%'},
      {name: 'Author', width: '15%', sortProperty: 'name', hasSort: true},
      {name: 'Gender', width: '15%'},
      {name: 'Media Type', width: '10%'},
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
    this.genderTypes = ['male', 'female']
  },
  methods: {
    switchTab(tab) {
      this.activeTab = tab
    },
  },
}
</script>

<style lang="scss" scoped></style>
