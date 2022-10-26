<template>
  <MainLayout>
    <div class="settings-nav-wrapper">
      <div v-for="(item, index) in settings" :key="'setting' + index">
        <div
          :class="['nav-item', item.name === settingName && 'active-setting']"
          @click="openSetting(item.name)"
        >
          <component :is="item.name + 'Icon'" />

          {{ item.name }}
        </div>
      </div>
    </div>
    <component
      :is="settingName + 'Screen'"
      :current-project="currentProject"
      class="screen-wrapper"
    />
  </MainLayout>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import MainLayout from '@/components/layout/MainLayout'
import ReportsScreen from '@/components/project/screens/ReportsScreen'
import AlertsScreen from '@/components/project/screens/AlertsScreen'
import AnalyticsScreen from '@/components/project/screens/AnalyticsScreen'

import AnalyticsIcon from '@/components/icons/AnalyticsIcon'
import SearchIcon from '@/components/icons/SearchIcon'
import AlertsIcon from '@/components/icons/AlertsIcon'
import ReportsIcon from '@/components/icons/ReportsIcon'
import SettingsIcon from '@/components/icons/SettingsIcon'

export default {
  name: 'ProjectReports',
  components: {
    AnalyticsScreen,
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
        },
        {
          name: 'Search',
        },
        {
          name: 'Alerts',
        },
        {
          name: 'Reports',
        },
        {
          name: 'Settings',
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
      console.log(this.settingName)
    },
  },
}
</script>

<style lang="scss">
.settings-nav-wrapper {
  position: absolute;
  left: 0;

  display: flex;
  align-items: center;

  width: 100%;
  height: 50px;
  padding: 0 69px 0 79px;
  margin: -28px 0 0;

  background-color: var(--primary-button-color);

  .nav-item {
    display: flex;
    align-items: center;
    gap: 10px;

    padding: 8px 22px 10px 13px;

    cursor: pointer;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 22px;

    color: #ffffff;
  }

  .active-setting {
    border-radius: 8px;

    background: rgba(34, 42, 54, 0.4);
  }
}

.screen-wrapper {
  margin-top: 80px;
}
</style>
