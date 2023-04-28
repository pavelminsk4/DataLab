<template>
  <div class="wrapper-input">
    <BaseInput
      v-model="searchText"
      :isSearch="true"
      placeholder="Search projects..."
      label=" "
    />
  </div>
  <div v-if="findedProjects.length" class="wrapper scroll">
    <ProjectsTableWithModules
      v-model="selectedProjects"
      :projects="findedProjects"
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

const {mapActions: mapSocialActions} = createNamespacedHelpers('social')
const {mapActions: mapActionsAlerts} = createNamespacedHelpers('alerts')

import ProjectsTableWithModules from '@/components/ProjectsTableWithModules'
import BaseInput from '@components/common/BaseInput'

import createAlertMixin from '@/lib/mixins/create-alerts.js'

export default {
  name: 'CreateAlertAddProject',
  components: {ProjectsTableWithModules, BaseInput},
  mixins: [createAlertMixin],
  data() {
    return {
      selectedProjects: [],
      searchText: '',
    }
  },
  computed: {
    ...mapGetters({projects: get.ALL_PROJECTS, department: get.DEPARTMENT}),
    ...mapState({
      newAlert: (state) => state.alerts.newAlert,
    }),
    isDisableNextBtn() {
      return !this.selectedProjects.length
    },
    findedProjects() {
      return this.projects.filter((project) =>
        project.title.includes(this.searchText)
      )
    },
  },
  created() {
    this.getOnlineProjects()
    this.getSocialProjects()
  },
  methods: {
    ...mapActions({
      getOnlineProjects: action.GET_PROJECTS,
    }),
    ...mapActionsAlerts({
      createNewAlert: action.CREATE_NEW_ALERT,
    }),
    ...mapSocialActions({getSocialProjects: action.GET_PROJECTS}),
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
