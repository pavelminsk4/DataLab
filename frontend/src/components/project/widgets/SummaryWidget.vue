<template>
  <WidgetsLayout
    :title="availableWidgets['summary_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <div class="summary-widget__container scroll">
      <div
        v-for="(item, index) in widgetMetrics"
        :key="'metrics' + index"
        class="post-item"
      >
        <div class="title">{{ item.name.toUpperCase() }}</div>
        <div class="values">
          <div class="value">{{ item.value }}</div>
          <div :class="['icon', item?.style]"><PostIcon /></div>
        </div>
      </div>
    </div>
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import PostIcon from '@/components/icons/PostIcon'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'SummaryWidget',
  components: {PostIcon, WidgetsLayout},
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
  created() {
    if (this.isOpenWidget && !this.summary.length) {
      this[action.GET_SUMMARY_WIDGET](this.projectId)
    }
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      summary: get.SUMMARY_WIDGET,
    }),
    widgetMetrics() {
      return [
        {name: 'New posts', value: this.summaryData?.posts},
        {name: 'Neutral post', value: this.summaryData?.neut, style: 'neutral'},
        {
          name: 'Negative post',
          value: this.summaryData?.neg,
          style: 'negative',
        },
        {
          name: 'Positive post',
          value: this.summaryData?.pos,
          style: 'positive',
        },
        {name: 'Source', value: this.summaryData?.sources},
        {name: 'Potential reach', value: this.summaryData?.reach},
        {name: 'Countries', value: this.summaryData?.countries},
        {name: 'Authors', value: this.summaryData?.authors},
      ]
    },
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
  gap: 15px;

  margin-top: 25px;

  overflow: auto;

  .post-item {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    width: 136px;
    height: 97px;

    padding: 15px 23px 15px 20px;

    background: var(--primary-bg-color);
    border-radius: 8px;

    .title {
      font-style: normal;
      font-weight: 400;
      font-size: 12px;
      line-height: 16px;
    }

    .values {
      display: flex;
      justify-content: space-between;
      align-items: center;

      .value {
        font-style: normal;
        font-weight: 600;
        font-size: 1rem;
        line-height: 38px;
      }

      .icon {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        flex-grow: 0;

        width: 22px;
        height: 22px;

        border-radius: 100%;
        background-color: var(--primary-button-color);
      }

      .negative {
        background-color: var(--negative-status);
      }

      .positive {
        background-color: var(--tag-color);
      }

      .neutral {
        background-color: var(--neutral-status);
      }
    }
  }
}
</style>
