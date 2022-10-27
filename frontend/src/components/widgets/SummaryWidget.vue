<template>
  <WidgetsLayout
    title="Summary"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-summary-modal')"
  >
    <div class="summary-widget__container">
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
import {mapActions} from 'vuex'
import {action} from '@store/constants'

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
    if (this.isOpenWidget) {
      this[action.GET_SUMMARY_WIDGET](this.projectId)
    }
  },
  computed: {
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
        {name: 'Potential reach', value: 0},
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
    ...mapActions([action.GET_SUMMARY_WIDGET]),
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
        font-size: 28px;
        line-height: 38px;
      }

      .icon {
        display: flex;
        align-items: center;
        justify-content: center;

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

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 10px;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
}
</style>
