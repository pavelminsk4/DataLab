<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <BaseTable
      v-if="tableHeader.length"
      :table-header="tableHeader"
      :isCheckbox="false"
    >
      <tr v-for="(item, index) in widgetData" :key="item.reach + index">
        <td><img src="item.picture" /></td>
        <td>{{ item.name }}</td>
        <td>Gender</td>
        <td>{{ item.media_type }}</td>
        <td>{{ item.posts }}</td>
        <td>
          <ChartsView
            :chart-values="chartValues(item)"
            :chart-type="chartType"
          />
        </td>
        <td>{{ item.reach }}</td>
        <td>{{ item.engagements }}</td>
      </tr>
    </BaseTable>
  </component>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import BaseTable from '@/components/common/BaseTable'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'OverallTopWidget',
  components: {ChartsView, BaseTable, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    chartType() {
      return (
        this.widgetDetails.chart_type || this.widgetDetails.defaultChartType
      )
    },
    widgetData() {
      return this.socialWidgets.overallTopAuthors
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    labels() {
      return ['Positive', 'Negative', 'Neutral'].map((el) => el + ' posts')
    },
  },
  created() {
    if (!this.widgetData.length) {
      this[action.GET_OVERALL_TOP_AUTHORS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
      this.tableHeader = [
        {name: '', width: '5%'},
        {name: 'Author', width: '10%'},
        {name: 'Gender', width: '5%'},
        {name: 'Media Type', width: '5%'},
        {name: 'Posts', width: '5%'},
        {name: 'Sentiment', width: '20%'},
        {name: 'Reach', width: '5%'},
        {name: 'Engagement', width: '5%'},
      ]
    }
  },
  methods: {
    ...mapActions([action.GET_OVERALL_TOP_AUTHORS]),
    chartValues(item) {
      return [
        {
          data: Object.values(item.sentiments),
          colors: ['#00b884', '#ed2549', '#516bee'],
        },
      ]
    },
  },
}
</script>
<style lang="scss">
.widget-layout-wrapper {
  &__content {
    padding: 0;
  }
  .td {
    padding: 0px;
  }
}
</style>
