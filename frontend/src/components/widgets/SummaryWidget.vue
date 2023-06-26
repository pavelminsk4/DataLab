<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <div :class="['summary-widget__container', isSettings && 'settings-view']">
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
        <div class="value">{{ summaryWidgetData[item.valueName] }}</div>
      </div>
    </div>
  </component>
</template>

<script>
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
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'SummaryWidget',
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
    summaryWidgetData: {type: Object, required: true},
    widgetMetrics: {type: Object, required: true},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-view {
  padding: 24px;
}

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
