<template>
  <ProjectsTableWithModules
    v-model="selectedProjects"
    :projects="projects"
    :has-select-all="false"
  />
  <footer class="create-reports__footer">
    <ButtonWithArrow :is-disabled="isDisableNextBtn" @click="nextStep">
      <span>Next</span>
    </ButtonWithArrow>
  </footer>
</template>

<script>
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import createReportMixin from '@/lib/mixins/create-report.js'

import ProjectsTableWithModules from '@/components/ProjectsTableWithModules'

const {mapActions: mapSocialActions} = createNamespacedHelpers('social')

export default {
  name: 'CreateReportAddProject',
  mixins: [createReportMixin],
  components: {
    ProjectsTableWithModules,
  },
  data() {
    return {
      selectedProjects: [],
    }
  },
  computed: {
    ...mapGetters({projects: get.ALL_PROJECTS}),
    isDisableNextBtn() {
      return !this.selectedProjects.length
    },
  },
  created() {
    this.tableHeader = [
      {name: 'project name', width: ''},
      {name: 'type', width: '14%'},
      {name: 'keywords', width: '20%'},
      {name: 'assigned user', width: '11%'},
      {name: 'creator', width: '16%'},
      {name: 'date', width: '11%'},
    ]

    this.getOnlineProjects()
    this.getSocialProjects()
  },
  methods: {
    ...mapActions({getOnlineProjects: action.GET_PROJECTS}),
    ...mapSocialActions({getSocialProjects: action.GET_PROJECTS}),
    projectMembers(projectMembersIds) {
      return projectMembersIds.length
    },
    projectCreationDate(date) {
      return new Date(date).toLocaleDateString('ro-RO')
    },

    selectAll(isSelectAll) {
      this.selectedProjects = isSelectAll
        ? this.projects.map((value) => value.id)
        : []
    },
    nextStep() {
      const nextStep = 4
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_REPORT]({
        step: nextStep,
        projects: this.selectedProjects,
      })
      this.$router.push({name: nextStepName})
    },
  },
}
</script>

<style lang="scss" scoped>
.project-row {
  position: relative;

  &:last-child {
    .divider {
      display: none;
    }
  }
}

.divider {
  position: absolute;
  left: 0;
  bottom: 0;

  width: calc(100% - 5px);

  border-bottom: var(--border-primary);
}

.creator {
  display: flex;
  align-items: center;
}

.chips-height {
  height: 28px;
}
</style>
