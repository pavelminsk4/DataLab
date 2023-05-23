<template>
  <div class="statuses-wrapper">
    <div :style="`background-color: ${statuses[0].color}`" class="title">
      Picking
    </div>
    <div :style="`background-color: ${statuses[0].color}`" class="icon-wrapper">
      <ArrowDownIcon class="arrow-icon" />
    </div>
  </div>
</template>

<script>
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'

export default {
  name: 'TFSCardStatuses',
  components: {
    ArrowDownIcon,
  },
  data() {
    return {
      statuses: [
        {name: 'Picking', color: '#2A7697'},
        {name: 'Summary', color: '#3746A6'},
        // {name: 'Back to summary', color: '#3746A6'},
        {name: 'Q&A Check', color: '#AB3E00'},
        // {name: 'Back to Q&A Check', color: '#AB3E00'},
        {name: 'Publishing', color: '#168500'},
        {name: 'Published', color: '#961CCF'},
        {name: 'Irrelevant', color: '#797D80'},
      ],
    }
  },
}
</script>

<style lang="scss" scoped>
.statuses-wrapper {
  display: flex;
  gap: 2px;

  cursor: pointer;

  .title {
    padding: 6px 8px;

    border-radius: 4px;

    font-style: normal;
    font-weight: 400;
    font-size: 11px;
    line-height: 12px;
    color: var(--background-secondary-color);
  }

  .icon-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;

    padding: 6px 8px;

    border-radius: 4px;

    .arrow-icon {
      width: 8px;
      height: 8px;

      transform: rotate(-90deg);
      color: var(--background-secondary-color);
    }
  }
}
</style>
