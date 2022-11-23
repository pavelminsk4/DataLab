<template>
  <MainLayout :is-project-extra-settings="true" :is-visible-logo="false">
    <div class="settings-nav-wrapper">
      <LogoIcon class="logo" @click="goToDashboard" />

      <div
        v-for="(item, index) in settings"
        :key="'setting' + index"
        :class="['nav-item', item.name === settingName && 'active-setting']"
        @click="openSetting(item.name)"
      >
        <AnalyticsIcon :json="item.value" />

        <div class="tooltip">{{ item.name }}</div>
      </div>
    </div>
    <component :is="settingName + 'Screen'" :current-project="currentProject" />
  </MainLayout>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import MainLayout from '@/components/layout/MainLayout'
import ReportsScreen from '@/components/project/screens/ReportsScreen'
import AlertsScreen from '@/components/project/screens/AlertsScreen'
import SearchScreen from '@/components/project/screens/SearchScreen'
import AnalyticsScreen from '@/components/project/screens/AnalyticsScreen'

import AnalyticsIcon from '@/components/icons/AnalyticsIcon'
import SearchIcon from '@/components/icons/SearchIcon'
import AlertsIcon from '@/components/icons/AlertsIcon'
import ReportsIcon from '@/components/icons/ReportsUploadIcon'
import SettingsIcon from '@/components/icons/SettingsIcon'
import LogoIcon from '@/components/icons/LogoIcon'

import Analytics from '@/components/icons/animation/Analytics.json'
import Search from '@/components/icons/animation/Search.json'

export default {
  name: 'ProjectReports',
  components: {
    LogoIcon,
    AnalyticsScreen,
    SearchScreen,
    AlertsScreen,
    ReportsScreen,
    MainLayout,
    AnalyticsIcon,
    SearchIcon,
    AlertsIcon,
    ReportsIcon,
    SettingsIcon,
  },
  data() {
    return {
      settingName: 'Analytics',
      settings: [
        {
          name: 'Analytics',
          value: Analytics,
        },
        {
          name: 'Search',
          value: Search,
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
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
    openSetting(val) {
      this.settingName = val
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
  position: absolute;
  top: 16px;
  left: 24px;

  display: flex;
  flex-direction: column;
  align-items: center;

  width: 72px;
  height: 700px;

  border: 1px solid var(--sidebar-border-color);
  border-radius: 15px;
  background-color: var(--secondary-bg-color);

  .logo {
    cursor: pointer;

    width: 54px;
    margin: 18px 10px 94px;
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
    background-color: var(--primary-button-color);
  }

  .tooltip {
    position: absolute;
    top: 0;
    left: 50px;
    z-index: 1;

    visibility: hidden;
    text-align: center;

    padding: 10px;

    border-radius: 10px;

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
