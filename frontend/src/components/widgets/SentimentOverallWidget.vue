<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <div :class="['container', isSettings && 'settings-view']">
      <div
        v-for="(item, index) in widgetMetrics"
        :key="'metrics' + index"
        class="item"
      >
        <div>
          <component
            :is="item.iconName"
            :style="`background-color: ${item.backgroundColor}`"
            class="icon"
          />
          <CustomText :text="item.name" class="title" />
        </div>
        <div>
          <div :class="['value', item.className]">
            {{ widgetData[item.valueName] }}
          </div>
          <CustomText tag="span" text="result" />
        </div>
      </div>
    </div>
  </component>
</template>

<script>
import {sentimentOverallWidgetConfig} from '@lib/configs/widgetsConfigs'

import CustomText from '@components/CustomText'
import NeutralIcon from '@components/icons/NeutralIcon'
import NegativeIcon from '@components/icons/NegativeIcon'
import PositiveIcon from '@components/icons/PositiveIcon'
import WidgetsLayout from '@components/layout/WidgetsLayout'

export default {
  name: 'SentimentOverallWidget',
  components: {
    NeutralIcon,
    NegativeIcon,
    PositiveIcon,
    WidgetsLayout,
    CustomText,
  },
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    widgetData: {type: Object, required: true},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
  created() {
    this.widgetMetrics = sentimentOverallWidgetConfig
  },
}
</script>

<style lang="scss" scoped>
.settings-view {
  padding: 24px;
}

.container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px 12px;

  justify-content: space-between;

  height: 60%;

  cursor: default;

  .item {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

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
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--typography-primary-color);
    }

    .value {
      font-weight: 700;
      font-size: 56px;
      line-height: 56px;
      letter-spacing: 0.2px;
      color: var(--typography-title-color);
    }

    .pos {
      color: var(--positive-primary-color);
    }
    .neut {
      color: var(--neutral-primary-color);
    }
    .neg {
      color: var(--negative-primary-color);
    }
  }
}
</style>
