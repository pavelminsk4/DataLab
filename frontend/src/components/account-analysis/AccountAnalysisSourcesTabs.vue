<template>
  <div class="sources-tabs">
    <div
      v-for="(item, index) in sources"
      :key="item.name + index"
      :class="[
        'source-tab',
        selectedSouce === item.name && 'active-source',
        item.disabled && 'disable',
      ]"
    >
      <component :is="item.name.concat() + 'Icon'" class="icon" />
      {{ item.name.concat() }}
    </div>
  </div>
</template>

<script>
import TikTokIcon from '@/components/icons/TikTokIcon'
import TwitterIcon from '@/components/icons/TwitterIcon'
import InstagramIcon from '@/components/icons/InstagramIcon'
import FacebookIcon from '@/components/icons/FacebookIcon'
import YoutubeIcon from '@/components/icons/YoutubeIcon'
import LinkedInIcon from '@/components/icons/LinkedInIcon'
import GoogleReviewsIcon from '@/components/icons/GoogleReviewsIcon'

export default {
  name: 'AccountAnalysisSourcesTabs',
  components: {
    TikTokIcon,
    TwitterIcon,
    FacebookIcon,
    InstagramIcon,
    YoutubeIcon,
    LinkedInIcon,
    GoogleReviewsIcon,
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
        disabled: false,
      },
      {
        name: 'Instagram',
        disabled: true,
      },
      {
        name: 'Facebook',
        disabled: true,
      },
      {
        name: 'Youtube',
        disabled: true,
      },
      {
        name: 'TikTok',
        disabled: true,
      },
      {
        name: 'LinkedIn',
        disabled: true,
      },
      {
        name: 'GoogleReviews',
        disabled: true,
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
