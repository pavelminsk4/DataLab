<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    style="--widget-layout-content-padding: 0px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <table class="table">
      <thead>
        <th></th>
        <th class="project-header">project</th>
        <th
          v-for="item in widgetMetrics"
          :key="'header' + item.valueName"
          class="post-item"
        >
          <component
            :is="item.iconName"
            :style="`background-color: ${item.backgroundColor}`"
            class="icon"
          />
          <div class="title">{{ item.name }}</div>
        </th>
      </thead>
      <tbody>
        <tr v-for="(project, index) in tableRows" :key="project.project">
          <td>
            <div
              :style="`--circle-color: ${projectsColors[index - 1]}`"
              class="circle"
            />
          </td>
          <td class="project-name">{{ project.project }}</td>
          <td
            v-for="item in widgetMetrics"
            :key="item.name"
            :class="!index && 'total-value'"
          >
            {{ project.data[item.valueName] }}
          </td>
        </tr>
      </tbody>
    </table>
  </component>
</template>

<script>
import {COMPARISON_COLORS} from '@lib/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'

import NewPostIcon from '@/components/icons/NewPostIcon'
import NeutralIcon from '@/components/icons/NeutralIcon'
import NegativeIcon from '@/components/icons/NegativeIcon'
import PositiveIcon from '@/components/icons/PositiveIcon'
import SourceIcon from '@/components/icons/SourceIcon'
import PotentialReachIcon from '@/components/icons/PotentialReachIcon'
import CountryIcon from '@/components/icons/CountryIcon'
import AuthorIcon from '@/components/icons/AuthorIcon'
import LikeIcon from '@/components/icons/LikeIcon'
import RepliesIcon from '@/components/icons/RepliesIcon'
import RetweetIcon from '@/components/icons/RetweetIcon'

export default {
  name: 'SummaryTableWidget',
  components: {
    LikeIcon,
    RepliesIcon,
    RetweetIcon,
    NewPostIcon,
    NeutralIcon,
    NegativeIcon,
    PositiveIcon,
    SourceIcon,
    PotentialReachIcon,
    CountryIcon,
    AuthorIcon,
    WidgetsLayout,
  },
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    widgetData: {type: Object, required: true},
    widgetMetrics: {type: Object, required: true},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    tableRows() {
      const totalData = {}
      Object.keys(this.widgetData[0].data).forEach(
        (valueName) =>
          (totalData[valueName] = this.widgetData.reduce(
            (sum, currentItem) => sum + currentItem.data[valueName],
            0
          ))
      )

      return [
        {
          project: '',
          data: totalData,
        },
        ...this.widgetData,
      ]
    },
  },
  created() {
    this.projectsColors = COMPARISON_COLORS
  },
}
</script>

<style lang="scss" scoped>
.table {
  width: 100%;

  border-collapse: collapse;

  thead {
    background-color: var(--background-primary-color);
  }

  th {
    padding: 8px 16px;

    text-align: start;
    vertical-align: top;
    font-size: 11px;
    font-weight: 400;
  }

  td {
    padding: 17px 16px;

    font-size: 14px;
    color: var(--typography-primary-color);
  }

  tr:not(:last-child) {
    td {
      border-bottom: var(--border-primary);
    }
  }

  .project-header {
    vertical-align: middle;
  }

  .project-name {
    width: 28%;

    font-size: 16px;
    font-weight: 500;
  }

  .total-value {
    font-weight: 600;
  }
}

.icon {
  width: 28px;
  height: 28px;
  padding: 6px;
  margin-bottom: 6px;

  border-radius: 4px;

  color: var(--button-text-color);
}

.circle {
  width: 12px;
  height: 12px;

  border-radius: 50%;
  background-color: var(--circle-color);
}
</style>
