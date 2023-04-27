<template>
  <div class="sources-tabs">
    <div
      v-for="(item, index) in sources"
      :key="item.name + index"
      :class="['source-tab', selectedSouce === item.name && 'active-source']"
    >
      <component :is="item.name.concat() + 'Icon'" class="icon" />
      {{ item.name }}
    </div>
  </div>
</template>

<script>
import TikTokIcon from '../icons/TikTokIcon.vue'
import TwitterIcon from '../icons/TwitterIcon.vue'

export default {
  name: 'AccountAnalysisSourcesTabs',
  components: {
    TikTokIcon,
    TwitterIcon,
  },
  props: {
    selected: {type: String, default: ''},
  },
  data() {
    return {
      selectedSouce: 'Twitter',
    }
  },
  created() {
    this.sources = [
      {
        name: 'Twitter',
      },
      {
        name: 'Instagram',
      },
      {
        name: 'Facebook',
      },
      {
        name: 'Youtube',
      },
      {
        name: 'TikTok',
      },
      {
        name: 'Linkedln',
      },
      {
        name: 'GoogleReviews',
      },
    ]
  },
}
</script>

<style lang="scss" scoped>
.sources-tabs {
  display: flex;
  gap: 2px;

  padding: 4px;
  height: 56px;

  background: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: 12px;

  .source-tab {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 4px;

    height: 48px;
    width: 92px;

    font-weight: 400;
    font-size: 11px;
    line-height: 12px;

    .icon {
      width: 24px;
      height: 24px;
    }
  }

  .active-source {
    border-radius: 10px;
    background-color: var(--primary-active-color);
  }
}
</style>
