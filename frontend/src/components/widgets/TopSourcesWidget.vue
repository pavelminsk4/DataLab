<template>
  <component
    :is="widgetWrapper"
    :title="customTitle || widgetDetails.title"
    :is-show-delete-btn="false"
    style="--widget-layout-content-padding: 0px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <BaseTable
      v-if="tableHeader.length"
      :table-header="tableHeader"
      :has-checkbox="false"
    >
      <tr
        v-for="(item, index) in widgetData"
        :key="item.reach + index"
        class="base-table__row"
      >
        <td>
          <UserAvatar
            v-if="item.picture !== 'None'"
            :avatarUrl="item.picture"
          />
        </td>
        <td>
          <div class="source-cell">
            <span>{{ item.name }}</span>
            <span class="source-cell__alias">{{ item.url }}</span>
          </div>
        </td>
        <td>{{ item.posts }}</td>
        <td>
          <ChartsView :chart-values="datasets(item)" :chart-type="chartType" />
        </td>
        <td>{{ item.reach }}</td>
        <td>{{ item.engagements }}</td>
      </tr>
    </BaseTable>
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import BaseTable from '@/components/common/BaseTable'
import UserAvatar from '@/components/UserAvatar'
import TwitterIcon from '@/components/icons/TwitterIcon'
import ChipsGender from '@/components/ChipsGender'

export default {
  name: 'OverallTopWidget',
  components: {
    ChartsView,
    BaseTable,
    WidgetsLayout,
    UserAvatar,
    TwitterIcon,
    ChipsGender,
  },
  props: {
    widgetData: {type: Array, required: true},
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    customTitle: {type: String, default: ''},
    tableHeader: {type: Array, required: true},
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
        }
      })
    },
  },
}
</script>
<style lang="scss" scoped>
.base-table {
  thead {
    background-color: var(--background-primary-color);
    height: 40px;
  }
  &__row:nth-child(n + 2) {
    box-shadow: 0 1px 0 var(--border-color) inset;
  }
}
.icon-wrapper {
  vertical-align: middle;
  padding: 0px 15px;
}
.source-cell {
  display: flex;
  flex-direction: column;

  &__alias {
    font-size: 11px;
  }
}
</style>
