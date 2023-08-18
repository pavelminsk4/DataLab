<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    :is-show-delete-btn="false"
    :is-show-settings-btn="false"
    style="--widget-layout-content-padding: 0px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <BaseTable
      v-for="(tableHeader, tableIndex) in widgetHeaders"
      :key="'table' + tableIndex"
      :table-header="tableHeader"
      :has-checkbox="false"
      class="overall-top-authors"
    >
      <tr
        v-for="(project, index) in widgetDetails.widgetData"
        :key="project.project"
      >
        <td>
          <div
            :style="`--circle-color: ${projectsColors[index]}`"
            class="circle"
          />
        </td>
        <td>{{ project.project }}</td>
        <td class="most-cell">
          <UserAvatar :avatarUrl="project.data[tableIndex].picture" />
          <div class="author-cell">
            <span>{{ project.data[tableIndex].name }}</span>
            <span class="author-cell__alias">
              <span v-if="project.data[tableIndex].alias">@</span
              >{{
                project.data[tableIndex].alias || project.data[tableIndex].url
              }}
            </span>
          </div>
        </td>
        <td v-if="project.data[tableIndex].gender">
          <BaseChips :chips-type="project.data[tableIndex].gender" />
        </td>
        <td v-if="project.data[tableIndex].source">
          <component
            :is="`${project.data[tableIndex].source}Icon`"
            class="twitter-icon icon"
          />
        </td>
        <td>{{ project.data[tableIndex].value }}</td>
        <td>
          <ChartsView
            :chart-values="datasets(project.data[tableIndex])"
            :chart-type="chartType || 'StackedBarChart'"
            :iteractiveLabel="
              project.data[tableIndex].alias || project.data[tableIndex].name
            "
            :widget-details="widgetDetails"
          />
        </td>
      </tr>
    </BaseTable>
  </component>
</template>

<script>
import {COMPARISON_COLORS} from '@lib/constants'

import BaseChips from '@/components/BaseChips'
import BaseTable from '@/components/common/BaseTable'
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import UserAvatar from '@/components/UserAvatar'
import TwitterIcon from '@/components/icons/TwitterIcon'

export default {
  name: 'OverviewTopSharingSources',
  components: {
    BaseChips,
    ChartsView,
    BaseTable,
    UserAvatar,
    WidgetsLayout,
    TwitterIcon,
  },
  props: {
    widgetDetails: {type: Object, required: true},
    widgetHeaders: {type: Array, required: true},
    isSettings: {type: String, default: ''},
  },
  computed: {
    chartType() {
      return (
        this.widgetDetails.chart_type || this.widgetDetails.defaultChartType
      )
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
  created() {
    this.projectsColors = COMPARISON_COLORS
  },
  methods: {
    datasets(item) {
      const barPercent =
        Object.values(item.sentiments).reduce((a, b) => a + b, 0) /
        Object.values(item.sentiments).length

      const colors = {
        positive: '#00b884',
        negative: '#ed2549',
        neutral: '#516bee',
      }

      return Object.keys(item.sentiments).map((key) => {
        return {
          data: [item.sentiments[key] * barPercent],
          backgroundColor: colors[key],
          borderRadius: 12,
          label: key,
          value: item.name,
        }
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.circle {
  width: 12px;
  height: 12px;

  border-radius: 50%;
  background-color: var(--circle-color);
}

.most-cell {
  display: flex;
  align-items: center;
}

.author-cell {
  display: flex;
  flex-direction: column;

  &__alias {
    font-size: 11px;
  }
}

.icon {
  width: 24px;
  height: 24px;
}

td {
  vertical-align: middle;
}
</style>
