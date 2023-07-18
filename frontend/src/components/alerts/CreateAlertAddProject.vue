<template>
  <div class="wrapper-input">
    <BaseInput
      v-model="searchText"
      :isSearch="true"
      placeholder="Search projects..."
      label=" "
    />
  </div>
  <div v-if="foundProjects.length" class="wrapper scroll">
    <WorkspaceTableWithProjects
      v-model="selectedProjects"
      :projects="foundProjects"
      :workspaces="workspaces"
    />
  </div>
  <div v-else>No search results</div>
  <footer class="create-reports__footer">
    <ButtonWithArrow :is-disabled="isDisableNextBtn" @click="nextStep">
      <span>Next</span>
    </ButtonWithArrow>
  </footer>
</template>

<script>
import {mapActions, mapGetters, mapState, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import createAlertMixin from '@/lib/mixins/create-alerts.js'

import WorkspaceTableWithProjects from '@/components/WorkspaceTableWithProjects'
import BaseInput from '@components/common/BaseInput'

const {mapActions: mapSocialActions} = createNamespacedHelpers('social')
const {mapActions: mapActionsAlerts} = createNamespacedHelpers('alerts')

export default {
  name: 'CreateAlertAddProject',
  components: {WorkspaceTableWithProjects, BaseInput},
  mixins: [createAlertMixin],
  data() {
    return {
      selectedProjects: [],
      searchText: '',
    }
  },
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
      workspaces: get.ALL_WORKSPACES,
    }),
    ...mapState({
      newAlert: (state) => state.alerts.newAlert,
    }),
    projects() {
      return this.workspaces.map(({projects}) => projects).flat()
    },
    isDisableNextBtn() {
      return !this.selectedProjects.length
    },
    foundProjects() {
      return this.projects.filter((project) =>
        project.title.includes(this.searchText)
      )
    },
  },
  created() {
    this.getSocialWorkspaces()
    this.getOnlineWorkspaces()
  },
  methods: {
    ...mapActions({
      getOnlineWorkspaces: action.GET_WORKSPACES,
    }),
    ...mapSocialActions({
      getSocialWorkspaces: action.GET_WORKSPACES,
    }),
    ...mapActionsAlerts({
      createNewAlert: action.CREATE_NEW_ALERT,
    }),
    nextStep() {
      const projects = this.selectedProjects.map((project) => {
        const newModule =
          project.moduleType === 'Online' ? 'Project' : 'ProjectSocial'

        return {module_type: newModule, module_project_id: project.id}
      })
      this.createNewAlert({
        data: {...this.newAlert, items: projects},
        projectId: this.department.id,
      })
      this.$router.push({name: 'Alerts'})
    },
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  height: calc(100% - 250px);
}

.wrapper-input {
  max-width: 30%;

  margin: 40px 0 20px 0;
}
</style>
