<template>
  <MainLayout
    v-if="currentProject"
    :is-project-extra-settings="true"
    :is-visible-logo="false"
  >
    <div class="settings-nav-wrapper">
      <LogoIcon class="logo" @click="goToDashboard" />

      <div
        v-for="(item, index) in settings"
        :key="'setting' + index"
        :class="['nav-item', item.name === routeName && 'active-setting']"
        @click="openSetting(item.name)"
      >
        <SidebarIcon :json="item.value" />

        <div class="tooltip">{{ item.name }}</div>
      </div>
    </div>

    <router-view :current-project="currentProject"></router-view>
  </MainLayout>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import MainLayout from '@/components/layout/MainLayout'

import SidebarIcon from '@/components/icons/SidebarIcon'
import LogoIcon from '@/components/icons/LogoIcon'

import Alerts from '@/components/icons/animation/Alerts.json'
import Search from '@/components/icons/animation/Search.json'
import Reports from '@/components/icons/animation/Reports.json'
import Analytics from '@/components/icons/animation/Analytics.json'

export default {
  name: 'ProjectReports',
  components: {
    LogoIcon,
    MainLayout,
    SidebarIcon,
  },
  data() {
    return {
      settings: [
        {
          name: 'Analytics',
          value: Analytics,
        },
        {
          name: 'Search',
          value: Search,
        },
        {
          name: 'Alerts',
          value: Alerts,
        },
        {
          name: 'Reports',
          value: Reports,
        },
      ],
    }
  },
  created() {
    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
  },
  computed: {
    ...mapState(['workspaces']),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    projectId() {
      return this.$route.params.projectId
    },
    currentWorkspace() {
      return this.workspaces.filter((el) => el.id === +this.workspaceId)
    },
    currentProject() {
      return this.currentWorkspace[0]?.projects.filter(
        (el) => el.id === +this.projectId
      )[0]
    },
    projectName() {
      return this.currentProject?.title
    },
    routeName() {
      return this.$route.name
    },
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
    // TODO: I don't like this name
    openSetting(pathName) {
      this.$router.push({
        name: pathName,
      })
    },
    goToDashboard() {
      this.$router.push({
        name: 'Home',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-nav-wrapper {
  position: fixed;
  top: 16px;
  left: 24px;
  z-index: 10;

  display: flex;
  flex-direction: column;
  align-items: center;

  width: 72px;
  height: 96vh;

  border: 1px solid var(--sidebar-border-color);
  border-radius: 15px;
  background-color: var(--secondary-bg-color);

  .logo {
    cursor: pointer;
    opacity: 0;

    width: 0;
    height: 0;
    margin: 18px 10px 50px;
  }

  .nav-item {
    position: relative;

    cursor: pointer;

    width: 35px;
    height: 35px;
    padding: 5px;
    margin-bottom: 30px;
  }

  .active-setting {
    border-radius: 6px;
    background-color: var(--button-primary-color);
  }

  .tooltip {
    position: absolute;
    top: 0;
    left: 50px;
    z-index: 1;

    visibility: hidden;
    text-align: center;

    padding: 10px;

    border-radius: 6px;

    background-color: var(--primary-text-color);

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 110%;

    &::after {
      content: '';

      position: absolute;
      top: 48%;
      left: 0;
      transform: translate(-50%, -50%) rotate(230deg);

      margin-left: 2px;

      border-width: 5px;
      border-style: solid;
      border-top-right-radius: 2px;
      color: var(--primary-text-color);
    }
  }

  .nav-item:hover .tooltip {
    visibility: visible;
  }
}
</style>
