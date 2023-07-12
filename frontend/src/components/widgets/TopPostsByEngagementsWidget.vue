<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="customTitle || widgetDetails.title"
    style="--widget-layout-content-padding: 0px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <BaseTable
      v-if="tableHeader.length"
      :table-header="tableHeader"
      :has-checkbox="false"
      @sorting-by="sorting"
    >
      <tr
        v-for="(item, index) in tableValue"
        :key="`${item.date}-${index}`"
        class="base-table__row"
      >
        <td>
          <component :is="item.type + 'Icon'" />
        </td>
        <td class="tweet-text">{{ item.text }}</td>
        <td>
          <BaseChips :chipsType="item.sentiment" />
        </td>
        <td>{{ item.engagements }}</td>
        <td>
          {{ item.engmt_rate.toFixed() }}
        </td>
        <td>
          {{ item.date }}
        </td>
      </tr>
    </BaseTable>
  </component>
</template>

<script>
import {SORT_BY} from '@lib/constants'

import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import BaseTable from '@/components/common/BaseTable'
import BaseChips from '@/components/BaseChips'

import textIcon from '@/components/icons/TextIcon'
import retweetIcon from '@/components/icons/RetweetIcon'
import replyIcon from '@/components/icons/ReplyFilledIcon'

export default {
  name: 'TopPostsByEngagementsWidget',
  components: {
    ChartsView,
    BaseTable,
    WidgetsLayout,
    BaseChips,
    textIcon,
    retweetIcon,
    replyIcon,
  },
  props: {
    widgetData: {type: Array, required: true},
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    customTitle: {type: String, default: ''},
    tableHeader: {type: Array, required: true},
  },
  data() {
    return {
      sortBy: {
        property: '',
        condition: '',
      },
    }
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    tableValue() {
      if (!this.sortBy.property) return this.widgetData

      const ratio = this.sortBy.condition === SORT_BY.DESCENDING ? -1 : 1

      if (this.sortBy.property === 'date') {
        return [...this.widgetData].sort(
          (a, b) =>
            ratio *
            (new Date(a[this.sortBy.property]) -
              new Date(b[this.sortBy.property]))
        )
      }

      return [...this.widgetData].sort(
        (a, b) => ratio * (a[this.sortBy.property] - b[this.sortBy.property])
      )
    },
  },
  methods: {
    sorting(property, condition) {
      this.sortBy = {property, condition}
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

  .tweet-text {
    max-width: 450px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
}
</style>
