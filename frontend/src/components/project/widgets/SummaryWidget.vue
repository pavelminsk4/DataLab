<template>
  <WidgetsLayout
    :title="availableWidgets['summary_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <div class="summary-widget__container">
      <div
        v-for="(item, index) in widgetMetrics"
        :key="'metrics' + index"
        class="post-item"
      >
        <component
          :is="item.iconName"
          :style="`background-color: ${item.backgroundColor}`"
          class="icon"
        />
        <div class="title">{{ item.name }}</div>
        <div class="value">{{ summaryData[item.valueName] }}</div>
      </div>
    </div>
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {summaryWidgetConfig} from '@/lib/configs/widgetsConfigs'

import NewPostIcon from '@/components/icons/NewPostIcon'
import NeutralIcon from '@/components/icons/NeutralIcon'
import NegativeIcon from '@/components/icons/NegativeIcon'
import PositiveIcon from '@/components/icons/PositiveIcon'
import SourceIcon from '@/components/icons/SourceIcon'
import PotentialReachIcon from '@/components/icons/PotentialReachIcon'
import CountryIcon from '@/components/icons/CountryIcon'
import AuthorsIcon from '@/components/icons/AuthorsIcon'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'SummaryWidget',
  components: {
    NewPostIcon,
    NeutralIcon,
    NegativeIcon,
    PositiveIcon,
    SourceIcon,
    PotentialReachIcon,
    CountryIcon,
    AuthorsIcon,
    WidgetsLayout,
  },
  props: {
    summaryData: {
      type: [Array, Object],
      required: true,
    },
    projectId: {
      type: [String, Number],
      required: true,
    },
    isOpenWidget: {
      type: Boolean,
      required: true,
    },
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      summary: get.SUMMARY_WIDGET,
    }),
  },
  created() {
    this.widgetMetrics = summaryWidgetConfig

    if (this.isOpenWidget && !this.summary.length) {
      this[action.GET_SUMMARY_WIDGET](this.projectId)
    }
  },
  watch: {
    isOpenWidget() {
      if (this.isOpenWidget) {
        this[action.GET_SUMMARY_WIDGET](this.projectId)
      }
    },
  },
  methods: {
    ...mapActions([action.GET_SUMMARY_WIDGET, action.GET_AVAILABLE_WIDGETS]),
  },
}
</script>

<style lang="scss" scoped>
.summary-widget__container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px 12px;

  .post-item {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    width: 124px;
    height: 76px;

    background: var(--background-secondary-color);
    border-radius: 8px;

    .icon {
      width: 28px;
      height: 28px;
      padding: 6px;
      margin-bottom: 6px;

      border-radius: 4px;

      color: var(--button-text-color);
    }

    .title {
      margin-bottom: 2px;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--typography-primary-color);
    }

    .value {
      font-style: normal;
      font-weight: 700;
      font-size: 18px;
      line-height: 20px;
      letter-spacing: 0.2px;
      color: var(--typography-title-color);
    }
  }
}
</style>
