<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock
        v-if="workspace?.title"
        :title="workspace.title"
        :description="workspace.description"
        :back-page="{
          name: 'workspaces',
          routeName: 'ComparisonWorkspaces',
        }"
      >
      </MainLayoutTitleBlock>

      <BaseButtonWithTooltip
        :is-disabled="false"
        :has-tooltip="false"
        tooltip-title="Created the maximum possible number of projects!"
        @click="createProject"
        class="create-btn"
      >
        <PlusIcon /> Add new project
      </BaseButtonWithTooltip>
    </div>

    <div class="projects-wrapper scroll">
      <ComparisonProjectsTable
        :values="filteredProjects"
        :members="workspace?.members"
        @go-to-project="goToProject"
      />
    </div>
  </MainLayout>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ComparisonProjectsTable from '@/components/comparison/ComparisonProjectsTable'
import PlusIcon from '@/components/icons/PlusIcon'
import {isAllFieldsEmpty} from '@/lib/utilities'

const {mapActions, mapState} = createNamespacedHelpers('comparison')

export default {
  name: 'ComparisonWorkspaceView',
  components: {
    BaseButtonWithTooltip,
    MainLayout,
    MainLayoutTitleBlock,
    ComparisonProjectsTable,
    PlusIcon,
  },
  props: {
    workspaces: {type: Array, required: true},
  },
  data() {
    return {
      search: '',
    }
  },
  computed: {
    ...mapState(['modulesProjects']),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    workspace() {
      return this.workspaces.find((el) => el.id === +this.workspaceId)
    },
    currentModule() {
      return this.workspace?.cmpr_workspace_projects[0].cmpr_items[0] ===
        'Project'
        ? 'Online'
        : 'Social'
    },
    filteredProjects() {
      if (!this.search) return this.workspace?.cmpr_workspace_projects
      return this.workspace?.cmpr_workspace_projects.filter((project) =>
        project.title.toLowerCase().includes(this.search.toLowerCase())
      )
    },
  },
  async created() {
    if (!this.workspaces.length) await this[action.GET_WORKSPACES]()
    if (isAllFieldsEmpty(this.modulesProjects)) this[action.GET_PROJECTS]()
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES, action.GET_PROJECTS]),
    goToProject(projectId) {
      this.$router.push({
        name: 'ComparisonFeaturesView',
        params: {projectId, workspaceId: this.workspaceId},
      })
    },
    createProject() {
      this.$router.push({
        name: 'ComparisonWorkspaceStep2',
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
.create-btn {
  align-self: flex-end;
}
</style>
