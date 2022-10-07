<template>
  <section class="summary-widget">
    <div class="summary-widget__header">
      <div class="title">Summary</div>
    </div>

    <div class="summary-widget__container">
      <table>
        <tr v-for="(item, index) in widgetMetricsFirst" :key="'metric' + index">
          <td class="metric-name">{{ item.name.toUpperCase() }}</td>
          <td class="metric-value">{{ item.value }}</td>
          <td class="metric-count">+1</td>
          <td class="metric-badge">+10%</td>
        </tr>
      </table>

      <table>
        <tr
          v-for="(item, index) in widgetMetricsSecond"
          :key="'metric' + index"
        >
          <td class="metric-name summary-name">
            {{ item.name.toUpperCase() }}
          </td>
          <td class="metric-value">{{ item.value }}</td>
          <td class="metric-count">+1</td>
          <td class="metric-badge">+10%</td>
        </tr>
      </table>
    </div>
  </section>
</template>

<script>
export default {
  name: 'SummaryWidget',
  props: {
    summaryData: {
      type: [Array, Object],
      required: true,
    },
  },
  computed: {
    widgetMetricsFirst() {
      return [
        {name: 'New posts', value: this.summaryData?.posts},
        {name: 'Source', value: this.summaryData?.sources},
        {name: 'Authors', value: this.summaryData?.authors},
        {name: 'Countries', value: this.summaryData?.countries},
      ]
    },
    widgetMetricsSecond() {
      return [
        {name: 'Potential reach', value: this.summaryData?.reach},
        {name: 'Neutral', value: this.summaryData?.neut},
        {name: 'Negative', value: this.summaryData?.neg},
        {name: 'Positive', value: this.summaryData?.pos},
      ]
    },
  },
}
</script>

<style lang="scss" scoped>
.summary-widget {
  display: flex;
  flex-direction: column;

  min-width: 100%;
  min-height: 100%;
  padding: 12px 20px 35px;

  &__header {
    width: 100%;
    padding-bottom: 12px;

    border-bottom: 1px solid var(--input-border-color);

    .title {
      font-style: normal;
      font-weight: 600;
      font-size: 16px;
      line-height: 22px;
    }
  }

  &__container {
    display: flex;
    justify-content: space-between;

    margin-top: 25px;

    table {
      color: var(--primary-text-color);
    }

    .metric-name {
      width: 100px;

      font-style: normal;
      font-weight: 400;
      font-size: 12px;
      line-height: 20px;
      color: var(--secondary-text-color);
    }

    .summary-name {
      width: 150px;
    }

    .metric-value {
      width: 32px;

      font-style: normal;
      font-weight: 600;
      font-size: 16px;
      line-height: 22px;
    }

    .metric-count {
      width: 21px;

      color: var(--negative-status);
    }

    .metric-badge {
      padding: 3px 9px;

      border-radius: 29px;
      background-color: rgba(51, 204, 112, 0.2);

      color: var(--tag-color);
    }
  }
}
</style>
