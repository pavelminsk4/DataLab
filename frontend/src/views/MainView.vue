<template>
  <MainLayout>
    <MainLayoutTitleBlock :title="`Hello, ${fullName} &#x1F44B;`" />

    <div class="modules scroll">
      <div
        v-for="item in modules"
        :key="item.name"
        :style="`
          --module-background-color: ${item.color};
          --module-background-image: url(${item.imageUrl});
          --module-background-position: ${item.backgroundPosition};`"
        :class="['module-card', !item.openRouteName && 'disable']"
        @click="$router.push({name: item.openRouteName})"
      >
        <div>
          <h3 class="module-name">{{ item.name }}</h3>
          <p class="module-description">{{ item.description }}</p>
        </div>

        <BaseButton
          :is-not-background="true"
          @click.stop="
            $router.push({
              name: item.createRouteName,
              params: {workspaceId: 'new'},
            })
          "
        >
          <PlusIcon />
          <span>{{ item.buttonName }}</span>
        </BaseButton>
      </div>
    </div>
  </MainLayout>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import BaseButton from '@components/common/BaseButton'
import PlusIcon from '@/components/icons/PlusIcon'

export default {
  components: {BaseButton, MainLayout, MainLayoutTitleBlock, PlusIcon},
  computed: {
    ...mapGetters({userInfo: get.USER_INFO}),
    fullName() {
      const fullName = `${this.userInfo?.first_name} ${this.userInfo?.last_name}`
      return fullName ? fullName : this.userInfo?.username
    },
  },
  created() {
    this.modules = [
      {
        name: 'Online',
        description: 'News from online media',
        buttonName: 'Add Workspace',
        openRouteName: 'OnlineHome',
        createRouteName: 'OnlineCreateWorkspace',
        color: '#E0E5FF',
        imageUrl: require('@/assets/modules/online.svg'),
        backgroundPosition: 'right 33px bottom',
      },
      {
        name: 'Social Media',
        description: 'News from social media posts',
        buttonName: 'Add Workspace',
        openRouteName: 'SocialHome',
        createRouteName: 'SocialCreateWorkspace',
        color: '#FCDCE3',
        imageUrl: require('@/assets/modules/social-media.svg'),
        backgroundPosition: 'right 23px bottom',
      },
      // {
      //   name: 'TV & Radio',
      //   description: 'Delivers results from Radio and TV',
      //   buttonName: 'Add Workspace',
      //   openRouteName: '',
      //   createRouteName: '',
      //   color: '#C0DFF4',
      //   imageUrl: require('@/assets/modules/tv&radio.svg'),
      //   backgroundPosition: 'right bottom',
      // },
      {
        name: 'Account Analysis',
        description: 'Monitor social media content created by influencers',
        buttonName: 'Add Report',
        openRouteName: 'AccountAnalysis',
        createRouteName: 'AccountAnalysisCreateWorkspace',
        color: '#E5E9FC',
        imageUrl: require('@/assets/modules/account-analysis.svg'),
        backgroundPosition: 'right bottom',
      },
      {
        name: '24/7',
        description: 'Collect and process news for your publications',
        buttonName: 'Add Workspace',
        openRouteName: 'TwentyFourSeven',
        createRouteName: 'TwentyFourSevenCreateWorkspace',
        color: '#C0DFF4',
        imageUrl: require('@/assets/modules/tfs.svg'),
        backgroundPosition: 'right 0 bottom 0',
      },
      {
        name: 'Reports',
        description: 'Regular reports with analytics',
        buttonName: 'Add Report',
        openRouteName: 'Reports',
        createRouteName: 'CreateReport',
        color: '#E5E9FC',
        imageUrl: require('@/assets/modules/reports.svg'),
        backgroundPosition: 'right 14px bottom 12px',
      },
      {
        name: 'Alerts',
        description: 'Get the news when given thresholds are met',
        buttonName: 'Add Alert',
        openRouteName: 'Alerts',
        createRouteName: 'CreateAlert',
        color: '#FFEDF1',
        imageUrl: require('@/assets/modules/alerts.svg'),
        backgroundPosition: 'right bottom',
      },
      {
        name: 'Comparison module',
        description: 'Monitor social media content created by influencers ',
        buttonName: 'Add Workspace',
        openRouteName: 'Comparison',
        createRouteName: 'ComparisonCreateWorkspace',
        color: '#FCDCE3',
        imageUrl: require('@/assets/modules/comparison.svg'),
        backgroundPosition: 'right bottom',
      },
    ]
  },
}
</script>

<style lang="scss" scoped>
.modules {
  display: flex;
  flex-wrap: wrap;
  gap: 32px;

  padding: 40px 32px;
}

.module-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  width: 436px;
  height: 196px;
  padding: 20px;

  background: no-repeat var(--module-background-position)
    var(--module-background-image) var(--module-background-color);
  border-radius: var(--border-radius);
  box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);

  cursor: pointer;
  transition-duration: 0.4s;

  &:hover {
    transform: scale(1.075);
  }
}

.module-name {
  font-size: 20px;
}

.module-description {
  width: 60%;
}
</style>
