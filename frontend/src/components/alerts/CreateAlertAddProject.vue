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
      newAlert: (state) => state.newAlert,
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
    setLoading() {
      this.isLoading = !this.isLoading
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
{ "items": [{"module_type":"Project", "module_project_id":1}], "title": "TEst",
"triggered_on_every_n_new_posts": 1, "how_many_posts_to_send": 1,
"alert_condition": "", "creator": 1, "department": null, "project": null,
"user": [1] }
