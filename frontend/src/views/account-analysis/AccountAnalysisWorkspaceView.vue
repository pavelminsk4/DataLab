<template>
  <MainLayout v-if="workspace?.title">
    <div class="content-header">
      <MainLayoutTitleBlock
        :title="workspace.title"
        :description="workspace.description"
        :back-page="{
          name: 'main page',
          routeName: 'AccountAnalysisWorkspaces',
        }"
        :should-translate="false"
      >
      </MainLayoutTitleBlock>

      <BaseButtonWithTooltip
        :is-disabled="isProjectCreationAvailable"
        :has-tooltip="isProjectCreationAvailable"
        tooltip-title="Created the maximum possible number of projects!"
        @click="createProject"
      >
        <PlusIcon />
        <CustomText text="Add new profile" />
      </BaseButtonWithTooltip>
    </div>

    <div class="projects-wrapper scroll">
      <AccountAnalysisProjectsTable
        :values="filteredProjects"
        :members="workspace?.members"
        @go-to-project="goToProject"
      />
    </div>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import CustomText from '@/components/CustomText'
import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import AccountAnalysisProjectsTable from '@/components/account-analysis/AccountAnalysisProjectsTable'
import PlusIcon from '@/components/icons/PlusIcon'

const {mapState: mapAccountAnalyticsState} =
  createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisWorkspaceView',
  components: {
    CustomText,
    BaseButtonWithTooltip,
    MainLayout,
    MainLayoutTitleBlock,
    AccountAnalysisProjectsTable,
    PlusIcon,
  },
  data() {
    return {
      search: '',
    }
  },
  computed: {
    ...mapAccountAnalyticsState(['workspaces', 'loading']),
    ...mapGetters({
      department: get.DEPARTMENT,
      isLoading: get.LOADING,
    }),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    workspace() {
      const existingWorkspace = this.workspaces.find(
        (el) => el.id === +this.workspaceId
      )
      if (!existingWorkspace && !this.loading) return this.goToNotFoundPage()

      return existingWorkspace
    },
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_projects >=
        this.department?.max_projects
      )
    },
    filteredProjects() {
      if (!this.search) return this.workspace?.projects
      return this.workspace?.projects.filter((project) =>
        project.title.toLowerCase().includes(this.search.toLowerCase())
      )
    },
  },
  created() {
    this[action.CLEAR_STATE]()
  },
  methods: {
    ...mapActions([action.CLEAR_STATE]),
    goToProject(projectId) {
      this.$router.push({
        name: 'AccountAnalysisDashboard',
        params: {projectId, workspaceId: this.workspaceId},
      })
    },
    createProject() {
      this.$router.push({
        name: 'AccountAnalysisWorkspaceStep2',
        params: {workspaceId: this.workspaceId},
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.content-header {
  display: flex;
  justify-content: space-between;
}
</style>
