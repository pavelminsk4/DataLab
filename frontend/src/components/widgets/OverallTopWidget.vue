<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="customTitle || widgetDetails.title"
    :is-show-delete-btn="false"
    :is-show-settings-btn="isShowSettingsBtn"
    style="--widget-layout-content-padding: 0px"
    class="widget-table scroll"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <BaseTable
      v-if="tableHeader.length"
      :table-header="tableHeader"
      :has-checkbox="false"
      :has-min-width="true"
      class="overall-top-authors"
      @sorting-by="sorting"
    >
      <tr
        v-for="(item, index) in tableValue"
        :key="`${item.date}-${index}`"
        class="base-table__row"
      >
        <td class="avatar">
          <UserAvatar :avatarUrl="item.picture" />
        </td>
        <td>
          <div class="author-cell">
            <span>{{ item.name }}</span>
            <span class="author-cell__alias">
              <span v-if="item.alias">@</span>{{ item.alias || item.url }}
            </span>
          </div>
        </td>
        <td v-if="item.gender">
          <BaseChips :chips-type="item.gender" />
        </td>
        <td v-if="item.media_type">
          <component :is="`${item.media_type}Icon`" class="icon-wrapper" />
        </td>
        <td>{{ item.posts }}</td>
        <td>
          <ChartsView
            :chart-values="datasets(item)"
            :chart-type="chartType || 'StackedBarChart'"
            :iteractiveLabel="item.alias || item.name"
            :widget-details="widgetDetails"
          />
        </td>
        <td>{{ item.reach }}</td>
        <td>{{ item.engagements }}</td>
      </tr>
    </BaseTable>
  </component>
</template>

<script>
import sortByMixin from '@lib/mixins/sort-for-table.js'

import ChartsView from '@components/charts/ChartsView'
import WidgetsLayout from '@components/layout/WidgetsLayout'
import BaseTable from '@components/common/BaseTable'
import UserAvatar from '@components/UserAvatar'
import TwitterIcon from '@components/icons/TwitterIcon'
import BaseChips from '@components/BaseChips'

export default {
  name: 'OverallTopWidget',
  components: {
    ChartsView,
    BaseTable,
    WidgetsLayout,
    UserAvatar,
    TwitterIcon,
    BaseChips,
  },
  mixins: [sortByMixin],
  props: {
    widgetData: {type: Array, required: true},
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    customTitle: {type: String, default: ''},
    tableHeader: {type: Array, required: true},
    isShowSettingsBtn: {type: Boolean, default: true},
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
          label: key,
          value: item.name,
        }
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.widget-table {
  width: 100%;
}

.base-table {
  &__row:nth-child(n + 2) {
    box-shadow: 0 1px 0 var(--border-color) inset;
  }
  .avatar {
    vertical-align: middle;
  }
}
.icon-wrapper {
  vertical-align: middle;
  width: 24px;
  height: 24px;
}
.author-cell {
  display: flex;
  flex-direction: column;

  &__alias {
    font-size: 11px;
  }
}
</style>

<style lang="scss">
.overall-top-authors {
  cursor: default;

  thead {
    background-color: var(--background-primary-color);
    height: 40px;
  }
}
</style>
