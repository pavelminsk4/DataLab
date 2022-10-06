<template>
  <MainLayout>
    <div class="settings-nav-wrapper">
      <div v-for="(item, index) in settings" :key="'setting' + index">
        <div class="nav-title">{{ item.name }}</div>
      </div>
    </div>
    <ReportsScreen v-if="false" />
    <AlertsScreen v-if="false" />
    <AnalyticsScreen :current-project="currentProject" class="screen-wrapper" />
  </MainLayout>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import MainLayout from '@/components/layout/MainLayout'
import ReportsScreen from '@/components/project/screens/ReportsScreen'
import AlertsScreen from '@/components/project/screens/AlertsScreen'
import AnalyticsScreen from '@/components/project/screens/AnalyticsScreen'

export default {
  name: 'ProjectReports',
  components: {AnalyticsScreen, AlertsScreen, ReportsScreen, MainLayout},
  data() {
    return {
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

  .nav-title {
    margin-right: 34px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 22px;

    color: #ffffff;
  }
}

.screen-wrapper {
  margin-top: 80px;
}
</style>
