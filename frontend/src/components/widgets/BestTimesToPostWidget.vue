<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    :is-show-delete-btn="false"
    style="--widget-layout-content-padding: 0px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ul v-if="widgetData.length" class="container">
      <li v-for="item in widgetData" :key="item.date" class="row">
        <CustomText tag="span" :text="item.weekday" class="stats__item" />
        <span class="stats__item" style="font-size: 16px">{{ item.time }}</span>
        <span class="stats__item" style="font-size: 11px">
          <CustomText tag="span" text="AVG Engagements" class="stats__item" />
          {{ item.engagements.toFixed() }}
        </span>
        <div class="stats__item">
          <LikeIcon />
          <span>{{ item.likes }}</span>
        </div>
        <div class="stats__item">
          <RetweetIcon />
          <span>{{ item.retweets }}</span>
        </div>
        <div class="stats__item">
          <RepliesIcon />
          <span>{{ item.replies }}</span>
        </div>
      </li>
    </ul>
  </component>
</template>

<script>
import CustomText from '@/components/CustomText'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import LikeIcon from '@/components/icons/LikeIcon'
import RetweetIcon from '@/components/icons/RetweetIcon'
import RepliesIcon from '@/components/icons/RepliesIcon'

export default {
  name: 'BestTimesToPostWidget',
  components: {WidgetsLayout, LikeIcon, RetweetIcon, RepliesIcon, CustomText},
  props: {
    widgetDetails: {type: Object, required: true},
    widgetData: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  display: grid;

  height: 100%;
  padding: 12px;

  list-style: none;

  .row {
    display: grid;
    grid-template-columns: 2fr 1fr 2fr repeat(3, 1fr);

    grid-column-gap: 8px;
    padding: 25px 0px;

    border-bottom: 1px var(--border-color) solid;

    .stats__item {
      display: flex;
      align-items: center;
      justify-content: center;

      height: 100%;
      gap: 5px;

      border-right: 1px var(--border-color) solid;

      &:first-child {
        justify-content: flex-start;
      }

      &:last-child {
        border-right: none;
      }
    }

    &:last-child {
      border-bottom: none;
    }
  }
}
</style>
