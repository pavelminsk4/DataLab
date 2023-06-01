<template>
  <component
    :is="widgetWrapper"
    :title="customTitle || widgetDetails.title"
    style="--widget-layout-content-padding: 0px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <BaseTable
      v-if="tableHeader.length"
      :table-header="tableHeader"
      :has-checkbox="false"
    >
      <tr v-for="item in widgetData" :key="item.date" class="base-table__row">
        <td>
          <UserAvatar :avatar-url="item.picture" />
        </td>
        <td class="author-cell">
          <span>{{ item.name }}</span>
          <span class="author-cell__alias">@{{ item.alias }}</span>
        </td>
        <td class="tweet-text">{{ item.text }}</td>
        <td>
          <BaseChips :chipsType="item.sentiment" />
        </td>
        <td>{{ item.engagements }}</td>
        <td>{{ item.likes }}</td>
        <td>{{ item.retweets }}</td>
        <td class="date-cell">
          {{ item.date }}
        </td>
      </tr>
    </BaseTable>
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import BaseTable from '@/components/common/BaseTable'
import BaseChips from '@/components/BaseChips'
import UserAvatar from '@/components/UserAvatar'

export default {
  name: 'TopPostsByEngagementsWidget',
  components: {
    ChartsView,
    BaseTable,
    WidgetsLayout,
    BaseChips,
    UserAvatar,
  },
  props: {
    widgetData: {type: Array, required: true},
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    customTitle: {type: String, default: ''},
    tableHeader: {type: Array, required: true},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
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
    max-width: 300px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .author-cell {
    display: flex;
    flex-direction: column;

    &__alias {
      font-size: 11px;
    }
  }

  .date-cell {
    font-size: 11px;
  }
}
</style>
