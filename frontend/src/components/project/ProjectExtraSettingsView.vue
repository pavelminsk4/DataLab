<template>
  <MainLayout
    v-if="currentProject"
    :is-project-extra-settings="true"
    :is-visible-logo="false"
  >
    <nav class="settings-nav-wrapper">
      <li
        v-for="(item, index) in settings"
        :key="'setting' + index"
        :class="['nav-item', item.name === routeName && 'active-setting']"
        @click="openSetting(item.name)"
      >
        <SidebarIcon :json="item.value" />

        <div>{{ item.name }}</div>
      </li>
    </nav>

    <router-view :current-project="currentProject"></router-view>
  </MainLayout>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import MainLayout from '@/components/layout/MainLayout'

import SidebarIcon from '@/components/icons/SidebarIcon'

import Alerts from '@/components/icons/animation/Alerts.json'
import Search from '@/components/icons/animation/Search.json'
import Reports from '@/components/icons/animation/Reports.json'
import Analytics from '@/components/icons/animation/Analytics.json'

export default {
  name: 'ProjectReports',
  components: {
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
  --padding-top: calc(var(--header-height) + 24px);

  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;

  display: flex;
  flex-direction: column;
  align-items: center;

  width: 210px;
  height: 100vh;
  padding: var(--padding-top) 24px 20px 12px;

  border-right: 1px solid var(--border-color);
  background-color: var(--background-secondary-color);

  .nav-item {
    display: flex;
    align-items: center;

    width: 172px;
    height: 44px;
    padding: 12px 16px;
    margin-bottom: 10px;

    cursor: pointer;

    font-weight: 500;
    font-size: 16px;
    line-height: 20px;
    color: var(--typography-secondary-color);

    :first-child {
      margin-right: 7px;
    }
  }

  .active-setting {
    border-radius: 18px;
    background-color: var(--primary-active-color);

    color: var(--typography-title-color);
  }
}
</style>
